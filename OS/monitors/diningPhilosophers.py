import threading
import random
import time
 
# Shared Memory variables
numOfPhilosophers = 5
chopStickCount = numOfPhilosophers

totalServingAvailable = 15
servingCounter = 0

# Declaring Semaphores
chopStrick =[ threading.Semaphore() for i in range(chopStickCount)]

def getRandomNumber(endVal=4):
    return random.randint(1, endVal)
 
# Philosopher Thread Class
class Philosopher(threading.Thread):
    def __init__(self,*args, **kwargs):
        self.count = kwargs.pop('count')
        super().__init__()

    def run(self): 
        global  chopStrick, totalServingAvailable, servingCounter

        while servingCounter<totalServingAvailable:
            servingCounter+=1
            print(f"Serving Count : {servingCounter}")
            chopStrick[self.count].acquire()
            chopStrick[(self.count+1)%numOfPhilosophers].acquire()
            #Critical part
            print(f"Philosopher {self.count+1} is eating")
            time.sleep(getRandomNumber(3))
            chopStrick[self.count].release()
            chopStrick[(self.count+1)%numOfPhilosophers].release()
            print(f"Philosopher {self.count+1} is thinking")
            time.sleep(getRandomNumber())
       

if __name__ == "__main__":
    philosophers = [Philosopher(count=i) for i in range(numOfPhilosophers)]
    for philosopher in philosophers:
        philosopher.start()
    for philosopher in philosophers:
        philosopher.join()
