

import threading
import time 


class foo:

    def __init__(self) -> None:
        self.run = True


    def dummyfunc(self, x):
        y = x

        while self.run:

            

            print(y)
            time.sleep(1)


    def startThread(self,x = 5):

        threading.Thread(target = self.dummyfunc,args = (x,)).start()



A = foo()
B = foo()
C = foo()

A.startThread()
B.startThread(9)
C.startThread(69)

count = 0
while count < 3:
    time.sleep(1)
    count +=1


A.run = False
B.run = False

for t in threading.enumerate():
    print(t.is_alive())


print(f'active = {threading.active_count()}')
A.run = True
A.startThread()

print(f'active = {threading.active_count()}')