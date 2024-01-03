number = int (input ("please enter number to check prime or not "))

if number > 1 :
    for i in range (2, number):
        if (number % i == 0):
 #           print (number, "This is not prime number")
            print (i, "times", number//i , "is", number)
            break
    else :
            print (" This number is prime")