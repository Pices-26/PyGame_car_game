import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

pause = False

black = (0,0,0)
white = (200,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

block_colour = (53,115,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Wrum')
clock = pygame.time.Clock()
carImg = pygame.image.load('lambo.png')
expl = pygame.image.load('flame.png')
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("dodged: " + str(count), True, red)
    gameDisplay.blit(text, (0,0))

def quitgame():
    pygame.quit()
    quit()

def things_to_avoid(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])



def message_display(text):
    LargeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, LargeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def crash():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # displaying start window
        gameDisplay.blit(expl, (0,300))
        LargeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects('You Crashed', LargeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        # drawing boxes
        pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        # displaying text
        button('Play Again', 150, 450, 150, 50, green, bright_green, game_loop)
        button('QUIT', 550, 450, 100, 50, red, bright_red, quitgame)

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(15)

def unpause():
    global pause
    pause = False

def paused():
    LargeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects('Paused', LargeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                # drawing boxes
        pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        # displaying text
        button('Continue', 150, 450, 150, 50, green, bright_green, unpause)
        button('QUIT', 550, 450, 100, 50, red, bright_red, quitgame)


''' displaying the car '''
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def intro_window():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #displaying start window
        gameDisplay.fill(black)
        LargeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects('wrum', LargeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        #drawing boxes
        pygame.draw.rect(gameDisplay, green, (150,450,100,50))
        pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        #displaying text
        button('GO', 150, 450,100, 50, green, bright_green, game_loop)
        button('QUIT', 550, 450, 100, 50, red, bright_red, quitgame)







def game_loop():
    global pause
    car_width = 100
    x = (display_width * .45)
    y = (display_height * 0.8)
    dodged = 0
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    ''' main event'''
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x+= x_change

        ''' displaying'''
        gameDisplay.fill(black)
        car(x,y)

        things_dodged(dodged)

        # things_to_avoid(thingx, thingy, thingw, thingh, color):
        things_to_avoid(thing_startx, thing_starty, thing_width, thing_height, block_colour)
        thing_starty += thing_speed
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0 , display_width)
            dodged += 1
            thing_speed += 0.25
            thing_width += 0.01


        if y < thing_starty+thing_height:

            if x > thing_startx and x <thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx + thing_width:
                print('x crossover')
                crash()


        pygame.display.update()
        clock.tick(60)
''' calling functions'''

carImg = pygame.transform.scale(carImg,(100,160))
expl = pygame.transform.scale(expl,(1000, 800))
intro_window()
game_loop()
quitgame()

