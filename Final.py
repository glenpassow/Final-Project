from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from random import randrange
black = Color(0x000000, 1.0)
blue = Color(0x2D9FC2,1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xFC5D5D,1.0)
thinline = LineStyle(1, black)
celld = 35
rectangle3 = RectangleAsset(celld, celld, thinline, red)
rectangle = RectangleAsset(celld, celld, thinline, blue)
rectangle2 = RectangleAsset(celld, celld, thinline, white)
rectangle4 = RectangleAsset(celld, celld, thinline, black)
ocean = {}
oceanself = {}
enemyBoats = {}
selfBoats = {} 
enemyboatsalive = {}
length = 5
height = 10
width = 10

class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.visible = True
        
class enemyships(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.visible = False


for x in range(0, height):
    for y in range(0, width):
        #screen one set up
        Sprite(rectangle2, (x*celld, y*celld))
        enemyBoats[(x,y)] = enemyships(rectangle3, (x*celld, y*celld))
        ocean[(x,y)] = cell(rectangle, (x*celld, y*celld))
        #screen two set up
        yshift = height*celld + 20
        Sprite(rectangle2, (x*celld, y*celld + yshift))
        oceanself[(x,y)] = cell(rectangle, (x*celld, y*celld + yshift))
        #selfBoats[(x,y)] = cell(rectangle3, (x*celld, y*celld + yshift))

for a in range(0, 3):
    randx = randrange(1, 10)
    randy = randrange(1, 10)
    if randx > 5:
        nsx = -1
    else:
        nsx = 1
    if randy > 5:
        nsy = -1
    else:
        nsy = 1    
    randxy = randrange(1, 3)
    for u in range(0, length-1):
        enemyBoats[(randx+nsx,randy+nsy)].visible = True
        enemyboatsalive[(randx+nsx,randy+nsy)] = (randx+nsx,randy+nsy)
        if randxy == 2:
            randx = randx + 1
        else:
            randy = randy + 1
    length = length - 1

class Battleship(App):
    
    def __init__(self):
        #Battleship.listenKeyEvent("keydown", "space", self.spaceclick)
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 1000
        self.going = False
        self.squarehit = 0
        self.nonalcoholicshotstaken = 0
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        Battleship.listenMouseEvent("click",self.breathlife)
    
    def breathlife(self, event):
        self.cx = int(event.x/celld)
        self.cy = int(event.y/celld)
        ocean[(self.cx, self.cy)].visible = False
        #selfboats[(self.cx,self.cy)].visible = False
        if (self.cx, self.cy) in enemyboatsalive:
            self.squarehit = self.squarehit + 1
        self.nonalcoholicshotstaken = self.nonalcoholicshotstaken + 1
        print(self.nonalcoholicshotstaken)
    
    def step(self):
        if self.squarehit == 9:
            print("you win")
            for j in range(0, height):
                for k in range(0, width):
                    ocean[(j,k)].visible = False
        
myapp = Battleship()
myapp.run()

"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)
orange = Color(0xFF8400,1.0)
thinline = LineStyle(1, black)
a = 0
b = 0
height = 20
width = 20
ocean = {}
thinline = LineStyle(1, black)
rectangle = RectangleAsset(20, 20, thinline, green)
rectangle2 = RectangleAsset(20, 20, thinline, orange)

class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.visible = False
        self.sca = 0

for x in range(0, height):
            for y in range(0, width):
                Sprite(rectangle2, (x*height, y*width))
                ocean[(x,y)] = cell(rectangle, (x*height, y*width))
          
class ConwayGame(App):
    
    def __init__(self):
        ConwayGame.listenKeyEvent("keydown", "space", self.spaceclick)
        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 480
        self.going = False
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        ConwayGame.listenMouseEvent("click",self.breathlife)
   
    def breathlife(self, event):
        self.cx = int(event.x/20)
        self.cy = int(event.y/20)
        ocean[(self.cx, self.cy)].visible = not ocean[(self.cx, self.cy)].visible
    
    def spaceclick(self,event):
        self.going = not self.going

    def step(self):
        if self.going == True:
            for g in range(0, height):
                for f in range(0, width):
                    if ocean[(g,f)].visible == True:
                                ocean[(g,f)].sca = ocean[(g,f)].sca - 1
                    for w in range(-1, 2):
                        for h in range(-1, 2):
                            if (w+g, h+f) in ocean and ocean[(w+g, h+f)].visible == True:
                                ocean[(g,f)].sca = ocean[(g,f)].sca + 1
            
            for s in range(0, height):
                for d in range(0, width):
                    if ocean[(s, d)].visible == True and ocean[(s, d)].sca < 2:
                        ocean[(s, d)].visible = False
                    elif ocean[(s, d)].visible == True and ocean[(s, d)].sca > 3:
                        ocean[(s, d)].visible = False
                    elif ocean[(s, d)].visible == False and ocean[(s, d)].sca == 3:
                        ocean[(s, d)].visible = True
                    ocean[(s,d)].sca = 0
myapp = ConwayGame()
myapp.run()
"""