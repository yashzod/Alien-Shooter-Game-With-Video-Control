import cv2
import pyautogui
import pygame
from functions import random_aliens
from functions import objects

pygame.font.init()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
dis = pygame.display.set_mode((800,800))

shoot=True #shooter_shoot_if_shoot
running = True
#initial_shooter_position
pos=[100,600]
#initial_shooter_speed
xc,yc=0,0

#bullets
bullets=[]

#aliens
aliens=random_aliens.random_aliens(20)

#score
score = 0
while running:
    
    if len(aliens)==0:
        dis.fill((0,0,0))
        myfont=pygame.font.SysFont('Comic Sans MS', 60)
        text=myfont.render("You Won", False, (255,255,255))
        dis.blit(text,(300,300))
        pygame.display.update()
        pygame.time.wait(100)
        break
        
    for i in aliens:
        if i[1]>580:
            dis.fill((0,0,0))
            myfont=pygame.font.SysFont('Comic Sans MS', 60)
            text=myfont.render("Game Over", False, (255,255,255))
            dis.blit(text,(300,300))
            pygame.display.update()
            pygame.time.wait(100)
            running=False
            break
    if running==False:
        break
    #pygame_QUIT
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    dis.fill((0,0,0))
    myfont=pygame.font.SysFont('Comic Sans MS', 30)
    text=myfont.render(str(score), False, (255,255,255))
    dis.blit(text,(750,50))
    pygame.time.wait(100)
    #face_detection
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        #rectangle_on_face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    #limits_for_control
    depth=70
    left_x=450
    right_x=200
    objects.cv2_limits(img,depth, left_x, right_x)
    for (x,y,w,h) in faces:
        if x < right_x:
            xc=+5
        if x+w > left_x:
            xc=-5

        if shoot and y<depth:
            #pyautogui.press('space')
            bullets.append([pos[0],pos[1]])
            bullets.append([pos[0]+10,pos[1]])
            bullets.append([pos[0]+20,pos[1]])
            shoot=False
        elif y>70 and y<90:
            shoot=True
    
    #movement_of_shooter
    pos[0]+=xc
    
    #show_shooter
    objects.shooter_rect(dis,pos)
    
    #show_bullets
    for i in range(len(bullets)):
        bullets[i][1]-=20
        objects.bullets_rect(dis,(bullets[i]))
        
    #show_aliens
    for i in aliens:
        objects.alien_rect(dis,i)
        i[1]+=2
        
    #bullets_aliens_collision
    x=[]
    y=[]
    for i in range(len(bullets)):
        if bullets[i][1]<100:
            x.append(i)
    for i in range(len(aliens)):
        ai=i
        i=aliens[i]
        xi=[i[0]-10,i[0]+25]
        yi=[i[1]-10,i[1]+25]
        for j in range(len(bullets)):
            if i in y:
                break
            aj=j
            j=bullets[j]
            if j[1] in range(yi[0],yi[1]+1) and j[0] in range(xi[0],xi[1]+1):
                y.append(ai)
                x.append(aj)
                break
            
    #del_bullets
    for i in x:
        del bullets[i]
        x.remove(i)


    #kill_aliens
    for i in y:
        del aliens[i]
        score+=10
        y.remove(i)
    
    
    
    img=cv2.flip(img,1)
    cv2.imshow('img',img)
    cv2.waitKey(3)
    pygame.display.update()


cap.release()
cv2.destroyAllWindows()
