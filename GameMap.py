import Tileset as ts
import pygame

class eventRect():
    def __init__(self, fileName):
        self.rect = pygame.Rect(0,0,0,0)
        self.triggered = False
        self.fName = fileName
        self.img = pygame.image.load(fileName)

class GameMap():
    def __init__(self,fileName, fileName2, mapNum):

        self.tiles = []
        self.overlay = []
        self.underlay = []
        self.mySet = ts.aTileSet()
        self.gameRect = pygame.Rect(0,0,100,100)
        self.myFile = open(fileName, "r")
        self.myFile2 = open(fileName2, "r")

        self.mapNum = mapNum

        self.upMapRect = pygame.Rect((16*16,10,32,16))

        if mapNum == 2:
            self.upMapRect = pygame.Rect((18*16, 16, 32, 16))
        
        if mapNum == 3:
            self.upMapRect = pygame.Rect((18*16, 0, 64, 16))
        
        self.eventDisplay = False

        self.booksFound = 0
        mapRect1 = eventRect("servant text.png")
        mapRect1.rect = pygame.Rect(10*16,8*16,16,16)

        mapRect2 = eventRect("Barefoot text.png")
        mapRect2.rect = pygame.Rect(368,224,18,18)

        mapRect3 = eventRect("Biography text.png")
        mapRect3.rect = pygame.Rect(21*16,14*16,16,16)

        mapRect4 = eventRect("persepolis text.png")
        mapRect4.rect = pygame.Rect(4*16,22*16,16,16)

        mapRect5 = eventRect("signs text.png")
        mapRect5.rect = pygame.Rect(35*16,22*16,16,16)

        self.eventRects = [mapRect1, mapRect2, mapRect3, mapRect4, mapRect5]
       
        self.currentEvent = mapRect1

        for x in range(40):
            row = []
            theLine = self.myFile.readline().split()
            for y in range(40):
                myChar = theLine[y].strip()
                row.append(self.mySet.tileDict[myChar])
            self.tiles.append(row)

        for x in range(40):
            row = []
            theLine = self.myFile2.readline().split()
            for y in range(40):
                myChar = theLine[y].strip()
                row.append(self.mySet.tileDict[myChar])
            self.overlay.append(row)
        
        for x in range(40):
            row = []
            for y in range(40):
                row.append(self.mySet.tileDict["w1"])
            self.underlay.append(row)


    def draw(self,canvas):
        for x in range (40):
            for y in range(40):
                canvas.blit(self.underlay[y][x].img, (x*16, y*16, 16, 16))
        for x in range (40):
            for y in range(40):
                canvas.blit(self.tiles[y][x].img, (x*16, y*16, 16, 16))
        for x in range (40):
            for y in range(40):
                canvas.blit(self.overlay[y][x].img, (x*16, y*16, 16, 16))
        
        if self.eventDisplay:
            canvas.blit(self.currentEvent.img, (0,440,640,140))

        return canvas
    
    def checkTrigger(self, arr):
        checkRect = pygame.Rect(arr[0], arr[1], 2, 2)

        if self.mapNum == 1:
            if checkRect.colliderect(self.eventRects[0].rect):
                self.eventDisplay = True
                self.currentEvent = self.eventRects[0]
                if not self.eventRects[0].triggered:
                    self.booksFound+=1
                self.eventRects[0].triggered = True

            else:
                self.eventDisplay = False
        if self.mapNum == 2:
            if checkRect.colliderect(self.eventRects[1].rect):
                self.eventDisplay = True
                self.currentEvent = self.eventRects[1]

                if not self.eventRects[1].triggered:
                    self.booksFound+=1
                self.eventRects[1].triggered = True
            elif checkRect.colliderect(self.eventRects[2].rect):
                self.eventDisplay = True
                self.currentEvent = self.eventRects[2]

                if not self.eventRects[2].triggered:
                    self.booksFound+=1
                self.eventRects[2].triggered = True
            else:
                self.eventDisplay = False
        if self.mapNum == 3:
   
            if checkRect.colliderect(self.eventRects[3].rect):
                self.eventDisplay = True
                self.currentEvent = self.eventRects[3]
                if not self.eventRects[3].triggered:
                    self.booksFound+=1
                self.eventRects[3].triggered = True
            elif checkRect.colliderect(self.eventRects[4].rect):
                self.eventDisplay = True
                self.currentEvent = self.eventRects[4]
                if not self.eventRects[4].triggered:
                    self.booksFound+=1
                self.eventRects[4].triggered = True
            else:
                self.eventDisplay = False
    
    def getWalkable(self, arr):
        toReturn = False
        checkX = int(arr[0]/16)
        checkY = int(arr[1]/16)
        toReturn = self.tiles[checkY][checkX].walkable
        if self.overlay[checkY][checkX].walkable!=None:
            toReturn = self.overlay[checkY][checkX].walkable
        return toReturn
    
    def moveUp(self, arr):
        toCheck = pygame.Rect((arr[0], arr[1], 1, 1))
        if toCheck.colliderect(self.upMapRect):
            return True


    
