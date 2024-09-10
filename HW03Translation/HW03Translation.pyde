small_diameter= 10
large_diameter = 3 * small_diameter

def setup():
    size(displayWidth, displayHeight)
    background(255, 215, 0) #sets background to "gold" 

def draw():
    stroke(0)
    fill(0)
    
    for x in range(0, width, (5 * small_diameter)):
        for y in range(0, height, (5 * small_diameter)):
            ellipse(x, y, small_diameter, small_diameter)
 
    for x in range(0, width, (10 * small_diameter)):
        for y in range(0, height, (10 * small_diameter)):
            ellipse(x, y, large_diameter, large_diameter)
    
    translate(5 * small_diameter, 5 * small_diameter)
    for x in range(0, width, (10 * small_diameter)):
        for y in range(0, height, (10 * small_diameter)):
            ellipse(x, y, large_diameter, large_diameter)
