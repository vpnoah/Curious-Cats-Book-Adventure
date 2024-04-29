
import pygame
import Character
import GameMap

pygame.init() 
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((640, 640))

theGuy = Character.character()

booksFound = 0
mapNum = 1

# TITLE OF CANVAS 
pygame.display.set_caption("My Board") 
exit = False

left = False
right = False
up = False
down = False

m1 = GameMap.GameMap("maps/map1.txt", "maps/overlay1.txt", 1)
m2 = GameMap.GameMap("maps/map2.txt", "maps/overlay2.txt", 2)
m3 = GameMap.GameMap("maps/map3.txt", "maps/overlay3.txt", 3)
m4 = GameMap.GameMap("maps/map4.txt", "maps/overlay4.txt", 4)

currentMap = m1

def changeMap():
    global currentMap
    global mapNum
    global booksFound
    global m2
    global m1
    global m3
    global m4
    global exit
    if mapNum ==1:
        booksFound += currentMap.booksFound
        mapNum = 2
        currentMap = m2
        theGuy.y = 600
        theGuy.setImg(1)
    elif mapNum ==2:
        booksFound += currentMap.booksFound
        mapNum = 3
        currentMap = m3
        theGuy.y = 600
        theGuy.setImg(1)
    elif mapNum == 3:
        exit = True

def movement():
    if up:
        currentMap.checkTrigger(theGuy.upRect)
     
        if currentMap.getWalkable(theGuy.upRect):
            theGuy.y-=0.1
            theGuy.setImg(2)
  
    if down:
        currentMap.checkTrigger(theGuy.downRect)
        if currentMap.getWalkable(theGuy.downRect):
            theGuy.y+=0.1
            theGuy.setImg(1)
 
    if left:
        currentMap.checkTrigger(theGuy.leftRect)
        if currentMap.getWalkable(theGuy.leftRect):
            theGuy.x-=0.1
            theGuy.setImg(3)
  
    if right:
        currentMap.checkTrigger(theGuy.rightRect)
        if currentMap.getWalkable(theGuy.rightRect):
            theGuy.x+=0.1
            theGuy.setImg(4)

    
    if currentMap.moveUp(theGuy.upRect):
        changeMap()

titleScreen = pygame.image.load("Title Screen.png")
starterScreen = False

while not starterScreen:
    canvas.blit(titleScreen, (0,0,640,640))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            starterScreen = True
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()

firstScreen = pygame.image.load("First Screen.jpg")
starterScreen = False

while not starterScreen:
    canvas.blit(firstScreen, (0,0,640,640))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            starterScreen = True
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()

while not exit:
    currentMap.draw(canvas)
    canvas.blit(theGuy.img, (theGuy.x,theGuy.y,100,100))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            theGuy.x = pygame.mouse.get_pos()[0]
            theGuy.y = pygame.mouse.get_pos()[1]
            theGuy.setImg(1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_a:
                print(str(theGuy.x) + " " + str(theGuy.y))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
        if event.type == pygame.QUIT: 
            exit = True
    movement()
    pygame.display.update()

finalScreen = pygame.image.load("Final Screen.jpg")

ending = False

while not ending:
    canvas.blit(finalScreen, (0,0,640,640))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ending = True
    pygame.display.update()


pygame.quit() 
