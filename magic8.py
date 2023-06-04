#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:11:50 2023

@author: ishita
"""
#extract random library so we can use library functions
import random

#assign question variable to ask user to enter a yes or no question
question = input("Enter yes or no question: ")

#assign random number variable to tell program to randomly assign an answer to the question above with the bounds 1 and 9
#randstr does not exist
random_number = random.randint(1, 9)

#if statements to assign string values to each randomized integer since randstr doesn't exist
if random_number == 1:
    answer = "Yes - definitely."
   
    #use elif after the original if to continue the if statement so all conditions are met
    #elif = "else if"
elif random_number == 2: 
    answer = "It is decidedly so."

elif random_number == 3: 
    answer = "Without a doubt"

elif random_number == 4: 
    answer = "Reply hazy, try again."

elif random_number == 5: 
    answer = "Ask again later"

elif random_number == 6: 
    answer = "Better not tell you now"

elif random_number == 7:
    answer = "Outlook not so good"

elif random_number == 8: 
        answer = "Very doubtful"
        
        #display question and the value within the  question string in line 12
print('Question:  ' + question)

#display magic 8 ball and the randomized answer within the if statements
#do not use 'Magic 8 Ball: ' + random_number, as random_number will throw an 
#error since random error is an integer value, when we want a string value 
#within the console derived from the if statements above
print('Magic 8 Ball:  ' + answer) 

