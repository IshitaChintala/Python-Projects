#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:34:34 2023

@author: ishita
"""
#originally I put 1, but I'm supposed to assign these values to 0 so they don't ruin the point system
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

#Original Q1 code

#Q1 = int(input("Do you like 1) Dawn or 2) Dusk? Please enter 1 for Dawn or 2 for Dusk: "))

#if Q1 == 1:
#    print(Gryffindor or Ravenclaw +1)
    
#elif Q1 == 2: 
#    print(Hufflepuff or Slytherin +1)

 #else: 
 #    print("Wrong input") 

#Q1 revised code

#use three print functions for formatting purposes instead of one
print("Q1: Do you like Dawn or Dusk? ")

print(" 1) Dawn")
print(" 2) Dusk")

#use answer variable to simplify code

answer = int(input("Enter answer (1-2): "))

#use radical operators like += to assign G, R, H, S variables a point system, so we can add them at the end
#something I didn't do in ny own code was not use radical operators, making it difficult to assign a point system
if answer == 1: 
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2: 
    Hufflepuff += 1
    Slytherin += 1
else: 
    print('Wrong input.')
    
    
Q2 = int(input("When I'm dead, I want people to remember me as: " + "1) The Good" + " " + "2) The Great" + " " + "3) The Wise" + " " + "4) The Bold" + " "))

if Q2 == 1: 
    Hufflepuff += 2
elif Q2 == 2: 
   Slytherin += 2
elif Q2 == 3: 
    Ravenclaw += 2
elif Q2 == 4: 
    Gryffindor += 2
else: 
    "Wrong input"
    
Q3 = int(input("Which kind of instrument most pleases your ear? " + "1) The violin" + " " + "2) The trumpet" + " " + "3) The piano" + " " + "4) The drum" + " "))

if Q3 == 1: 
   Slytherin += 4
elif Q3 == 2: 
   Hufflepuff += 4
elif Q3 == 3: 
    Ravenclaw += 4
elif Q3 == 4: 
   Gryffindor += 4
else: 
    print("Wrong input")
    
    
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)


if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin: 
    print("Gryffindor!")
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin: 
    print("Ravenclaw!")
elif Hufflepuff >= Slytherin: 
    print("Hufflepuff!")
else: 
    print("Slytherin!")
    
    


