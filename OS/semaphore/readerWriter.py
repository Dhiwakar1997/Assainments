import threading
import time
import random

def getRandomNumber(endVal=4):
    return random.uniform(1, endVal)

# Shared Memory variables
quotes = [  'This is the 1st quote',
            'This is the 2nd quote',
            'This is the 3ed quote',
            'This is the 4th quote',
            'This is the 5th quote',
        ]

 
# Declaring Semaphores
mutex = threading.Semaphore()
rw_mutex = threading.Semaphore()
readerCount = 0
quoteCount = -1
maxReaderCount = 3
closingCount = 3
content =''

class Writer(threading.Thread):
    
  def run(self):
    global mutex,quotes,content, quoteCount
    while quoteCount < len(quotes)-1:
        rw_mutex.acquire()
        quoteCount += 1
        content = quotes[quoteCount]
        print(f'\nWriting {quoteCount+1}: \t"{content}"\n')
        rw_mutex.release()
        time.sleep(getRandomNumber(1))
       


class Reader(threading.Thread):
    def __init__(self,*args, **kwargs):
        self.count = kwargs.pop('count')
        super().__init__()

    def run(self):
        global mutex,quotes,readerCount, quoteCount, content, closingCount
        while True:
            if content!="":
                mutex.acquire()
                readerCount= readerCount+1
                if readerCount == 1:
                    rw_mutex.acquire()
                mutex.release()

                print(f'The quote read by reader {self.count+1} :\t"{content}"\n')

                mutex.acquire()
                readerCount-=1
                if readerCount==0:
                    rw_mutex.release()
                    #content=""
                mutex.release()
                time.sleep(getRandomNumber(2))

            if quoteCount >= len(quotes)-1:
                closingCount-=1
                if closingCount <=0:
                    break
                
if __name__ == "__main__":
    writer = Writer()
    readers = [Reader(count=i) for i in range(maxReaderCount)]

    writer.start()
    for reader in readers:
        reader.start()

    writer.join()
    for reader in readers:
        reader.join()

