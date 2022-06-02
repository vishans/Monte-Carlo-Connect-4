import socket
import threading
from datetime import datetime


class Server:
    def __init__(self) -> None:
        
        self.ENCODING = 'ascii'


        host = '127.0.0.1'
        port = 55555

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host,port))
        self.server.listen()

        self.is_there_a_host = False
        self.clients = []
        self.nicknames = []
        
        



    def broadcast(self,message):
        for nickname, client in zip(self.nicknames,self.clients):

            if nickname == message.split('#')[0]:
                continue
            
            client.send(message)



    def handle(self,client):
        while True:
            try:
                message = client.recv(1024).decode(self.ENCODING)
                print(message)
                content = message.split('#')

                name = content[0]
                msg = content[1]
                now = datetime.now().strftime('%d/%m/%y  %H:%M:%S')
                print(f'[{now}] {name}: {msg}')
                self.broadcast(message.encode(self.ENCODING))

            except:

                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'{nickname} left the chat'.encode(self.ENCODING))
                print(f'{nickname} left the chat')
                self.nicknames.remove(nickname)
                break
            



    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f'\t\tTrying to connect with {address}')

            # client.send('STS'.encode(self.ENCODING))
            sts = client.recv(1024).decode(self.ENCODING)

            if sts == 'HOST':
                if not self.is_there_a_host:
                    allow = True
                    message = '0'

                else:
                    allow = False
                    message = 'HOST_ALREADY'


            elif sts == 'SCND':
                if not self.is_there_a_host:
                    allow = False
                    message = 'NO_HOST'

                else:

                    allow = True
                    message = '0'


            else:
                allow = False
                message = '1'


            client.send(message.encode(self.ENCODING))

            if message == '0':

                print(f'Successful connection with {address}')

                client.send('NICK'.encode(self.ENCODING))
                nickname = client.recv(1024).decode(self.ENCODING)
                self.nicknames.append(nickname)
                self.clients.append(client)

                print(f'Nickname of the client is {nickname}')
                self.broadcast(f'{nickname}#JOINED'.encode(self.ENCODING))
                client.send(f'_#CONN'.encode(self.ENCODING))


                thread = threading.Thread(target=self.handle, args=(client,))
                thread.start()

            else:
                print('UNSUCCESS {client} Error = {message}')

# if __name__ == '__main__':
#     print('Server is listening')
#     receive()