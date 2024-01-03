# My first program to write table of asked number till 10th digit
number = int(input("Enter number who's table is required - "))
def table (number):
    for i in range (1 ,11):
        print (i , "x " + str(number) + "=" ,i *number)
    return
table (number)