'''algo- serverfile to be update, read write '''
def config(filepath,key,value):
    
    with open(filepath,"r") as file:
        lines=file.readline()
    
    with open (filepath,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + " " + value + "\n")
            else:
                file.write(line)

config("server.conf","MAX_CONNECTIONS","50")