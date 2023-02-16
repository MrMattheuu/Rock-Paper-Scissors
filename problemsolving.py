#====================================
#Author:                            |
#Matthew Boylan                     |
#                                   |
#File Name:                         |
#Problemsolving.py                  |
#                                   |
#Objective:                         |
#I am going to be solving problems  |
#                                   |
#date:                              |
#Feb 15 2023                        |
#====================================

#357 until my birthday!!!
#3 days until Trebbe's brithday!!!

#onansnumbers = "Ronan loves to count numbers!!!"

#print(ronansnumbers.count("!"))

#print(ronansnumbers.split("o"))
wordcount = 0
#GET INPUT
inputt = input("Please type stuff here: ")


#get legnth
length = len(inputt)
#check what is/isnt a space
for x in range (length):
    if (inputt[x]) == " " and (inputt[x-1]) == " ":
        wordcount +=0
    elif (inputt[x]) == " " and (inputt[x-1]) != " ":
        wordcount +=1
        #comment
print(f"the word count of your message is {wordcount}")
    
        

'''
#if there are any double spaces
if input.count(" ") 

    #dont count the spaces
    *placeholder*

if input.count("  ") == 0:
    #count spaces
    wordcount = (input.count("x "))
#wordcount=(input.count(" ")) + 1

#PRINT WORD COUNT
print(f"the word count of the message is: {wordcount}")

'''