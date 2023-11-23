import requests

response = requests.get("https://api.github.com/repos/LondheShubham153/90DaysOfDevOps/pulls")

#print(response.json()) # all

full_detail = response.json()

#print(full_detail[0]["user"]["login"])
#print(full_detail[0]["url"])

# for loop to get all user 
#for i in range(len(full_detail)):
 #   print (full_detail[i]["user"]["login"])

                     

