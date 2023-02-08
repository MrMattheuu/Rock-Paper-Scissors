import pygame
import random
pygame.init()
#change
#variables and constants here
BGCOLOR  = "#Ff00e4"
player_1 = ""

#load assets here
rock_image = pygame.image.load("assets/happyrock.png")
rock_image=pygame.transform.scale(rock_image,(305,160))

scissors_image = pygame.image.load("assets/happyscissors.png")
scissors_image=pygame.transform.scale(scissors_image,(240,155))

paper_image=pygame.image.load("assets/happypaper.png")
paper_image=pygame.transform.scale(paper_image,(175,182))

#functions to make interactable objects
def rock(x,y):
    screen.blit(rock_image,(x,y))
def scissors(x,y):
    screen.blit(scissors_image,(x,y))
def paper(x,y):
    screen.blit(paper_image,(x,y))

def player_choice(text):
    setup_text = pygame.font.SysFont("arial",60)
    textSurface = setup_text.render(text, True, "black")
    screen.blit(textSurface, (100,500))


#initializing screen and set it up
screen = pygame.display.set_mode([800,800])

running = True
while running:
    #get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player_1 = "rock"
            elif event.key == pygame.K_3:
                player_1="paper"
            elif event.key == pygame.K_2:
                player_1="scissors"
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (mouse_x >= 50 and mouse_x <=355) and (mouse_y >= 100 and mouse_y <= 260):
                    player_1 = "rock"
                elif (mouse_x >= 350 and mouse_x <=595) and (mouse_y >= 100 and mouse_y <= 250):
                    player_1 = "scissors"
                elif (mouse_x >= 600 and mouse_x <=775) and (mouse_y >= 100 and mouse_y <= 282):
                    player_1 = "paper"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if rock.collidepoint(mouse_x,mouse_y):
                        player_1 = "rock"
                    elif scissors.collidepoint(mouse_x,mouse_y):
                        player_1 = "scissors"
                    elif paper.collidepoint(mouse_x,mouse_y):
                        player_1 = "paper"
#get computer player input
    compchoices = ["paper","scissors","rock"]
    player_2=random.choice(compchoices)

if player_2 == "paper" and player_1 == "paper":
     print("tie")


        
    #do stuff

    #refresh screen
screen.fill(BGCOLOR)
    #printing computer choice as image
if player_2 == "paper":
    screen.blit(paper_image,(600,400))
      
    
rock = screen.blit(rock_image,(50,100))
scissors = screen.blit(scissors_image,(350,100))
paper = screen.blit(paper_image,(600,100))
   #must I delete this last 3???
'''
if player_1 != "":
    player_choice(f"You've selected {player_1}")'''
        
    
    
    #draw screen
pygame.display.flip()
    

pygame.quit()


