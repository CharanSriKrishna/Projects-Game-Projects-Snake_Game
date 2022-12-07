import pygame

class cube(object):
    rows=50
    w =1000
    def __init__(self,start,dirnx=1,dirny=0,color=(100,100,100)):
        self.pos=start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color
    
    def move(self,dirnx,dirny):
        self.dirnx=dirnx
        self.dirny=dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self,surface,eyes=False):
        dis=self.w//self.rows
        i=self.pos[0]
        j=self.pos[1]

        pygame.draw.circle(surface, self.color, [i*dis+1,j*dis+1],dis/2,0)


class snakes(object):
    body1=[]
    body2=[]
    turns1={}
    turns2={}
    def __init__(self, color1, color2, pos1, pos2):
        self.color1=color1
        self.color2=color2
        self.head1=cube(pos1,1,0,color1)
        self.head2=cube(pos2,-1,0,color2)
        self.body1.append(self.head1)
        self.body2.append(self.head2)
        self.dirnx1=1
        self.dirny1=0
        self.dirnx2=0
        self.dirny2=1
    
    def move(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            
            keys=pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx1 = -1
                    self.dirny1 = 0
                    self.turns1[self.head1.pos[:]] = [self.dirnx1, self.dirny1]
                
                elif keys[pygame.K_a]:
                    self.dirnx2 = -1
                    self.dirny2 = 0
                    self.turns2[self.head2.pos[:]] = [self.dirnx2, self.dirny2]
 
                elif keys[pygame.K_RIGHT]:
                    self.dirnx1 = 1
                    self.dirny1 = 0
                    self.turns1[self.head1.pos[:]] = [self.dirnx1, self.dirny1]

                elif keys[pygame.K_d]:
                    self.dirnx2 = 1
                    self.dirny2 = 0
                    self.turns2[self.head2.pos[:]] = [self.dirnx2, self.dirny2]
 
                elif keys[pygame.K_UP]:
                    self.dirnx1 = 0
                    self.dirny1 = -1
                    self.turns1[self.head1.pos[:]] = [self.dirnx1, self.dirny1]
                
                elif keys[pygame.K_w]:
                    self.dirnx2 = 0
                    self.dirny2 = -1
                    self.turns2[self.head2.pos[:]] = [self.dirnx2, self.dirny2]
 
                elif keys[pygame.K_DOWN]:
                    self.dirnx1 = 0
                    self.dirny1 = 1
                    self.turns1[self.head1.pos[:]] = [self.dirnx1, self.dirny1]

                elif keys[pygame.K_s]:
                    self.dirnx2 = 0
                    self.dirny2 = 1
                    self.turns2[self.head2.pos[:]] = [self.dirnx2, self.dirny2]

        for i,c in enumerate(self.body1):
            p = c.pos[:]
            if p in self.turns1:
                turn = self.turns1[p]
                c.move(turn[0],turn[1])
                if i == len(self.body1)-1:
                    self.turns1.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)

        for i,c in enumerate(self.body2):
            p = c.pos[:]
            if p in self.turns2:
                turn = self.turns2[p]
                c.move(turn[0],turn[1])
                if i == len(self.body2)-1:
                    self.turns2.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)


    def reset(self, pos1,pos2):
        self.head1 = cube(pos1,color = self.color1)
        self.body1 = []
        self.body1.append(self.head1)
        self.turns1 = {}
        self.dirnx1 = 0
        self.dirny1 = 1
        self.head2 = cube(pos2,0,1,self.color2)
        self.body2 = []
        self.body2.append(self.head2)
        self.turns2 = {}
        self.dirnx2 = 1
        self.dirny2 = 0

    def addCube(self,val=False):
        if val:
            tail = self.body1[-1]
            dx,dy = tail.dirnx, tail.dirny

            if dx == 1 and dy == 0:
                self.body1.append(cube((tail.pos[0]-1,tail.pos[1]),color = (100,0,0)))
            elif dx == -1 and dy == 0:
                self.body1.append(cube((tail.pos[0]+1,tail.pos[1]) ,color = (100,0,0)))
            elif dx == 0 and dy == 1:
                self.body1.append(cube((tail.pos[0],tail.pos[1]-1),color = (100,0,0)))
            elif dx == 0 and dy == -1:
                self.body1.append(cube((tail.pos[0],tail.pos[1]+1),color = (100,0,0)))

            self.body1[-1].dirnx = dx
            self.body1[-1].dirny = dy
        else:
            tail = self.body2[-1]
            dx,dy = tail.dirnx, tail.dirny

            if dx == 1 and dy == 0:
                self.body2.append(cube((tail.pos[0]-1,tail.pos[1])))
            elif dx == -1 and dy == 0:
                self.body2.append(cube((tail.pos[0]+1,tail.pos[1])))
            elif dx == 0 and dy == 1:
                self.body2.append(cube((tail.pos[0],tail.pos[1]-1)))
            elif dx == 0 and dy == -1:
                self.body2.append(cube((tail.pos[0],tail.pos[1]+1)))

            self.body2[-1].dirnx = dx
            self.body2[-1].dirny = dy


    def draw(self,surface,val=False):
        if val:
            for i,c in enumerate(self.body1):
                if i==0:
                    c.draw(surface,True)
                else:
                    c.draw(surface)
        else :
            for i,c in enumerate(self.body2):
                if i==0:
                    c.draw(surface,True)
                else:
                    c.draw(surface)
