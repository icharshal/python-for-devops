def main():
    file = open("lco.txt", "w+")
    for i in range (20):
        file.write("This is python code %d \n" %(i))
    file.close()
if __name__=="__main__":
    main()