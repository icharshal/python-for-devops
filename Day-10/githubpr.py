import requests

url=requests.get(url="https://api.github.com/repos/LondheShubham153/90DaysOfDevOps/pulls")
#print(url.json())
output= url.json()
#print (output[1]["id"])
for id in output:
    print(id["id"])