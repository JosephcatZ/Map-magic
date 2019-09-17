def newCont(StartingX,StartingY,Xspan,Yspan,Xsize,Ysize,Layers):
    x = []
    op=["Circle","Square"]
    for i in range(Layers):
        x.append([random(StartingX,StartingX+Xspan),random(StartingY,StartingY+Yspan),random(Xsize),random(Ysize),op[int(random(len(op)))]])
    conts.append(x)
global xp
xp = 0
global yp
yp=0
global conts
conts=[]
def drawCont(cont):
    for i in cont:
        if i[0]>=xp-width-width and i[2]<=xp+width+width and i[1] >= yp-height-height and i[3] <= yp + height + height:
            if i[4] == "Circle":
                ellipse(i[0]+xp,i[1]+yp,i[2],i[3])
            if i[4] == "Square":
                rect(i[0]+xp,i[1]+yp,i[2],i[3])
    endShape(CLOSE)
def setup():
    this.surface.setResizable(True)
    load()
    global conts
    newCont(0,0,100,100,50,50,500)
def load():
    for i in range(200):
        newCont(random(-5000,5000),random(-5000,5000),random(100,500),random(100,500),110,110,500)
def draw():
    background(0,0,255)
    stroke(0,255,0)
    fill(0,255,0)
    global conts
    for j in conts:
        drawCont(j)
    
def mouseDragged():
    global xp
    global yp
    print(xp-(pmouseX-mouseX))
    xp = xp- (pmouseX-mouseX)
    yp = yp- (pmouseY-mouseY)
def keyPressed():
    global xp
    global yp
    global conts
    if key == "r" or key =="R":
        conts=[]
        load()
        xp=0
        yp=0
    elif key == "c" or key == "C":
        conts=[]
    elif key == 'l' or key == 'L':
        load()
    else:
        xp=0
        yp=0
        
    
