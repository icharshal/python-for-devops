lower_range = 550
upper_range = 600

    
from array import *
#number = 11
for number in range (lower_range, upper_range):
    if number > 1 :
        for i in range (2 , number):
            if (number % i == 0):
#                print (number, "This is not prime number")
                break
        else:
            print(number, "This number is prime")
            
            store = str(number) 
                       
            file = open("prime_number.txt", "w+")
            file.write((store)) 
            file.close()
            #