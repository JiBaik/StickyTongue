import pygame , sys
from pygame.locals import *
import math


pygame.init()

#set RGB colors
BLACK    =  (0 ,0 ,0)
BLUE     = ( 51 ,153 ,255)
#set screen size
display_width = 1000
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',15)
count_string = ('Flies Eaten:')
lives_string = ('Lives Left:')

#import images
start_menuImg = pygame.image.load('start_menu.png')
restart_menuImg = pygame.image.load('restart_menu.png')
flyImg = pygame.image.load('fly.png')
frogImg = pygame.image.load('frog.png')
tongueImg = pygame.image.load('tongue.png')
lilipadImg = pygame.image.load('lilipad.png')
lilipadpartImg = pygame.image.load('lilipadpart.png')
beeImg = pygame.image.load('bee.png')
escapeImg = pygame.image.load('exit.png')

class img_Sprites(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
    def draw(self , image, x , y):
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
        screen.blit(image,(x,y))

class frog_Tongue(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = tongueImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,direction):
        self.rect.y =self.rect.y - direction
        
        #touches hitbox at direction = 220
        
class fly(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = flyImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,fast):
        self.rect.x = self.rect.x+fast
    
class bee(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = beeImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,fast):
        self.rect.x = self.rect.x+fast
        
class escape(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = escapeImg
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 150
 
        
def message_Display(text,x,y):
     text_message = font.render(text ,True ,BLACK)
     screen.blit(text_message,(x,y))
     
def start_menu():
    menu_close = False
    while not menu_close:
            for event in pygame.event.get():   #take in user action
                if event.type == pygame.QUIT: #check if action is quit
                     pygame.quit() 
                     sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                             menu_close = True
                    if event.key == pygame.K_n:
                        print("You quit the game")
                        pygame.quit()
                        sys.exit() 

            screen.fill(BLUE)
            
            screen.blit(start_menuImg,(0,0))
            pygame.display.update()

            clock.tick(30)

    
def game_Loop():
    display_width = 1000
    display_height = 600
    #game loop test
    done = False
    restart = False
    high_Score = 0
    while not done:
       
        #score counter
        score = 0
        life = 5
        #tongue movement
        lick = False
        count = 0
        speed = 110
        #spawn
        fps = 0
        fast = 5
        make_Bee = False
        #location of sprites
        flyW = (display_width * 0.01)
        flyH = (display_height * 0.3)

        lilipadW = (display_width * 0.7)
        lilipadH = (display_height * 0.71)

        lilipadpartH = (display_height *.86)
        
        frogW = (display_width * 0.745)
        frogH = (display_height * 0.78)
                 
        tongueW = (frogW+54)
        tongueH = (frogH-20)


        #initalize groups
        frog_tongue = pygame.sprite.Group()
        frog_tongue.add(frog_Tongue(tongueW,tongueH))
        
        flies = pygame.sprite.Group()
        flies.add(fly(flyW,flyH))

        bees = pygame.sprite.Group()

        escaped = pygame.sprite.Group()
        escaped.add(escape())

        if restart:
                display_width = 500
                display_height = 300
                screen = pygame.display.set_mode((display_width,display_height))
                menu_close = False
                parsed_high_Score = str(high_Score)
                while not menu_close:
                        for event in pygame.event.get():   #take in user action
                            if event.type == pygame.QUIT: #check if action is quit
                                  pygame.quit()
                                  sys.exit() #flag to quit gameloop
                            #when space is pressed, tongue goes up
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                         menu_close = True
                                if event.key == pygame.K_n:
                                    print("You quit the game")
                                    pygame.quit()
                                    sys.exit()

                        screen.blit(restart_menuImg,(0,0))
                        message_Display("Your highest score was:", display_width-370, display_height*0.5)
                        message_Display(parsed_high_Score, display_width -185, display_height*0.5)
                        pygame.display.update()
            
        display_width = 1000
        display_height = 600
        screen = pygame.display.set_mode((display_width,display_height))
        restart = True
        #game loop
        while life != 0:
            for event in pygame.event.get():   #take in user action
                if event.type == pygame.QUIT: #check if action is quit
                    print ("You have exited the game")
                    pygame.quit()
                    sys.exit()
                #when space is pressed, tongue goes up
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                             lick = True
                     
            #set background
            screen.fill(BLUE)
            #create score counter
            parsed_Score = str(score)
            if score >= high_Score:
                high_Score = score
            
            message_Display(count_string, display_width-150, display_height*0.1)
            message_Display(parsed_Score, display_width -60, display_height*0.1)
            #create lives counter
            parsed_Lives = str(life)
            message_Display(lives_string , display_width/2, display_height *0.1)
            message_Display(parsed_Lives , (display_width/2)+80, display_height *0.1)

            #draw static images
            lilipad = img_Sprites()
            lilipad.draw(lilipadImg,lilipadW,lilipadH)
            
            frog_tongue.draw(screen)
            
            lilipadpart = img_Sprites()
            lilipadpart.draw(lilipadpartImg,lilipadW,lilipadpartH)

            frog = img_Sprites()
            frog.draw(frogImg,frogW,frogH)

            escaped.draw(screen)        
            #move tongue quickly within 6 frames divide       
            if lick == True and count <=3:
                frog_tongue.update(speed)
                count += 1
            if count >=3 and count <=6:
                frog_tongue.update(-speed)
                count+=1
            if count == 6:
                lick = False
                count = 0
            
           #spawning algorithim
            fps += 1
            if(fps%2):
                make_Bee = True
            else:
                make_Bee = False
            if(fps > 180):
                if(fps % 107==0 or fps % 135 == 0 or fps % 177 ==0):
                    if(make_Bee == True):
                        bees.add(bee(flyW,flyH))
                    else:
                        flies.add(fly(flyW,flyH))         
            
            flies.draw(screen)
            flies.update(fast)
            bees.draw(screen)
            bees.update(fast)
            #speed increase as score gets higher
            if (score > 0 and score  == 5):
                fast = 7
            if (score > 0 and score  == 10):
                fast = 10
            if (score > 0 and score == 20):
                fast = 12
            if (score > 0 and score == 25):
                fast = 15
            if (score > 0 and score == 30):
                fast = 17
 
            #check collisions between frog tongue, flies, and bees
            if pygame.sprite.groupcollide(frog_tongue,flies,False,True):
                score +=1
            if pygame.sprite.groupcollide(frog_tongue,bees,False,True):
                life -= 1
            if pygame.sprite.groupcollide(flies,escaped,True,False):
                life -=1
            pygame.sprite.groupcollide(bees,escaped,True,False)
            #update with graphics
            pygame.display.update()
            
            #get 60fps 
            clock.tick(60)


start_menu()
game_Loop()


pygame.quit()

quit()  



