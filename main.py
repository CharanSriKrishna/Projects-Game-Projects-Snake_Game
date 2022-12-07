import pygame
import  random
import tkinter as tk
from tkinter import messagebox
import snake

global width, rows, s, snack
def redrawWindow(surface):
    surface.fill((0,0,0))
    s.draw (surface)
    s.draw (surface,True)
    snack.draw(surface)
    pygame.display.update()

def randomSnack(rows, item):
 
    positions1 = item.body1
    positions2 = item.body2
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if (len(list(filter(lambda z:z.pos == (x,y), positions1))) > 0)or(len(list(filter(lambda z:z.pos == (x,y), positions2))) > 0):
            continue
        else:
            break
       
    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global width, rows, s, snack
    width = 1000
    rows = 50
    win = pygame.display.set_mode((width,width))
    s = snake.snakes((100,0,0),(100,100,100),(10,15),(15,10))
    snack = snake.cube(randomSnack(rows,s),color=(255,255,255))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(100)
        clock.tick(10)
        redrawWindow(win)
        s.move()

        if s.body1[0].pos == snack.pos:
            s.addCube(True)
            snack = snake.cube(randomSnack(rows,s),color = (255,255,255))
        
        if s.body2[0].pos == snack.pos:
            s.addCube()
            snack = snake.cube(randomSnack(rows,s),color = (255,255,255))

        for x in range(len(s.body1)):
            if s.body1[x].pos in list(map(lambda z:z.pos,s.body1[x+1:])):
                message_box( 'player 2 Won!', 'Player 2 Congrats')
                s.reset((10,15),(15,10))
                break
        if s.body1[0].pos in list(map(lambda z:z.pos,s.body2[:])):
                message_box( 'player 2 Won!', 'Player 2 Congrats')
                s.reset((10,15),(15,10))

        for x in range(len(s.body2)):
            if s.body2[x].pos in list(map(lambda z:z.pos,s.body2[x+1:])):
                message_box( 'player 1 Won!', 'Player 1 Congrats')
                s.reset((10,15),(15,10))
                break
        if s.body2[0].pos in list(map(lambda z:z.pos,s.body1[:])):
                message_box( 'player 1 Won!', 'Player 1 Congrats')
                s.reset((10,15),(15,10))

        redrawWindow(win)
main()