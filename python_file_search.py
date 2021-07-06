import string
import os
li = []  
  
li = list(string.ascii_uppercase)
print("1. choose starts with case to find the file \n2. choose ends with case to find the file like .exe or so on \n3.exit")
choice=int(input("choose 1 or 2\n"))
if choice == 1:
    filename=input("starts with file name \n")
      
    for i in range(len(li)):
        dp=li[i]+":\\"
        for root, dirs, files in os.walk(dp):
            for file in files:
                if file.startswith(filename):
                  print (root+"\\"+str(file)+"\n")
elif choice == 2:
    filename=input("ends with file name \n")
      
    for i in range(len(li)):
        dp=li[i]+":\\"
        for root, dirs, files in os.walk(dp):
            for file in files:
                if file.startswith(filename):
                  print (root+"\\"+str(file)+"\n")

else:
    exit()

