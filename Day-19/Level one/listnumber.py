list_num= [1,3,5,6,4,5,45,4,4,3,3,35,66,3,5,7,56]
user_input = int (input ("Enter a value : "))

for ln in list_num :
    if ln == user_input:
        print ("match found ")
#        print ("Entered value is ",user_input)
        break
else :
        print ("No match found")
print ("Hey i am outside of loop")

for l in "HelloWorld" :
     if l == "o" :
          break
     print ("value is : ", l)