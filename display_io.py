import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
x = 0
y = 0
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10,20] = green
pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
#(where to print, color, width starting location, width, height)
pygame.draw.rect(gameDisplay, red, (100, 100, 50,25))
pygame.draw.circle(gameDisplay, white, (200,300), 56)
pygame.draw.polygon(gameDisplay, green,((45,56),(343,423),(23,43),(564,45)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
