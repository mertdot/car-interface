import pygame
import sys
import serial 
import time
pygame.init()
display_width = 480
display_height = 420

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)

ArduinoSerial = serial.Serial('com3',2000000)
time.sleep(2.0)
#h = ArduinoSerial.readline() 
#h.decode('utf-8')
#h = int(h)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('LODOS')
clock = pygame.time.Clock()

def ledopen():
	ArduinoSerial.write(bytes('o'.encode('utf-8')))
	time.sleep(1.0)
    
def ledclose():
	ArduinoSerial.write(bytes('c'.encode('utf-8')))
	time.sleep(1.0)



def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == 'quit':
            #     pygame.quit()
            #     quit()
            #elif action == 'blabla':
                  #print('blabla')

           
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

        smallText = pygame.font.SysFont('comicsansms', 12)
        TextSurf, TextRect = text_objects(msg, smallText)
        TextRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(TextSurf, TextRect)

def interacttable():
    h = ArduinoSerial.readline() 
    h.decode('utf-8')
    h = int(h)
 
    pygame.draw.rect(gameDisplay, red, (130,310,15,h)) # 4.sü dikdörtgenin aşağıya olan uzanması yani h olmalı 4.
    smallText = pygame.font.SysFont('comicsansms', 12)
    TextSurf, TextRect = text_objects('', smallText)
    TextRect.center = ( (15+(100/2)), (15+(50/2)) )
    gameDisplay.blit(TextSurf, TextRect)

def main_page():

    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms',80)
        TextSurf, TextRect = text_objects('LODOS', largeText)
        TextRect.center = (display_width/2), (display_height/2)
        gameDisplay.blit(TextSurf, TextRect)
        
        button('Lodos1',15,355,100,50,bright_red,red,None)
        button('ledclose',15,15,100,50,bright_red,red,ledclose)
        button('ledopen',365,15,100,50,bright_red,red,ledopen)
        button('Quit',365,355,100,50,bright_red,red,quitgame)
        
        interacttable()

        mouse = pygame.mouse.get_pos()

        # print(mouse)
        
        # sol alttaki buton
        # if 15+100 > mouse[0] > 15 and 355+50 > mouse[1] > 355: 
        #    pygame.draw.rect(gameDisplay, red, (15,355,100,50))
        # else:
        #    pygame.draw.rect(gameDisplay, bright_red, (15,355,100,50))

        # smallText = pygame.font.SysFont('comicsansms', 12)
        # TextSurf, TextRect = text_objects('Lodos1!', smallText)
        # TextRect.center = ( (15+(100/2)), (355+(50/2)) )
        # gameDisplay.blit(TextSurf, TextRect)
        
        # sol üstteki buton
        # if 15+100 > mouse[0] > 15 and 15+50 > mouse[1] > 15:
        #    pygame.draw.rect(gameDisplay, red, (15,15,100,50))
        # else:
        #    pygame.draw.rect(gameDisplay, bright_red, (15,15,100,50))
        
        # smallText = pygame.font.SysFont('comicsansms', 12)
        # TextSurf, TextRect = text_objects('Lodos2!', smallText)
        # TextRect.center = ( (15+(100/2)), (15+(50/2)) )
        # gameDisplay.blit(TextSurf, TextRect)
        
        # sağ üstteki buton
        # if 365+100 > mouse[0] > 365 and 15+50 > mouse[1] > 15:
        #    pygame.draw.rect(gameDisplay, red, (365,15,100,50))
        # else:
        #    pygame.draw.rect(gameDisplay, bright_red, (365,15,100,50))
        
        # smallText = pygame.font.SysFont('comicsansms', 12)
        # TextSurf, TextRect = text_objects('Lodos3!', smallText)
        # TextRect.center = ( (365+(100/2)), (15+(50/2)) )
        # gameDisplay.blit(TextSurf, TextRect)
        
        # sağ alttaki buton
        # if 365+100 > mouse[0] > 365 and 355+50 > mouse[1] > 355:
        #    pygame.draw.rect(gameDisplay, red, (365,355,100,50))
        # else:
        #    pygame.draw.rect(gameDisplay, bright_red, (365,355,100,50))
        
        # smallText = pygame.font.SysFont('comicsansms', 12)
        # TextSurf, TextRect = text_objects('Lodos4!', smallText)
        # TextRect.center = ( (365+(100/2)), (355+(50/2)) )
        # gameDisplay.blit(TextSurf, TextRect)



        pygame.display.update()
        clock.tick(15)



crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        
            
        pygame.display.update()
        clock.tick(60)
        main_page()
        
pygame.quit()
quit()
