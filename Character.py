import SpriteSheet
import pygame

class character(object):
    def __init__(self):
        self.x = 320
        self.y = 560
        self.ss = SpriteSheet.spritesheet("Basic Charakter Spritesheet.png") 
        self.imgDown = self.ss.image_at((16,16,16,16))
        self.imgUp = self.ss.image_at((16,64,16,16))
        self.imgLeft = self.ss.image_at((16,112,16,16))
        self.imgRight = self.ss.image_at((16,160,16,16))
        self.img = self.imgDown
        self.img.set_colorkey((0,0,0))
        self.myRect = pygame.Rect(self.x,self.y,16,16)
        self.upRect = (self.x+8, self.y-1)
        self.downRect = (self.x+8, self.y+17)
        self.leftRect = (self.x-1, self.y+8)
        self.rightRect = (self.x+17, self.y+8)

    
    def setImg(self, dir):
        self.myRect = pygame.Rect(self.x,self.y,16,16)
        self.upRect = (self.x+8, self.y-1)
        self.downRect = (self.x+8, self.y+17)
        self.leftRect = (self.x-1, self.y+8)
        self.rightRect = (self.x+17, self.y+8)
        if dir==1:
            self.img = self.imgDown
        if dir==2:
            self.img = self.imgUp
        if dir==3:
            self.img = self.imgLeft
        if dir==4:
            self.img = self.imgRight
        self.img.set_colorkey((0,0,0))
    

