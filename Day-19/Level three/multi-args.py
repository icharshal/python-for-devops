# def addme(num, num2):
#     total = num + num2
#     return total
# # myval = addme (3,5)
# print(addme(3,6))

def addme(*num):
    total = 0
    for v in num:
        total = total + v
    return total

print (addme(3,3))