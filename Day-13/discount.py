cost= int( input ("enter amount =  "))
print ("cost = ",cost)
if cost > 10000:
    amount = cost * 20 / 100
else:
    if cost > 5000:
        amount = cost * 10 / 100
    else:
        if cost > 1000 :
            amount = cost * 5 / 100
        else:
            amount = 0
print ("payable amount =" , cost - amount)