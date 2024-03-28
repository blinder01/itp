def setup():
    size(400, 400) 
    noStroke()
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    rectMode(CENTER)
    fill(0) # fill with black
    rect(50, 50, 10, 30)
    triangle(45, 65, 35, 60, 45, 55)
    triangle(55, 65, 65, 60, 55, 55)
    triangle(45, 35, 50, 25, 55, 35)
    rect(50, 70, 5, 15)  
    ellipse(50, 80, 10, 5)
    pop()
    
def draw():
    drawObject(0,0,1)
    drawObject(0,200,1)
