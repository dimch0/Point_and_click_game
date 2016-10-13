import pygame,sys, random
from pygame.locals import *
from functions.functions import *
from clickables.buttons import *
import copy


# LOADING
pygame.init()
gameDisplay = setDisplay(800,600)
# images
lemon_img = imgLoader("lemon.png")
msg_panel = imgLoader("msg_panel.png")
_drop.png')
Q2 = imgLoader('./Q2.png')

gas_tank_img = imgLoader('./gas_tank.png')
man_asleep = imgLoader('./man_asleep.png')




class LevelObject(object):

    """A class for the obejcts placed on the map"""
    def __init__(self, name, pos, point, image, available, hovered, active, description):
        self.name = str(name)
        self.pos = pos
        self.point = point
        self.image = image
        self.available = True
        self.hovered = False
        self.active = False
        self.description = str(description)
        self.__original_dict__ = self.__dict__.copy()

    def position(self):
        return mapping(self.pos,self.point)

    def reset(self):
        self.__dict__.update(self.__original_dict__)
        self.alive = True

    def hover(self):
        if mouse_in_poly(self.position()):
            self.hovered = True
            return True
        else:
            self.hovered = False
            return False

    def click(self): # TO CALL ONLY IF EVENT == MOUSECLICK
        if self.hover():
            print("Object {} clicked!".format(self.name))
            return True
        else:
            return False

class Creature(LevelObject):

    def __init__(self,alive, health, image_dead, pos_dead, description_dead,**kwargs):
        super().__init__(**kwargs)
        self.alive = True
        self.health = int(health)
        self.image_dead = image_dead
        self.pos_dead = pos_dead
        self.description_dead = str(description_dead)

    def reset(self):
        self.__dict__.update(self.__original_dict__)
        self.alive = True
        self.health = 1

    def explore(self): # TO CALL ONLY IF Button Explore.active == True
        if not self.hover():
            self.active = False
        if self.active and self.alive:
            gameDisplay.blit(msg_panel,[0,560])
            message(self.description,font_2)
            pygame.display.update()
            return True
        if self.active and not self.alive:
            gameDisplay.blit(msg_panel,[0,560])
            message(self.description_dead,font_2)
            pygame.display.update()
            return True

    def dying(self):

        self.alive = False
        self.image = self.image_dead
        self.pos = self.pos_dead
        self.description = self.description_dead
        gameDisplay.blit(Pig.image_dead,Pig.point)




# CREATING OBJECTS

Panel_top = LevelObject(
    name = "Panel_top",
    pos = [0, 100, 0, 0, 800, 0, 800, 100],
    point = [0,0],
    image = None,
    available = True,
    hovered = False,
    active = False,
    description = "Panel")

Pig = Creature(
    name = "Pig",
    pos = [11,54,10,47,12,35,10,30,9,20,12,13,21,8,30,11,45,17,51,17,59,26,63,31,75,29,75,32,68,36,68,37,67,38,66,39,63,42,65,54,62,58,57,57,57,57,54,57,52,55,43,43,44,49,43,50,44,57,46,62,39,60,38,58,38,52,34,41,27,40,24,37,22,40,22,47,25,51,26,53,24,54,20,51,19,52,16,39,14,53],
    image = pig_img,
    point = [69, 372],
    available = True,
    hovered = False,
    active = False,
    description = "It pig.",
    alive = True,
    health = 1,
    image_dead = pig_dead,
    pos_dead = [0,32,18,34,24,30,12,26,12,25,14,23,25,25,29,21,37,20,66,33,75,42,76,52,78,52,78,56,75,56,75,61,70,62,69,64,59,66,59,66,55,68,48,68,45,65,47,62,46,58,45,59,45,58,38,51,11,51,11,47,36,45,26,40,23,40,19,38,16,37,10,37,10,36,0,36,0,33,0,33],
    description_dead = "It pig, but dead."
)


Car = LevelObject(
    name = "Car",
    pos = [61,2,113,2,133,4,142,7,156,30,195,38,196,41,196,57,198,58,198,65,191,66,190,69,187,69,187,74,186,77,182,83,178,85,171,86,168,84,165,81,160,76,160,74,155,73,154,75,126,75,123,83,121,86,117,88,115,89,108,90,104,90,101,83,95,73,97,77,94,78,88,77,85,76,82,73,81,70,68,68,64,70,59,69,57,65,55,68,45,68,43,75,39,79,36,81,30,81,24,75,22,70,16,70,17,62,13,61,9,57,4,56,4,56,3,49,8,48,5,45,5,35,9,30,18,28,28,28,38,8,43,5,49,3],
    point = [20,220],
    image = car_img,
    available = True,
    hovered = False,
    active = False,
    description = "It car, but no gas.")
