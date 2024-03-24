import pygame
from network import Network
pygame.init()
width=500
height=500
win=pygame.display.set_mode((width,height))

# set caption
pygame.display.set_caption("client")

clientNumber=0


class Player():
    vel=3
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rect=(x,y,width,height)
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x-=Player.vel
        
        if keys[pygame.K_RIGHT]:
            self.x+=Player.vel

        if keys[pygame.K_DOWN]:
            self.y-=Player.vel

        if keys[pygame.K_UP]:
            self.y+=Player.vel

        self.update()
        
    def update(self):
        self.rect=(self.x,self.y,self.width,self.height)
        



def convertttos(tuple):
    return (str(tuple[0])+','+str(tuple[1]))


def convertstot(string):
    list=string.split(',')
    # for l in list:
    return (int(list[0]),int(list[1]))



# clock=pygame.time.Clock()
def redrawWindow(player,win,player2):
    # filling the window with white color
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()




def main():
    running=True
    n=Network()
    startPos=convertstot(n.getpos())
    p=Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2=Player(0,0,100,100,(255,0,0))

    clock=pygame.time.Clock()

    while(running):
        clock.tick(60)
        p2pos=convertstot(n.send(convertttos((p.x,p.y))))
        p2.x=p2pos[0]
        p2.y=p2pos[1]
        p2.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()

        p.move()
        redrawWindow(p,win,p2)

main()





