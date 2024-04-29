import SpriteSheet
import pygame

class Tile(object):
    def __init__(self, img, walkable):
        self.img = img
        self.img.set_colorkey((0,0,0))
        self.walkable = walkable


class aTileSet(object):
    def __init__(self):
        self.tileDict = {}
        self.grass = SpriteSheet.spritesheet("Grass.png")
        self.tileDict["0"] = Tile(self.grass.image_at((0,0,16,16)), True)
        self.tileDict["1"] = Tile(self.grass.image_at((16,0,16,16)), True)
        self.tileDict["2"] = Tile(self.grass.image_at((32,0,16,16)), True)

        self.tileDict["3"] = Tile(self.grass.image_at((0,16,16,16)), True)
        self.tileDict["4"] = Tile(self.grass.image_at((16,16,16,16)), True)
        self.tileDict["5"] = Tile(self.grass.image_at((32,16,16,16)), True)

        self.tileDict["6"] = Tile(self.grass.image_at((0,32,16,16)), True)
        self.tileDict["7"] = Tile(self.grass.image_at((16,32,16,16)), True)
        self.tileDict["8"] = Tile(self.grass.image_at((32,32,16,16)), True)
       
        self.tileDict["b"] = Tile(self.grass.image_at((0,0,1,1)), None)

        self.dirt = SpriteSheet.spritesheet("Tilled_Dirt.png")
        self.tileDict["d1"] = Tile(self.dirt.image_at((0,16*5,16,16)), True)

        self.water = SpriteSheet.spritesheet("Water.png")
        self.tileDict["w1"] = Tile(self.water.image_at((0,0,16,16)), False)
        self.tileDict["w"] = Tile(self.water.image_at((0,0,16,16)), False)

        self.chest = SpriteSheet.spritesheet("Chest.png")
        self.tileDict["c"] = Tile(self.chest.image_at((16,16,16,16)), False)

        self.fences = SpriteSheet.spritesheet("Fences.png")
        self.tileDict["f1"] = Tile(self.fences.image_at((0,16,16,16)), False)
        self.tileDict["f2"] = Tile(self.fences.image_at((0,16,16,16)), False)
        self.tileDict["f3"] = Tile(self.fences.image_at((0,16,16,16)), False)

        self.tileDict["f4"] = Tile(self.fences.image_at((16,48,16,16)), False)
        self.tileDict["f5"] = Tile(self.fences.image_at((32,48,16,16)), False)
        self.tileDict["f6"] = Tile(self.fences.image_at((48,48,16,16)), False)

        self.bridge = SpriteSheet.spritesheet("Wood_Bridge.png")
        self.tileDict["b1"] = Tile(self.bridge.image_at((0,0,16,16)), True)
        self.tileDict["b2"] = Tile(self.bridge.image_at((0,16,16,16)), True)
        self.tileDict["b3"] = Tile(self.bridge.image_at((0,32,16,16)), True)

        self.tileDict["s1"] = Tile(self.bridge.image_at((32,0,16,16)), True)
        self.tileDict["s2"] = Tile(self.bridge.image_at((48,0,16,16)), True)
        self.tileDict["s3"] = Tile(self.bridge.image_at((64,0,16,16)), True)

        self.trees = SpriteSheet.spritesheet("Basic_Grass_Biom_things.jpg")
        self.tileDict["t1"] = Tile(self.trees.image_at((16,0,16,16)), False)
        self.tileDict["t2"] = Tile(self.trees.image_at((32,0,16,16)), False)
        self.tileDict["t3"] = Tile(self.trees.image_at((16,16,16,16)), False)
        self.tileDict["t4"] = Tile(self.trees.image_at((32,16,16,16)), False)

        self.tileDict["a1"] = Tile(self.trees.image_at((16+32,0,16,16)), False)
        self.tileDict["a2"] = Tile(self.trees.image_at((32+32,0,16,16)), False)
        self.tileDict["a3"] = Tile(self.trees.image_at((16+32,16,16,16)), False)
        self.tileDict["a4"] = Tile(self.trees.image_at((32+32,16,16,16)), False)

        self.tileDict["d1"] = Tile(self.trees.image_at((8*16, 2*16, 16, 16)), False)
        self.tileDict["d2"] = Tile(self.trees.image_at((8*16, 3*16, 16, 16)), False)
        self.tileDict["y1"] = Tile(self.trees.image_at((7*16, 2*16, 16, 16)), False)
        self.tileDict["o1"] = Tile(self.trees.image_at((7*16, 3*16, 16, 16)), False)

        #sprouts
        self.tileDict["p1"] = Tile(self.trees.image_at((5*16, 1*16, 16, 16)), True)
        self.tileDict["p2"] = Tile(self.trees.image_at((6*16, 1*16, 16, 16)), True)

        #stump
        self.tileDict["z"] = Tile(self.trees.image_at((4*16, 2*16, 16, 16)), False)
        #self.tileDict["p2"] = Tile(self.trees.image_at((6*16, 1*16, 16, 16)), True)

        #rocks
        self.tileDict["r"] = Tile(self.trees.image_at((8*16, 1*16, 16, 16)), False)

        #lily pads
        self.tileDict["l1"] = Tile(self.trees.image_at((7*16, 4*16, 16, 16)), True)
        self.tileDict["l2"] = Tile(self.trees.image_at((8*16, 4*16, 16, 16)), True)

        #bushes
        self.tileDict["g1"] = Tile(self.trees.image_at((0,48,16,16)), False)
        self.tileDict["g2"] = Tile(self.trees.image_at((16,48,16,16)), False)

        self.cows = SpriteSheet.spritesheet("Free Cow Sprites.png")
        self.tileDict["cw"] = Tile(self.cows.image_at((0,0,16,16)), False)
        self.tileDict["cx"] = Tile(self.cows.image_at((16,0,16,16)), False)
        self.tileDict["cy"] = Tile(self.cows.image_at((0,16,16,16)), False)
        self.tileDict["cz"] = Tile(self.cows.image_at((16,16,16,16)), False)
