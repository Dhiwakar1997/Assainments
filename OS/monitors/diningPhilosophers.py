import threading
 
class MonitorDP(threading.Thread):
    
    def __init__(self, numOfPhilosophers):
        self.numOfPhilosophers  = numOfPhilosophers 
        self.chopStick =[ threading.Semaphore() for i in range(numOfPhilosophers)]
        self.states = [ "THINKING" for i in range(numOfPhilosophers)] 

    def pickUp(self, philosopherId):
        self.states[philosopherId] = "HUNGRY"
        print(f"\nPhilosopher {philosopherId} is hungry")
        self.test(philosopherId)
        if self.states[philosopherId]!="EATING":
            self.chopStick[philosopherId].acquire() #wait 


    def putDown(self, philosopherId):
        self.states[philosopherId] = "THINKING"
        print(f"Philosopher {philosopherId} putDown the chopstick\n")
        self.test((philosopherId+(self.numOfPhilosophers-1))%self.numOfPhilosophers)
        self.test((philosopherId+1)%self.numOfPhilosophers)

    def test(self, philosopherId):
        if self.states[(philosopherId+(self.numOfPhilosophers-1))%self.numOfPhilosophers]!="EATING" \
        and self.states[(philosopherId+1)%self.numOfPhilosophers] != "EATING"\
        and self.states[philosopherId] == "HUNGRY" :

            self.states[philosopherId] = "EATING"
            print(f"\nPhilosopher {philosopherId} pickup the chopstick")
            print(f"Philosopher {philosopherId} is eating")

            self.chopStick[philosopherId].release() #signal 


if __name__ == "__main__":
    numOfPhilosophers = 5
    diningPhilosophers = MonitorDP(numOfPhilosophers)
    diningPhilosophers.pickUp(1)
    diningPhilosophers.pickUp(2)
    diningPhilosophers.pickUp(4)
    diningPhilosophers.pickUp(0)
    diningPhilosophers.putDown(1)
    diningPhilosophers.pickUp(3)
    diningPhilosophers.putDown(2)
    diningPhilosophers.putDown(4)
    diningPhilosophers.putDown(0)


