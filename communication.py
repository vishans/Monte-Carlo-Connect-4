import socket
import threading
from datetime import datetime
ENCODING = 'ascii'


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)



def handle(client):
    while True:
        #try:
            message = client.recv(1024).decode(ENCODING)
            print(message)
            content = message.split('#')

            name = content[0]
            msg = content[1]
            now = datetime.now().strftime('%d/%m/%y  %H:%M:%S')
            print(f'[{now}] {name}: {msg}')
            broadcast(message.encode(ENCODING))

        # except:
        #     index = clients.index(client)
        #     clients.remove(client)
        #     client.close()
        #     nickname = nicknames[index]
        #     broadcast(f'{nickname} left the chat'.encode(ENCODING))
        #     print(f'{nickname} left the chat')
        #     nicknames.remove(nickname)
        #     break
        



def receive():
    while True:
        client, address = server.accept()
        print(f'\t\tConnected with {address}')

        client.send('NICK'.encode(ENCODING))
        nickname = client.recv(1024).decode(ENCODING)
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname}#JOINED'.encode(ENCODING))
        client.send(f'_#CONN'.encode(ENCODING))


        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == '__main__':
    print('Server is listening')
    receive()