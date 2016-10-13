import pygame, random
from pygame.locals import *
from functions.functions import *
from clickables.buttons import *
from clickables.objects import *

# LOADING
pygame.init()
pygame.display.set_caption('Game')
gameDisplay = setDisplay(800,600)
FPS = 300
clock = pygame.time.Clock()

# COLOURS
white = (255,255,255)
purp = (170,167,194)



# IMAGES
pointer_img = imgLoader('./cursor.png')

room_0_img = imgLoader("room_0_img.png")
room_1_img = imgLoader('./room_1_img.png')
room_2_img = imgLoader('./room_2_img.png')


# ALL BUTTONS AND OBJECTS
ALL_Objects = [Car,
               Lake,
               Cave,
               CaveEntrance,
               Stake,
               BasaltEgg_1,
               Pig,
               Lemon_small_1,
               Lemon_small_2,
               Lemon_small_3,
               Trilobite,
               MagnetSmall,
               QuestionWindow,
               Yos_btn,
               No_btn,
               Gas_tank,
               BigMan,
               LordOfFlies
               ]
ALL_Buttons = [Explore,
               Communicate,
               Hit,
               Lemon,
               Knife,
               Pork,
               PigHead,
               GasTank,
               Magnet]




# FUNCTION FOR COUNTING BUTTON STATS
def stats(button,counter,sx,sy):
     if button.available and counter:
        gameDisplay.blit(button.image,button.point)
        message("{}".format(counter),font_0,sx,sy)
        if button == Health:
            if button.hover():
                message("{}.".format(counter),font_2,225)
                
                
# FUNCTION FOR GAMEOVER SCREEN
def GameOver(play_game,game_over):
    pygame.mouse.set_visible(True)
    game_over = True

    if game_over:
        gameDisplay.fill(purp)
        gameDisplay.blit(dialog_btn_1,[225,300])
        gameDisplay.blit(dialog_btn_1,[425,300])
        if Car.available:
            message("You dead.",font_3,310,200)
        elif not Car.available:
            message("You win.", font_3, 320, 200)
        message("Reborn",font_2,250,312)
        message("Quit",font_2,468,312)
        pygame.display.update()
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
                pygame.quit()
                quit()

            if event.type == MOUSEBUTTONDOWN:
                # QUIT
                if mouse_in_poly(mapping([448,301,561,301,572,305,579,313,583,324,583,332,579,343,571,351,561,355,449,355,439,351,431,343,427,333,426,325,430,313,438,306,447,302,447,302])):
                    play_game = False
                    pygame.quit()
                    quit()
                # REBORN
                if mouse_in_poly(mapping([248,301,361,301,371,305,378,313,383,324,383,332,379,343,371,351,360,355,249,355,238,351,230,343,226,333,226,325,230,313,238,306,246,302,247,302])):
                    print("REBORN")
                    for object in ALL_Objects:
                        object.reset()
                    for button in ALL_Buttons:
                        button.active = False
                        button.clicks = 0
                    GameLoop()
                    play_game = False
                    game_over = False
                    
                    
# FUNCTION FOR GENERATING RANDOM POSITION OF BLOOD DROPS
def Blood_drops_generating(blood_pool,blood_point,number_of_drops):
    for x in range(number_of_drops):
        blood_pool.append([round(random.randint(blood_point[0],blood_point[0]+40)), round(random.randint(blood_point[1]+40,blood_point[1]+80))])


# FUNCTION FOR GETTING THE DROPS ON THE SCREEN
def bleeding_blit(blood_pool,number_of_drops):
    for x in range(number_of_drops):
        gameDisplay.blit(blood_drop,blood_pool[x])


# FUNCTION FOR TEMPORARY MESSAGE ON THE SCREEN
def tempMsg(temp_msg, time_to_show = 3000):
    return [temp_msg, pygame.time.get_ticks() + time_to_show]


# FUNCTION FOR DISPLAYING THE AVAILABLE BUTTONS AND DESCRIPTION
def available_buttons(current_buttons):
    for button in current_buttons:
        button.available = True
        if button.available and button.image:
            gameDisplay.blit(button.image,button.point)
            button.hover()


# FUNCTION FOR MOVING AN OBJECT TO A DESTINATION (SPECIFIC POINT)
def Move(object,destination):
    track = Tracks(object.point,list(destination))
    step = 1
    while track:
        gameDisplay.blit(object.image, object.point)
        object.point = track[step]
        step += 1
        if object.point == track[-1]:
            track = []
            step = 1
            clock.tick(300)
        pygame.display.update()
        clock.tick(100)




# GAME LOOP
def GameLoop():

    pygame.mouse.set_visible(False)
    cursor_img = pointer_img

    play_game = True
    game_over = False
    temp_msg = None
    blood_pool = []
    room = 0
    health = 6
    info = 1
    lemon_stash = 0
    fuel = 0


    # ASSIGNING RANDOM POINTS FOR EGGS AND FRUITS + TRILO
    eggs = [(219, 103),(244, 103),(269, 103),(231, 135),(257, 136),(243, 167),(270, 170),(283, 134),(295, 103),(772, 323),(773, 361),(772, 399),(748, 341),(749, 381),(434, 487),(451, 480),(660, 314),(672, 328),(110, 112),(101, 132),(78, 145),(92, 169),(426, 509),(449, 514),(471, 499)]
    for non_egg in range(5):
        random_index = random.randint(0, len(eggs) - 1)
        if non_egg < 3:
            eval('Lemon_small_' + str(non_egg + 1)).point = eggs[random_index]
        elif non_egg < 4:
            Trilobite.point = eggs[random_index]
        else:
            MagnetSmall.point = eggs[random_index]
        eggs.pop(random_index)
    for removing_egg in range(15):
        eggs.pop(random.randint(0, len(eggs) - 1))




    # ROOM 0
    room_0_objects = [Car,
                      Pig,
                      Lake,
                      Cave,
                      CaveEntrance,
                      Trilobite,
                      Lemon_small_1,
                      Lemon_small_2,
                      Lemon_small_3,
                      MagnetSmall
                      ]
    room_0_buttons = [Health,
                      Explore,
                      Communicate
                      ]


    # ROOM 1
    room_1_objects = []
    room_1_buttons = [Health,
                      Stay_btn,
                      Go_btn
                      ]


    # ROOM 2
    room_2_objects = [Gas_tank,
                      BigMan,
                      CaveExit,
                      Stake,
                      Gas_tank,
                      BigMan
                      ]
    room_2_buttons = room_0_buttons


    while play_game:


        # LOADING ROOM STUFF
        Current_room = eval('room_' + str(room) + '_img')
        Current_Objects = eval('room_' + str(room) + '_objects')
        Current_Buttons = eval('room_' + str(room) + '_buttons')
        Current_stuff = Current_Objects + Current_Buttons
        hovered_objects = []

        # MOUSE POSITION X AND Y
        mouse_pos = pygame.mouse.get_pos()
        mx = mouse_pos[0]
        my = mouse_pos[1]

        # GAME OVER
        if health < 1:
            GameOver(play_game,game_over)

        for event in pygame.event.get():

            # QUIT EVENTS
            if event.type == pygame.QUIT:
                play_game = False
                pygame.quit()
                quit()


            # FOR MONITORING ONLY
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click!", mouse_pos)

                #Blood_drops_generating(blood_pool,mouse_pos,30)
                print(blood_pool)

                for object in Current_Objects:
                    object.hover()
                    hovered_objects.append(object.hovered)

                for button in Current_Buttons:
                    if button != Health:
                        button.click()

                # NO-ACTION-MESSAGE FOR EACH BUTTON
                if not point_inside_polygon((mx, my), [(0, 100), (0, 0), (800, 0), (800, 100)]):
                    # no action Communicate
                    if Communicate.active and not ((Pig.click() and Pig.alive) or (Trilobite.click() and Trilobite.image == trilo_small) or (BigMan.click() and BigMan.alive)):
                        temp_msg = tempMsg("You shout, but not answer.",1000)
                    # no action Knife
                    if Knife.active and not ((Pig.click() and Pig in Current_Objects) or (BigMan.click() and BigMan.alive)):
                        temp_msg = tempMsg("You stab air.",1000)


                if GasTank.active and Car.click():
                    Move(Car,[810,525])
                    Car.available = False
                    temp_msg = tempMsg("Car go.")
                    GameOver(play_game,game_over)


                # PIG ACTIONS
                if Pig.click():
                    if Communicate.active and Pig.alive:
                        Move(Pig,randomPoint())
                        temp_msg = tempMsg("Pig scare. It run.")
                    elif Knife.active:
                        Pig.health -= 1
                        if not Pig.health:
                            Pig.dying()
                            temp_msg = tempMsg("You kill pig.")
                            Blood_drops_generating(blood_pool,Pig.point,50)
                        elif Pig.health < 0 and Pig in Current_Objects:
                            temp_msg = tempMsg("You cut pig head.", 2000)

                if BigMan.click() and room == 2:

                    if Communicate.active and BigMan.alive and LordOfFlies.active:
                        BigMan.image = man_pray
                        BigMan.pos = man_angry_pos
                        Move(BigMan, [303,203])
                        temp_msg = tempMsg("Big man hypnotized.")

                    elif Communicate.active and BigMan.alive and info < 6:
                        BigMan.image = man_angry
                        BigMan.pos = man_angry_pos
                        Move(BigMan, [390,300])
                        temp_msg = tempMsg("Big man no understand, but angry.")
                        BigMan.description = "Hypnotized."
                        health -= 1

                    elif Communicate.active and BigMan.alive and info > 5:
                        BigMan.image = man_trade
                        BigMan.pos = man_trade_pos
                        Move(BigMan, [390, 300])
                        temp_msg = tempMsg("You speak big man. Trade for gas.")
                        BigMan.description = "Man hungry. Want meat."

                    elif Communicate.active and BigMan.alive and info < 6:
                        BigMan.image = man_angry
                        BigMan.pos = man_angry_pos
                        Move(BigMan, [390,300])
                        temp_msg = tempMsg("Big man no understand, but angry.")
                        BigMan.description = "He fight you."
                        health -= 1

                    elif Knife.active and BigMan.alive:
                        BigMan.health -= 1
                        health -= 2
                        BigMan.pos = man_angry_pos
                        BigMan.image = man_angry
                        Move(BigMan, [390,300])
                        temp_msg = tempMsg("You stab big man. He fight strong.")
                        BigMan.description = "He fight you."
                        if not BigMan.health:
                            BigMan.dying()
                            temp_msg = tempMsg("You kill man.")


                # CUTTING PIG ACTION
                if Pig.health < 0:
                    if not Pork in room_0_buttons and not GasTank in room_0_buttons:
                        room_0_buttons.append(Pork)
                    if not PigHead in room_0_buttons and not LordOfFlies.active:
                        room_0_buttons.append(PigHead)
                    if Pig in room_0_objects:
                        room_0_objects.remove(Pig)
                        Pig.available = False

                # TRILO ACTION ON MOUSE CLICK
                if Trilobite.click() and Communicate.active:
                    Trilobite.active = True

                # LEMON ACTION ON MOUSE CLICK
                if health < 6 and Lemon.active and Health.hover():
                    health += 1
                    lemon_stash -= 1

                # MAGNET LAKE ACTION
                if Magnet.active and Lake.click():
                    if not Knife in room_0_buttons:
                        room_0_buttons.append(Knife)
                        temp_msg = tempMsg("You find knife.", 3000)

            # AVAILABLE STUFF FOR THE CURRENT ROOM
            gameDisplay.blit(Current_room,[0,0])
            available_buttons(Current_stuff)
            stats(Health,health,30,22)
            stats(Lemon,lemon_stash,364,32)
            #stats(GasTank,fuel,765,40)
            ChangingButtons(Current_Buttons,event)

            # TEMP MESSAGE BLIT
            if temp_msg:
                gameDisplay.blit(msg_panel,[0,560])
                message(temp_msg[0])
                if pygame.time.get_ticks() >= temp_msg[1]:
                    temp_msg = None

            # BLEEDING and EGGING for ROOM 0
            if room == 0:
                if not Pig.alive:
                    bleeding_blit(blood_pool,50)
                for egg in eggs:
                    gameDisplay.blit(basalt_egg_img,egg)


            if PigHead.active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Stake.click():
                        room_2_objects.append(LordOfFlies)
                        LordOfFlies.active = True
                        temp_msg = tempMsg("Gift for big man.")
                        room_0_buttons.remove(PigHead)
                        PigHead.active = False

            if Pork.active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BigMan.click() and BigMan.image == man_trade:
                        fuel += 1
                        if Pork in room_0_buttons:
                            room_0_buttons.remove(Pork)
                        if Gas_tank in room_2_objects:
                            room_2_objects.remove(Gas_tank)


            # EXPLORE BUTTON ACTIONS:
            if Explore.active and not Panel_top.hover():
                if event.type == pygame.MOUSEBUTTONDOWN:


                    for object in Current_Objects:

                        if not any(hovered_objects):
                            for egg in eggs:
                                BasaltEgg_1.point = egg
                                if BasaltEgg_1.hover():
                                    temp_msg = tempMsg("Stone egg.", 2000)
                                else:
                                    temp_msg = tempMsg("You only see air.", 1000)

                        else:
                            if object.click():
                                temp_msg = tempMsg(object.description, 2000)
                                if object == Gas_tank and (not BigMan.alive or BigMan.image == man_pray):
                                    fuel += 1
                                    room_2_objects.remove(Gas_tank)
                                elif object in [CaveEntrance,CaveExit]:
                                    QuestionWindow.active = True
                                    QuestionWindow.point = [mouse_pos[0] - 75, mouse_pos[1]]
                                    Yos_btn.point = [mouse_pos[0] - 56, mouse_pos[1] + 45]
                                    No_btn.point = [mouse_pos[0] + 4, mouse_pos[1] + 45]
                                    Current_Objects.append(QuestionWindow)
                                    Current_Objects.append(Yos_btn)
                                    Current_Objects.append(No_btn)
                                elif object == Trilobite:
                                    object.image = trilo_small
                                elif object == MagnetSmall:
                                    object.image = magnet_small_img
                                    object.health -= 1
                                    if object.health < 0:
                                        room_0_buttons.append(Magnet)
                                        room_0_objects.remove(object)
                                        object.available = False
                                elif object in [Lemon_small_1,Lemon_small_2,Lemon_small_3]:
                                    object.image = lemon_small
                                    object.health -= 1
                                    if object.health < 0:
                                        lemon_stash += 1
                                        room_0_objects.remove(object)
                                        object.available = False

            # ROOM 1 TRILOBITE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Communicate.active and Trilobite.active and Trilobite.click() and Trilobite.image == trilo_small:
                    room = 1
                    Communicate.active = False
                    Communicate.clicks = 0
            if room == 1:
                message("Stay", font_2, 373, 424)
                message("Go", font_2, 505, 424)
                TrilobiteDialog(info)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Stay_btn.click():
                        health -= 1
                        if info < 6:
                            info += 1
                    elif Go_btn.click():
                        Trilobite.active = False
                        room = 0

            # QUESTION WINDOW
            if QuestionWindow.active:
                if CaveEntrance in Current_Objects:
                    Current_Objects.remove(CaveEntrance)
                if CaveExit in Current_Objects:
                    Current_Objects.remove(CaveExit)
                if room == 0:
                    message("Explore cave?", font_0, QuestionWindow.point[0] + 20, QuestionWindow.point[1] + 22)
                if room == 2:
                    message("Exit cave?", font_0, QuestionWindow.point[0] + 28, QuestionWindow.point[1] + 22)
                message("Yos", font_0, Yos_btn.point[0] + 11, Yos_btn.point[1] + 6)
                message("No", font_0, No_btn.point[0] + 15, No_btn.point[1] + 6)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Yos_btn.click() or No_btn.click():
                        Current_Objects.remove(Yos_btn)
                        Current_Objects.remove(No_btn)
                        Current_Objects.remove(QuestionWindow)
                        QuestionWindow.active = False
                        if CaveEntrance not in Current_Objects and room == 0:
                            Current_Objects.append(CaveEntrance)
                        if CaveExit not in Current_Objects and room == 2:
                            Current_Objects.append(CaveExit)

                    if Yos_btn.click():
                        if room == 0:
                            room = 2
                            if BigMan.alive:
                                BigMan.pos = [96,12,108,24,117,25,126,36,128,51,117,61,113,61,117,70,115,102,115,115,104,119,98,111,97,107,89,108,88,106,91,99,92,92,83,105,71,117,79,117,81,120,80,128,79,131,61,133,52,131,52,129,52,122,55,114,52,107,56,94,57,91,47,96,41,96,27,94,20,89,16,85,12,78,11,70,12,60,15,51,19,42,27,34,38,28,47,22,60,17,82,13]
                                BigMan.image = man_asleep
                                BigMan.description = "Big man. He sleep."
                                BigMan.point = [528,201]

                        elif room == 2:
                            room = 0

        bleeding_blit(blood_pool, len(blood_pool))

        # BUTTON MOUSE IMAGE:
        active_buttons_count = 0
        for button in Current_Buttons:
            if button.active:
                active_buttons_count += 1
                if active_buttons_count > 0:
                    cursor_img = button.image_1
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        cursor_img = button.image_2
                    elif event.type == pygame.MOUSEBUTTONUP:
                        cursor_img = button.image_1
        if active_buttons_count < 1:
            cursor_img = pointer_img
        gameDisplay.blit(cursor_img, [mx - 25, my - 25])
        gameDisplay.blit(pointer_img, [mx - 25, my - 25])



        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()


GameLoop()
