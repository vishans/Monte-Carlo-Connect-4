import socket
import threading
from datetime import datetime

class Client:

    def __init__(self, nickname) -> None:

        self.ENCODING = 'ascii'

        self.nickname = nickname
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 55555))


        # for sending stream

        self.send = None
        self.allow_send = False

        # client response

        self.clients_response = None
        self.cls_recved = False

        self.status_packet = None
        self.opponent_online = False


    def preliminary_recv(self):
        #client should send if want to host or not

        self.client.send(self.status_packet)

        message = self.client.recv(1024).decode(self.ENCODING)

        if message == '0':
            return 0

        elif message == 'HOST_ALREADY':
            print('Someone is already a host on the server. You cannot host.')
            print('Try joining as the second player...')

        elif message == 'NO_HOST':
            print('There is no host on the server. Try hosting yourself')
            print('And then invite your friend to joion as the second player.')

        else:
            print('An internal server error occurred. Please try again later')


        return 1



    
    def receive(self):
        while True:
            try:

                if self.preliminary_recv() == 0:

                    message = self.client.recv(1024).decode(self.ENCODING)
                    #print(message)
                    #print(message)
                    if message == 'NICK': # gotta send server the nickname
                        self.client.send(self.nickname.encode(self.ENCODING))
                    
                    else:
                        content = message.split('#')
                        opcode = content[0]
                        operand = content[1]
                        if 'P' in opcode:
                            # now = datetime.now().strftime('%d/%m/%y  %H:%M:%S')
                            
                            print(f'Opponent played {operand[-1]}')

                            self.clients_response = operand[-1]
                            self.cls_recved = True
                        # print(message)

                        elif opcode == 'L':
                            print('Opponent disconnected')


                        elif opcode == 'C':
                            print('config')

                    

            except:

                print('Server has shut down.')
                self.client.close()
                break


    def write(self):
        while True:
            
           if self.allow_send == True:
                self.client.send(f'{self.nickname}#{self.send}'.encode(self.ENCODING))

                self.allow_send = False


    def playMove(self,move):

        self.send = f'P{move}'
        self.allow_send = True


    def leaveGame(self):
        self.send = f'L'
        self.allow_send = True


    def sendConfig(self,my_symbol,who_goes_first):
        self.send = f'C{my_symbol}{who_goes_first}'
        self.allow_send = True


    def silentlyLeaveGame(self):
        self.send = f'SL'


    def getClientResponse(self):
        while not(self.cls_recved):
            pass #block until client plays 

        self.cls_recved = False

        return self.clients_response

    



    def start_communication(self):


        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

        