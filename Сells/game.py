import pygame
import sys
import language as l
from menu import *
pygame.init()

info = pygame.display.Info()
fulldisplay_info = (info.current_w,info.current_h)
size_minimap = (fulldisplay_info[0]/5,fulldisplay_info[0]/5)
nomber_language = 1
width = 500
height = 500
FPS = 60
name_display = "Squares"
icon = pygame.transform.scale((pygame.image.load("pictures/icon.png")),(30,30))
menu_bd = pygame.transform.scale(pygame.image.load("pictures/menu_bg.png"),fulldisplay_info)
game_bd = pygame.transform.scale(pygame.image.load("pictures/space.jpg"),fulldisplay_info)
terra = pygame.transform.scale(pygame.image.load("pictures/terra.png"),(fulldisplay_info[0]/10,fulldisplay_info[0]/10))
tic = 0
x = 100
y = 100 
spin = 1
colors = {
    "Red":(255,0,0),
    "Eastern Blue":(30, 129, 176)
}


display = pygame.display.set_mode(fulldisplay_info,pygame.FULLSCREEN)

virtual_display = pygame.Surface(fulldisplay_info)
mini_maps = pygame.transform.scale( virtual_display,(100,100))
clock = pygame.time.Clock()
pygame.display.set_caption(name_display)
pygame.display.set_icon(icon)



play = Menu(display,"1-blackmoor-let-plain103.ttf",100)  
play.create_button(l.play[nomber_language],(100,100,300,100)) 
play.create_button(l.language[nomber_language],(100,250,600,100)) 
play.create_button(l.exit[nomber_language],(100,400,300,100)) 

language_option = Menu(display,"1-blackmoor-let-plain103.ttf",100) 
language_option.create_button(l.english[nomber_language],(100,100,300,100)) 
language_option.create_button(l.ukrainian[nomber_language],(100,250,600,100)) 
language_option.create_button(l.back[nomber_language],(100,400,300,100)) 

game = Menu(display,"1-blackmoor-let-plain103.ttf",100)  
game.create_button2(icon,(0,0,30,30)) 

pause = Menu(display,"1-blackmoor-let-plain103.ttf",100)  
pause.create_button2(icon,(0,0,30,30)) 
pause.create_button(l.pausa[nomber_language],(100,400,300,100)) 

runing = True
def menu1():
    runing1 = True
    while runing1 :
        a = play.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (a == 0) :
                    print("i i i  ха")
                    game1()
                if (a == 1):
                    runing1 = False
                    language_options()
                if (a == 2) :
                    pygame.quit()
                    sys.exit()
                
        display.blit(menu_bd,(0,0))
        display.blit(icon,(0,0))
        
        play.draw_menu((100,100,100))
        pygame.display.update()
        clock.tick(FPS)
  
def language_options():
    runing1 = True
    while runing1 :
        a = language_option.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (a == 0) :
                    nomber_language = 0  
                if (a == 1):
                    nomber_language = 1
                if (a == 2) :
                    runing1 = False
                    menu1()
                
        display.blit(menu_bd,(0,0))
        display.blit(icon,(0,0))
        
        language_option.draw_menu((100,100,100))
        pygame.display.update()
        clock.tick(FPS)
def game1():
    runing1 = True
    while runing1 :
        
        a = game.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (a == 0) :
                    pause1()
         
               
        display.blit(game_bd,(0,0))  
        terra_spin(10,500,200)
        game.draw_menu((100,100,100))
        pygame.display.update()
        clock.tick(FPS)

def pause1():
    runing2 = True
    while runing2 :
        b = pause.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (b == 0) :
                    runing2 = False
                if (b == 1):
                    menu1()  
                
            pause.draw_menu((100,100,100))           
            pygame.display.update()
            clock.tick(FPS)
def terra_spin(speed = 30,x = 100,y = 100,w = 300,h = 300):
    global tic
    global spin
    tic +=1
    if tic == speed:
        tic = 0
        spin +=1
    if spin > 12:
        spin = 1
    display.blit(pygame.transform.scale((pygame.image.load("terra_animation/terra_"+str(spin)+".png")),(w,h)),(x,y))

menu1()
   
