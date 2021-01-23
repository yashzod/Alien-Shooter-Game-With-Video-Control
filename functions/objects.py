import pygame
import cv2

#alien
def alien_rect(display:"pygame display", position:"list"):
    color=(0,0,255)       #RGB--(0,255)
    pygame.draw.rect(display, color, [position[0], position[1],20,20])
    
#shooter
def shooter_rect(display:"pygame display", position:"list"):
    color=(0,0,255)       #RGB--(0,255)
    pygame.draw.rect(display, color, [position[0], position[1],20,20])

#bullets
def bullets_rect(display:"pygame display", position:"list"):
    color=(255,255,255)   #RGB--(0,255)
    pygame.draw.rect(display, color, [position[0], position[1],4,12])
    #pygame.draw.rect(display, color, [position[0]+10, position[1]-5,4,12])
    #pygame.draw.rect(display, color, [position[0]+20, position[1],4,12])
#CV2_limits
def cv2_limits(img,depth,left_x,right_x):
    #CV2_upper_limit
    cv2.rectangle(img,(50,depth),(600,depth),(0,0,255),8)

    #CV2_left_limit
    cv2.rectangle(img,(left_x,70),(left_x,700),(0,255,0),8)

    #CV2_right_limit
    cv2.rectangle(img,(right_x,70),(right_x,700),(0,255,0),8)

#driver code
if __name__=="__main__":
    dis = pygame.display.set_mode((800,800))
    running=True
    while running==True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        alien_rect(dis,[400,400])
        shooter_rect(dis,[300,300])
        bullets_rect(dis,[500,500])
        pygame.display.update()
        pygame.time.wait(100)
    pygame.quit()
    quit()

    
