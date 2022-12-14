import threading
import random
 
# Shared Memory variables
numOfPhilosophers = 5
chopStickCount = numOfPhilosophers
totalServingAvailable = 10

def getRandomNumber(endVal=4):
    return random.uniform(1, endVal)
 
class MonitorDP(threading.Thread):
    
    def __init__(self):
        self.chopStick =[ threading.Semaphore() for i in range(chopStickCount)]
        self.states = [ "THINKING" for i in range(numOfPhilosophers)] 

    def pickUp(self, philosopherId):
        self.states[philosopherId] = "HUNGRY"
        print(f"\nPhilosopher {philosopherId} is hungry")
        self.test(philosopherId)
        if self.states[philosopherId]=="EATING":
            self.chopStick[philosopherId].acquire() #wait 


    def putDown(self, philosopherId):
        self.states[philosopherId] = "THINKING"
        print(f"Philosopher {philosopherId} putDown the chopstick\n")
        self.test((philosopherId+(numOfPhilosophers-1))%numOfPhilosophers)
        self.test((philosopherId+1)%numOfPhilosophers)

    def test(self, philosopherId):
        if self.states[(philosopherId+(numOfPhilosophers-1))%numOfPhilosophers]!="EATING" \
        and self.states[philosopherId] == "HUNGRY" \
        and self.states[(philosopherId+1)%numOfPhilosophers] != "EATING":
            self.states[philosopherId] = "EATING"
            print(f"\nPhilosopher {philosopherId} pickup the chopstick")
            print(f"Philosopher {philosopherId} eating")
            self.chopStick[philosopherId].release() #signal 


if __name__ == "__main__":
    diningPhilosophers = MonitorDP()
    diningPhilosophers.pickUp(1)
    diningPhilosophers.pickUp(2)
    diningPhilosophers.pickUp(4)
    diningPhilosophers.pickUp(0)
    diningPhilosophers.putDown(1)
    diningPhilosophers.pickUp(3)
    diningPhilosophers.putDown(2)
    diningPhilosophers.putDown(4)
    diningPhilosophers.putDown(0)


