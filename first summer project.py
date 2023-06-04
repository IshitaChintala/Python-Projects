# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = 'ishita'
#name = chan is False, sky is the first true value, so the if block executes as 'sky', aka true and access granted!

if name in ['chan', 'sky', 'ishita']: 
    print('Access Granted!')
    
else: 
    print('Access Denied')
    
print("i love myself")

a = 3
b = 2
c = 21

average = (a + b + c) / 3

print(average) 

sky = a // b
print(sky)

rando = 7 % 2
print(rando)

power = 10 ** 23
print(power)

#dog years converter
#input dog years
#output human years

def dog_year_converter(years): 
    years = int(years)
    if years < 0: 
        return 'age must be larger than 0'
    #human years multiplied by 7
    return years*7
human_years = input('Enter your dogs age in human years: ')
print(dog_year_converter(human_years)); 


#first for loop will go through a max and min of 0 and 10 times
def mystery_function(num1, num2): 
    for num in range(num1, num2 + 1): 
        #num in line 54 is just the index... if num is greater than 1, then the code will run
        if num > 1: 
            #second for loop starts in line 56
            #finds factors (multiples)
            #take num from line 54 and i and find any factors, no factor than print a number
            #find all prime numbers from min and max
            for i in range(2, num): 
                if (num % i) == 0: 
                    break
                else: print(num)
                
        print(mystery_function(0,10))









