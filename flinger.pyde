#purpose of project: make a booger flinging game just because

activeMouse = False

startMouseX = 0 
startMouseY = 0

strokeN = 0

def setup():
    background(0)
    stroke(255)
    size(700, 400)
    
def draw():
    if not mousePressed:
        activeMouse = False
    else:
        incrementStroke()
        line(startMouseX, startMouseY, mouseX, mouseY)
    
def incrementStroke():
    global strokeN
    strokeN += 1
    if strokeN >= 255:
        strokeN = 0
    stroke(strokeN)
    
def mousePressed():
    global activeMouse
    if not activeMouse:
        activeMouse = True
        startMouseX = mouseX
        startMouseY = mouseY
        
    