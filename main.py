import pygame
import random
import math

pygame.init()
screen=pygame.display.set_mode((800,600))
back=pygame.image.load("gal.png")
score=0

pygame.display.set_caption("kushagra")
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


playerImg=pygame.image.load("aircraft.png")
playerx=370
playery=480
x_chnge=0

enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_chnge=[]
enemyy_chnge=[]
n=6
for i in range (n):
    enemyImg.append(pygame.image.load("zombie.png"))
    enemyx.append(random.randint(0,800))
    enemyy.append(random.randint(50,150)) 
    enemyx_chnge.append(2)
    enemyy_chnge.append(40)
n=6

bulletImg=pygame.image.load("bullet.png")
bulletx=0
bullety=480
bulletx_chnge=0
bullety_chnge=20
bullet_state="ready"


font=pygame.font.Font('freesansbold.ttf',32)
tx=10
ty=10

def show_score(x,y):
    scores=font.render("SCORE:"+str(score),True,(255,255,255))
    screen.blit(scores,(x,y))
    

def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+16))

def iscollision(x1,y1,x2,y2):
    d=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if d<27:
        return True
    return False

overfont=pygame.font.Font('freesansbold.ttf',64)
def gameover():
    scores=font.render("GAME OVER:"+str(score),True,(255,255,255))
    screen.blit(scores,(250,250))
    
    #overtext=overfont.render("GAME OVER",True,(255,255,255))
    #screen.blit(overtext,(200,250))



running =True
while running:
    screen.fill((0,0,0))
    screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_chnge=-5
            if event.key==pygame.K_RIGHT:
                x_chnge=5
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletx=playerx
                    fire_bullet(bulletx,bullety)
             
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_chnge=0
                
                
            
                
    playerx+=x_chnge
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736
        
    for i in range(n):       
        
        if enemyy[i]>370:
            for j in range (n):
                enemyy[j]=2000
            gameover()
            break
        
        enemyx[i]+=enemyx_chnge[i]
    
        if enemyx[i]<=0:
            enemyx_chnge[i]=5
            enemyy[i]+=enemyy_chnge[i]
        elif enemyx[i]>=736:
            enemyx_chnge[i]=-5
            enemyy[i]+=enemyy_chnge[i]
        c=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if c:
            bullety=480
            bullet_state="ready"
            score+=1
            print(score)
            
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150) 
        
        enemy(enemyx[i],enemyy[i],i)
    
    if bullety<=0:
        bullety=480
        bullet_state="ready"
    if bullet_state =="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_chnge
        
        
    

    
    player(playerx,playery)
    show_score(tx,ty)
    pygame.display.update()
            
