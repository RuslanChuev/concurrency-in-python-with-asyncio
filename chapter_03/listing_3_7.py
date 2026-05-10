import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1) #A

    if len(events) == 0: #B
        print('No events, waiting a bit more!')

    for event, _ in events:
        event_socket = event.fileobj

        # Новое подключение
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"I got a connection from {address}")
            selector.register(connection, selectors.EVENT_READ)
        else:
            # Чтение данных от клиента
            try:
                data = event_socket.recv(1024)
            except (ConnectionResetError, ConnectionAbortedError, OSError):
                # Клиент нештатно разорвал соединение
                print(f"Client forcibly closed connection: {event_socket.getpeername()}")
                selector.unregister(event_socket)
                event_socket.close()
                continue

            if data:
                # Данные получены — эхо
                print(f"I got some data: {data}")
                # В неблокирующем режиме send() может отправить не всё,
                # но для учебного примера оставим однократную попытку.
                # При реальной разработке нужно использовать sendall() в блокирующем режиме
                # или организовать буферизацию с отслеживанием EVENT_WRITE.
                event_socket.send(data)
            else:
                # data == b''  => клиент закрыл соединение (вежливо)
                print(f"Client closed connection: {event_socket.getpeername()}")
                selector.unregister(event_socket)
                event_socket.close()
