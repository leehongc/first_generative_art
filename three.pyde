totalDegrees = 365
radius = 0

def setup():
    global radius
    size(800, 600)
    background(0)
    noFill()
    stroke(255, 25)
    radius = height/2

    
def draw():
    xCenter = width/2
    yCenter = height/2
    global totalDegrees, radius
    translate(frameCount-width/3, 0)
    
    beginShape()
    for i in range(totalDegrees):
        noiseFactor = noise(i * 0.015, float(frameCount)/150)
        # output of noise is between 0-1
        x = xCenter + radius * cos(radians(i)) * noiseFactor
        y = yCenter + radius * sin(radians(i)) * noiseFactor
        curveVertex(x,y)
    endShape(CLOSE)
    
    radius -=1
    # if frameCount == 600:
    #      noLoop()
