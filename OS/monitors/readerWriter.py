import threading
import time
import random
 
# Shared Memory variables
quotes = ['The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela',
        'The way to get started is to quit talking and begin doing. -Walt Disney',
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
        "Life is what happens when you're busy making other plans. -John Lennon"
        ]

 
# Declaring Semaphores
mutex = threading.Semaphore()
rw_mutex = threading.Semaphore()
readerCount = 0
quoteCount = -1
maxReaderCount = 3
content =''

class Writer(threading.Thread):
  def run(self):
    global mutex,quotes,content, quoteCount
    while quoteCount < len(quotes)-1:
        rw_mutex.acquire()
        quoteCount += 1
        content = quotes[quoteCount]
        print(f'Writing {quoteCount}: \t"{content}"\n')
        rw_mutex.release()
        time.sleep(1)
       


class Reader(threading.Thread):
    def run(self):
        global mutex,quotes,readerCount, quoteCount, content
        while quoteCount < len(quotes)-1:
            if content!="":
                mutex.acquire()
                readerCount= readerCount+1
                if readerCount == 1:
                    rw_mutex.acquire()
                mutex.release()

                print(f'The quote read {readerCount} :\t"{content}"\n')

                mutex.acquire()
                readerCount-=1
                if readerCount==0:
                    rw_mutex.release()
                    #content=""
                mutex.release()
                time.sleep(2)
                
if __name__ == "__main__":
    writer = Writer()
    readers = [Reader() for i in range(maxReaderCount)]

    writer.start()
    for reader in readers:
        reader.start()

    writer.join()
    for reader in readers:
        reader.join()

