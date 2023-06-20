#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:55:15 2023

@author: ishita
"""
#to do: 
    #call variables rock, paper, scissors, ask user to input rock, paper or scissors in console, computer should generate rock, paper or scissors, if computer inserts rock against scissors, then print 'you lost' , if computer inserts paper against rock, print 'you lost' , if computer inserts scissors against paper, print 'you lost' , if none of the above, print 'you won' 
    
    
#import random library so we can use randint function later
import random

#computer variable
rock = 0

#computer variable
paper = 1

#computer variable
scissors = 2


#user variable
Rock = "Rock"

#user variable
Paper = "Paper"

#user variable
Scissors = "Scissors"

#guess variable holds a string that allows the user to input rock, paper or scissors in the console to start the game!
guess = str(input("Rock, Paper, Scissors: "))

#computer will generate a random output in response to user input, but only in integer form
computer = random.randint(0,2)

#if condition to make it so the int form of computer output will hold a string value in console

#aka if computer randomly chooses 0, then Rock will be printed
if computer == 0:
   print ("Rock")

#if computer randomly chooses 1, paper will be printed
if computer == 1:
   print ("Paper")
   
#if computer randomly chooses 2, scissors will be printed
if computer == 2:
   print ("Scissors")
   

#if conditions... elif generated errors and confusion, so this program uses individual if statements

#if user inputs the string "rock", and computer outputs "scissors" randomly, then the program will print "you won!"
#rock crushes scissors   
if guess == Rock and computer == scissors:
              print ("You won!")

#if user inputs string "scissors" and computer randomly generates "paper", print "you won!" 
#scissors cuts paper
if guess == Scissors and computer == paper:
              print ("You won!")
              
#if user inputs string "paper" and computer randomly generates "rock", print "you won!' 
#paper covers rock
if guess == Paper and computer == rock:
              print ("You won!")    

#paper covers rock, so if computer generates paper and user puts rock, you lost :(
if guess == Rock and computer == paper:
              print ("You lost")

#scissors can't cut rock, so user loses
if guess == Scissors and computer == rock:
              print ("You lost")
        
#paper can't cover scissors. scissors cut paper, so user loses
if guess == Paper and computer == scissors:
              print ("You lost")
        
#rock and rock is a tie :/
if guess == Rock and computer == rock: 
              print("It's a tie!")

#paper == int 1, which is paper, paper = paper is tie
if guess == Paper and computer == paper:
              print("It's a tie!")
              
#scissors = scissors, tie
if guess == Scissors and computer == scissors: 
              print("It's a tie!")

#while loop structure: while [variable] radical operator value: variable = XXX   
#using true boolean value, so as long as conditions within while loop are true, the program will keep running and you can play more rounds   

while True:
      
    #rps is another variable similar to guess variable
    #this asks user if they want to play again after previous round
    #if yes, continue program like before, if anything other than yes, break the program 
 
  rps = str(input("Do you want to play again?: "))
  if rps != "Yes": 
    break
 
    #if statement for if user inputs yes, then prompt user to input r p or s
  elif rps == "Yes": 
     guess = str(input("Rock, Paper, Scissors: "))
       
  if computer == 0:
    print ("Rock")
    
  if computer == 1:
    print ("Paper")
    
  if computer == 2:
    print ("Scissors")
    
    #below code is same as above
    #this is game code!
  computer = random.randint(0,2)

  if guess == Rock and computer == scissors:
             print ("You won!")
             
  if guess == Scissors and computer == paper:
             print ("You won!")
             
  if guess == Paper and computer == rock:
             print ("You won!")    

  if guess == Rock and computer == paper:
             print ("You lost")
       
  if guess == Scissors and computer == rock:
             print ("You lost")
       
  if guess == Paper and computer == scissors:
             print ("You lost")
       
  if guess == Rock and computer == rock: 
             print("It's a tie!")
             
             
  if guess == Paper and computer == 1:
             print("It's a tie!")
             
             
  if guess == Scissors and computer == scissors: 
             print("It's a tie!")
   
          
  #if function to stop the program when tries reaches more than 10
#if tries >= 10: 
   #   print("You ran out of tries.")


  
''''irrelevant: if function to stop the program when tries reaches more than 10, if condition to make it so the computer doesn't print integers since the computer variable is an int. computer variable is an int so that the random function can be called, conditions to show whether or not the player won in the console, if guess == Rock and computer != scissors or guess == Scissors and computer != paper or guess == Paper and computer != rock: 


#past attempt to fix while loop problem - 06.14.23

#if user == Rock and computer != scissors: 
     #   print ("Try again")
#elif user == Paper and computer != rock:
      #  print ("Try again")
#elif user == Scissors and computer != paper:
      #  print ("Try again") 

      ''' 



