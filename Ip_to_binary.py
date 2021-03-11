import socket
listA=[]
host=input("enter your domain to print ip and its equalent binary format\n")
system = socket.gethostbyname(host) #gets the ip adress of the host
print(system) #prints ip adress
new_system=system.split(".") #splitting the ip adress into list such as 145.156.1.14 to ["145","156","1","14"]
for i in range(len(new_system)):
    listA.append(bin(int(new_system[i])).replace("0b", "")) 
		
		'''conversion of data from charecters iin the list to binary format'''
    if len(new_system)-1==i:
		
		'''to check if the bits charecters are the last of the list'''
        print(listA[i].zfill(8)) 
		
		'''.zipfill(8) is used to complete bites from any number to 8 bits binary number, like if a binary data is 1001, this converts it onto 00001001'''
    else:
        print(listA[i].zfill(8),end=".")
