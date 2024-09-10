#Midterm Code Translation

class Agent:    
    def __init__(self):
        self.x = random.randrange(17, width - 17)
        self.y = random.randrange(17, height - 17)
        self.vx = random.randrange([-3, 3, 1])
        self.vy = random.randrange([-3, 3, 1])
        self.radius = random.randrange(8, 16)
        self.diam = 2 * self.radius
    
    def update():
        self.updateByVelocity()
        self.bounceBoundary()
    
    def bounceBoundary(): #if agent gets to the edges, bounce back
        if (self.x + self.radius >= width or self.x - self.radius <= 0):
            self.vx *= -1
        
        if (self.y + self.radius >= height or self.y - self.radius <= 0):
            self.vy *= -1
    
    def wrapBoundary(): #if agent gets to the edges, wrap around to the opposite edge
        if(self.x > width):
            self.x = self.x % width
        if(self.x < 0):
            self.x = self.x + width
        if(self.y > height):
            self.y = self.y % height
        if(self.y < 0):
            self.y = self.y + height
    
    def resetBoundary(): #if agent gets to the edges, reset its position, velocity, etc
        if(self.x > width or self.x < 0 or self.y > height or self.y < 0):
            self.x = random.randrange(17, width - 17)
            self.y = random.randrange(17, height - 17)
            self.vx = random.randrange([-3, 3, 1])
            self.vy = random.randrange([-3, 3, 1])
            self.radius = random.randrange(8, 16)
            self.diam = 2 * self.radius
    
    def updateByVelocity(): #use velocity values to update position
        self.x += self.vx
        self.y += self.vy
    
    def updaterandrange(): #use random velocity values to update position
        self.vx = random.randrange([-4, 4, 1])
        self.vy = random.randrange([-4, 4, 1])
        self.x += self.vx
        self.y += self.vy
    
    def distComp(agentA, agentB):
        distA = math.dist(self.x, self.y, agentA.x, agentA.y)
        distB = math.dist(self.x, self.y, agentB.x, agentB.y)
        return distA - distB
    
    def updateNearest(): #move away from nearest agent
        sortedByDistance = agents.sorted(self.distComp.bind(self))
        closestAgent = sortedByDistance[1]
        self.vx = map(closestAgent.x - self.x, -width, width, 4, -4)
        self.vy = map(closestAgent.y - self.y, -height, height, 4, -4)
        self.x += self.vx
        self.y += self.vy
    
    #draw agent
    def drawAgent():
        ellipse(self.x, self.y, self.diam)
    
    def draw(): #draw based on currentMode
        if (currentMode == POINT_MODE):
            stroke(0)
            self.drawPoint()
        elif (currentMode == FURTHEST_MODE):
            stroke(0, 8)
            self.drawFurthest()
        elif (currentMode == NEAREST_MODE):
            stroke(0, 8)
            self.drawNearest()
        elif (currentMode == OVERLAP_MODE):
            stroke(0, 16)
            noFill()
            self.drawOverlap()
    
    #draw black point at x, y
    def drawPoint():
        point(self.x, self.y)
    
    def drawFurthest(): #draw a line between each agent and the agent furthest away from it
        sortedByDistance = agents.sorted(self.distComp.bind(self))
        furthestAgent = sortedByDistance[sortedByDistance.length - 1]
        line(self.x, self.y, furthestAgent.x, furthestAgent.y)
    
    def drawNearest(): #draw a line between each agent and its nearest agent
        sortedByDistance = agents.sorted(self.distComp.bind(self))
        nearestAgent = sortedByDistance[1]
        line(self.x, self.y, nearestAgent.x, nearestAgent.y)
    
    def drawOverlap(): #draw ellipse between agents when they overlap
        for i in range(0, agents.length):
            otherAgent = agents[i]
            if (self != otherAgent):
                tDist = dist(self.x, self.y, otherAgent.x, otherAgent.y)
                if (tDist < self.radius + otherAgent.radius):
                    cx = (self.x + otherAgent.x) / 2
                    cy = (self.y + otherAgent.y) / 2
            ellipse(cx, cy, tDist)
    
#max number of agents
maxAgents = 32

#array for keeping track of agents
agents = []

#keep track of current mode
AGENT_MODE = 0
POINT_MODE = 1
FURTHEST_MODE = 2
NEAREST_MODE = 3
OVERLAP_MODE = 4

currentMode = None

def setup():
    size(displayWidth, displayHeight)
    #set initial state
    currentMode = AGENT_MODE
    
    #create agents and store them in array
    for i in range(0, maxAgents):
        agents[i].append(Agent())

def draw(): #update agents
    for i in range(0, agents.length):
        agents[i].update()
#depending on the mode:
    if (currentMode == AGENT_MODE):
        background(220, 20, 120)
    
        #draw agents
        noStroke()
        fill(255)
        
        for i in range(0, agents.length):
            agents[i].drawAgent()
    
    else:
        for i in range(0, agents.length):
            agents[i].draw()

def mouseClicked(): #cycle through modes
    currentMode = (currentMode + 1) % 5
    if (currentMode != AGENT_MODE):
        background(255)

def keyReleased():
    #if drawing:
    if (currentMode != AGENT_MODE):
        #s key: save drawing
        if (key == "s" or key == "S"):
            save("my-drawing.jpg")

        #r key: reset
        if (key == "r" or key == "R"):
            background(255)
