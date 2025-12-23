from pole import Pole
from disk import Disk
from turtle import *

class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showPole()
        self.workspacep.showPole()
        self.destinationp.showPole()
        for i in range(n):
            self.startp.pushDisk(Disk("d"+str(i),0,i*150,20,(n-i)*30))

    def move_disk(self,start,destination):
        disk = start.popDisk()
        destination.pushDisk(disk)
    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,s,w,d)
    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)

h = Hanoi()
h.solve()

exitonclick()
