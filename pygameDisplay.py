import pygame, os, sys
from pygame.locals import *
import readDMX
import sendsacn

#Init Modules
pygame.init()
screen = pygame.display.set_mode((1280,1024))
readDMX.init()
sendsacn.init()

#Colour Consts
BLACK = (0,0,0)
WHITE = (255,255,255)
LGREY = (200,200,200)
DGREY = (50,50,50)

def main():
    #main loop
    while True:
        drawScreen()
        checkForEvent()

def drawScreen():
    #get dmx array
    dmx = readDMX.getDMX()
    #send dmx array through sacn (to capture)
    sendsacn.send(dmx)

    #Visualise DMX in Pygame window
    screen.fill(BLACK)
    highlightedY = pygame.mouse.get_pos()[1]//255
    highlightedX = pygame.mouse.get_pos()[0]//10+1
    for y in range(4):
        for x in range(128):
            if y == highlightedY and x == highlightedX-1:
                col = LGREY
                pygame.draw.rect(screen, DGREY, (x*10, y*255, 10, 255))
            else:
                col = WHITE
            pygame.draw.rect(screen, col, (x*10, (y*255)+(255-dmx[y*128+x]), 10, dmx[y*128+x]))
    font = pygame.font.Font(None, 100)
    text = font.render(str(highlightedX+128*highlightedY), True,LGREY)
    screen.blit(text, (0,0))
    pygame.display.update()

def close():
    #Quit all modules
    readDMX.quit()
    sendsacn.quit()
    pygame.quit()
    sys.exit()

def checkForEvent():
    #Check for key inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            close()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                close()
            if event.key == K_F5:
                #Restart connection to PhantomJester
                readDMX.init()
            if event.key == K_F4:
                readDMX.ALTWASH = not readDMX.ALTWASH

if __name__ == '__main__':
    main()
