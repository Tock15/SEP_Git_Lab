import turtle as t
from disk import Disk
class Pole:
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.thick = thick
        self.length = length

        self.stack = []
        self.toppos = 0
    def showPole(self):
        t.pu()
        t.goto(self.xpos, self.ypos)
        t.pd()
        t.forward(self.thick / 2)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.thick)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.thick / 2)
    def pushDisk(self, disk):
        disk.newpos(self.xpos, self.ypos + self.toppos*20)
        self.stack.append(disk)
        self.toppos += 1
        disk.showDisk()

        
    def popDisk(self):
        disk = self.stack.pop()
        self.toppos -= 1
        disk.clearDisk()
        disk.newpos(disk.dxpos, 120)
        disk.showDisk()
        return disk


if __name__ == "__main__":
    p = Pole("A",150,0)
    p.showPole()
    d1 = Disk("D1")
    p.pushDisk(d1)
    p.popDisk()


    t.mainloop()

