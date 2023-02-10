#By Matthew Boylan
#Feb 10 2023

#Importing the necessary libraries:

#The pygame library is imported to be used for the creation of a graphical user interface.
#The random library is imported to be used for generating a random choice for the computer.
#Initializing the pygame library:

#The pygame.init() function is called to initialize the library.

import pygame
import random
pygame.init()

#Defining variables and constants:

#BGCOLOR is defined as a constant representing the background color of the game screen.
#player_1 is defined as a variable to store the player's choice.
#Defining variables and constants:

##change
#variables and constants here
BGCOLOR  = "#Ff00e4"
player_1 = ""

#Loading assets:
#Three image files, which represent rock, scissors, and paper, are loaded into memory and stored as variables rock_image, scissors_image, and paper_image respectively.
#The pygame.transform.scale function is used to scale each image to a specific size.
#load assets here

rock_image = pygame.image.load("assets/happyrock.png")
rock_image=pygame.transform.scale(rock_image,(305,160))

scissors_image = pygame.image.load("assets/happyscissors.png")
scissors_image=pygame.transform.scale(scissors_image,(240,155))

paper_image=pygame.image.load("assets/happypaper.png")
paper_image=pygame.transform.scale(paper_image,(175,182))

##Functions to create interactable objects:

#functions to make interactable objects
#Three functions, rock, scissors, and paper, are defined to render the corresponding images on the game screen.
#Each function takes in the x,y coordinates of where to render the image on the game screen.
def rock(x,y):
    screen.blit(rock_image,(x,y))
def scissors(x,y):
    screen.blit(scissors_image,(x,y))
def paper(x,y):
    screen.blit(paper_image,(x,y))
def computerselction():
    compchoices = ["paper","scissors","rock"]
    player_2=random.choice(compchoices)
    return(player_2)



#unction to display the player's choice:
#The player_choice function is defined to display the player's choice as text on the game screen.
def player_choice(text):
    setup_text = pygame.font.SysFont("arial",60)
    textSurface = setup_text.render(text, True, "black")
    screen.blit(textSurface, (100,500))

#Initializing the game screen:
#A game screen with a specified size of 800x800 is created and stored as the screen variable.
#initializing screen and set it up
screen = pygame.display.set_mode([800,800])
player2= computerselction()

player2
#Game loop:

# while loop is defined to run the game as long as the running variable is set to True.
#Inside the loop, pygame.event.get() is used to get input events from the user.
#Depending on the type of event, different actions are taken:
#If the event type is QUIT, the running variable is set to False to exit the game loop.
#If the event type is KEYDOWN, the value of the pressed key is checked to determine the player's choice.
#If the event type is MOUSEBUTTONDOWN, the mouse position is used to determine the player's choice by checking 
# if it falls within the boundaries of any of the three images.

running = True

while running:
  #  #get input
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

##get computer player input
#Getting the computer player's input:

#A list of three options, compchoices, is defined to represent rock, scissors, and paper.
#The random.choice function is used to generate a random choice for the computer and store it in the player_2 variable.


#Determining the outcome of the game:

#A series of if statements is used to compare the player's and computer's choices to determine the outcome of the game. 
# Currently, there is only one scenario that prints "tie" if both players choose paper.
if player_2 == "paper" and player_1 == "paper":
     print("tie")

#Updating the game screen:
#The screen.fill function is used to fill the screen with the background color defined in BGCOLOR.
#The screen.blit function is used to render the images and the player's choice on the game screen.
#The pygame.display.flip() function is called to update the game screen.
        
  #  #do stuff

   # #refresh screen
screen.fill(BGCOLOR)
    #printing computer choice as image
if player_2 == "paper":
    screen.blit(paper_image,(600,400))
      
    
rock = screen.blit(rock_image,(50,100))
scissors = screen.blit(scissors_image,(350,100))
paper = screen.blit(paper_image,(600,100))
 #  #must I delete this last 3???

pygame.display.update()

'''
if player_1 != "":
    player_choice(f"You've selected {player_1}")'''
        
    
    
 #   #draw screen
pygame.display.flip()
    

pygame.quit()






















'''

Sure! Here's my take on what each part of the code does:



Game loop:

A while loop is defined to run the game as long as the running variable is set to True.
Inside the loop, pygame.event.get() is used to get input events from the user.
Depending on the type of event, different actions are taken:
If the event type is QUIT, the running variable is set to False to exit the game loop.
If the event type is KEYDOWN, the value of the pressed key is checked to determine the player's choice.
If the event type is MOUSEBUTTONDOWN, the mouse position is used to determine the player's choice by checking if it falls within the boundaries of any of the three images.
Getting the computer player's input:

A list of three options, compchoices, is defined to represent rock, scissors, and paper.
The random.choice function is used to generate a random choice for the computer and store it in the player_2 variable.

Determining the outcome of the game:

A series of if statements is used to compare the player's and computer's choices to determine the outcome of the game. Currently, there is only one scenario that prints "tie" if both players choose paper.
Updating the game screen:
The screen.fill function is used to fill the screen with the background color defined in BGCOLOR.
The screen.blit function is used to render the images and the player's choice on the game screen.
The pygame.display.flip() function is called to update the game screen.
Ex
'''