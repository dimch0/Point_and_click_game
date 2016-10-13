import pygame,sys
from pygame.locals import *
from functions.functions import *

# LOADING
pygame.init()
gameDisplay = setDisplay(800,600)
# images
lemon_img = imgLoader("lemon.png")
...

# MOUSE POSITION
mouse_pos = pygame.mouse.get_pos()
mx = mouse_pos[0]
my = mouse_pos[1]

# A CLASS FOR THE BUTTONS IN THE TOP MENU
class Button(object):
    def __init__(self, name, pos, point, image, image_1, image_2, available, hovered, active, clicks, description):
        self.name = str(name)
        self.pos = pos
        self.point = point
        self.image = image
        self.image_1 = image_1
        self.image_2 = image_2
        self.available = False
        self.hovered = False
        self.active = False
        self.clicks = int(0)
        self.description = str(description)

    def position(self):
        return mapping(self.pos,self.point)

    def hover(self):
        if mouse_in_poly(self.position()) and self.available:
            gameDisplay.blit(msg_panel,[0,560])
            message(self.description,font_2)
            self.hovered = True
            return True
        if not mouse_in_poly(self.position()):
            #gameDisplay.blit(msg_panel,[0,560])
            self.hovered = False
            return False

    def click(self):
        if self.hovered and self.available:
            print("Button {} clicked!".format(self.name))
            self.clicks += 1
            if self.clicks % 2 != 0:
                self.active = True
            else:
                self.active = False



    # CHANGING BUTTONS

def ChangingButtons(Buttons,event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for button in Buttons:
            for button2 in Buttons:
                if button.hover() and not button == button2:
                    if not button2.hover():
                        button2.active = False
                        button2.clicks = 0

# BUTTONS ROOM_0
Health = Button(
        name = 'Health',
        pos = [0,0,50,0,50,50,0,50],
        point = [10,5],
        image = health_img,
        image_1 = health_img,
        image_2 = health_img,
        available = True,
        hovered = False,
        active = False,
        clicks = 0,
        description = "Your health is")


Explore = Button(
        name = 'Explore',
        pos = [0,0,50,0,50,50,0,50],
        point = [70,5],
        image = explore_image,
        image_1 = explore_image,
        image_2 = explore_image_2,
        available = True,
        hovered = False,
        active = False,
        clicks = 0,
        description = "Explore")
