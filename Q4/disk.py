import turtle
t = turtle.Turtle()
t.speed(0)

class Disk:
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    def showDisk(self):
        t.pencolor("black")
        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)

        t.down()
        t.forward(self.dwidth//2)
        t.left(90)
        t.forward(self.dheight)
        t.left(90)
        t.forward(self.dwidth)
        t.left(90)
        t.forward(self.dheight)
        t.left(90)
        t.forward(self.dwidth//2)

        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)
    def newpos(self, xpos, ypos):
        self.clearDisk()

        self.dxpos = xpos
        self.dypos = ypos
        
    def clearDisk(self):
        t.color("white")
        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)

        t.down()
        t.backward(self.dwidth//2)
        t.right(90)
        t.backward(self.dheight)
        t.right(90)
        t.backward(self.dwidth)
        t.right(90)
        t.backward(self.dheight)
        t.right(90)
        t.backward(self.dwidth//2)

        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)

if __name__ == "__main__":
    disk = Disk("niggy")
    disk.showDisk()
    disk.newpos(50, 50)
    turtle.done()
