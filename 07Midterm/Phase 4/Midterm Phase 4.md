# itp

## Brianna

**Midterm Phase 4**


WOW this part took me so long

I think I was having the biggest brain fart ever.

I copied in the code from the preious sketch, and added in the for loop as I thought it should work.



this is what my draw function looked like

def draw():
    background(255)  
    gridScale = 20
    # Draw the object at the center of the canvas
    for i in range(gridScale):
        for j in range(gridScale):
            drawObject(i * width/gridScale, j * width/gridScale, 0.5)

this did make the grid, but didnt scale the image tiles correctly, so I tried to do this:

def draw():
    background(255)  
    gridScale = 20
    # Draw the object at the center of the canvas
    for i in range(gridScale):
        for j in range(gridScale):
            drawObject(i * width/gridScale, j * width/gridScale, gridScale)

obviously this didn't work either. I tried moving around a bunch of other things to no avail for like 2 hours.

After not being able to figure it out for a very, very long time, I turned to my fellow classmate Neil, who was gracious and wonderful enough to give me a hand and look at my code. He discovered that I was not using a scale factor correctly, and asked that I figure out the increments that I was printing tiles at. I found that I was printing a tile every 80 pixels, giving me an equation to work with. I promised him ice cream.

That brought me to this equation:

def setup():
    size(400, 400)  # Set the size of canvas
    noLoop()  # Disable continuous looping


def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    rectMode(CENTER)
    fill(0)  # fill with black
    rect(50, 50, 10, 30)
    triangle(45, 65, 35, 60, 45, 55)
    triangle(55, 65, 65, 60, 55, 55)
    triangle(45, 35, 50, 25, 55, 35)
    rect(50, 70, 5, 15)
    ellipse(50, 80, 10, 5)
    pop()



def draw():
    background(255)  
    gridScale = 20
    # Draw the object at the center of the canvas
    for i in range(gridScale):
        for j in range(gridScale):
            drawObject(i * width/gridScale, j * width/gridScale, gridScale/40)

this was also broken, so I added a float

def setup():
    size(400, 400)  # Set the size of canvas
    noLoop()  # Disable continuous looping


def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    rectMode(CENTER)
    fill(0)  # fill with black
    rect(50, 50, 10, 30)
    triangle(45, 65, 35, 60, 45, 55)
    triangle(55, 65, 65, 60, 55, 55)
    triangle(45, 35, 50, 25, 55, 35)
    rect(50, 70, 5, 15)
    ellipse(50, 80, 10, 5)
    pop()



def draw():
    background(255)  
    gridScale = 20
    # Draw the object at the center of the canvas
    for i in range(gridScale):
        for j in range(gridScale):
            drawObject(i * width/gridScale, j * width/gridScale, gridScale/40.0)

this was making them bigger instead of making them smaller as the grid became larger. So I tried putting the number on the other side like this:

def setup():
    size(400, 400)  # Set the size of canvas
    noLoop()  # Disable continuous looping


def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    rectMode(CENTER)
    fill(0)  # fill with black
    rect(50, 50, 10, 30)
    triangle(45, 65, 35, 60, 45, 55)
    triangle(55, 65, 65, 60, 55, 55)
    triangle(45, 35, 50, 25, 55, 35)
    rect(50, 70, 5, 15)
    ellipse(50, 80, 10, 5)
    pop()



def draw():
    background(255)  
    gridScale = 20
    # Draw the object at the center of the canvas
    for i in range(gridScale):
        for j in range(gridScale):
            drawObject(i * width/gridScale, j * width/gridScale, 4.0/gridScale)

and it worked! THANK GOD
