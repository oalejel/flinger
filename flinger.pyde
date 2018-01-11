#purpose of project: make a booger flinging game just because

activeMouse = False

startMouseX = 0 
startMouseY = 0

strokeN = 0

lines = []

class LineObject:
    def __init__(self, points):
        self.points = points
        self.vect = None
        self.timeToRemove = False
    
    def _shorten(self):
        if self.vect == None:
            self.vect = [self.points[2] - self.points[0], self.points[3] - self.points[1]]
        else:
            self.vect = [x * 0.6 for x in self.vect]
            #may have to remove if too small
            if self.vect[0] < 0.2 and self.vect[1] < 0.2:
                self.timeToRemove = True
            
    def _draw(self):
        if self.vect != None:
            line(self.points[0], self.points[1], self.points[0] + self.vect[0], self.points[1] + self.vect[1])
        
def setup():
    background(0)
    stroke(255)
    size(700, 400)
    
def draw():
    background(0)
    global activeMouse
    if activeMouse:
        line(startMouseX, startMouseY, mouseX, mouseY)
        
    for l in lines:
        l._draw()
        l._shorten()
        if l.timeToRemove:
            println("removing from list")
            lines.remove(l)
    
    
def mousePressed():
    println("pressed")
    global startMouseX, startMouseY, activeMouse
    activeMouse = True
    startMouseX = mouseX
    startMouseY = mouseY
    
def mouseReleased():
    println("released!")
    global activeMouse
    activeMouse = False
    
    println("new line created")
        #once this happens, we can store our last draw line and animate shrink
    global lines
    l = LineObject([startMouseX, startMouseY, mouseX, mouseY])
    lines.append(l)
        
#no longer used    
def incrementStroke():
    global strokeN
    strokeN += 1
    if strokeN >= 255:
        strokeN = 0
    stroke(strokeN)