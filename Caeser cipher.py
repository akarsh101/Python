#output will be
#enter the elemesnts u want to change
#akarsh(user input)
#Enter Your head alphabet
#b(userinput)
#       blbsti

output= []
name = input("enter the elemesnts u want to change\n")
key= input('Enter Your head alphabet\n')[0]
number_key= [ord(key) - 96 for key in key]
number_name = [ord(name) - 96 for name in name]
sub=[x - number_key[0] for x in number_name]
if ((name.isupper())and(key.isupper())):
    for n in number_key:
        n=n
    for num in sub:
        if num >= 0:
            num=(num+(n*2))
        else:
            num=((num*-1)+1)
        output.append(chr(ord('`')+num))
    ended=''.join([str(elem) for elem in output])
elif ((name.islower())and(key.islower())):
    for n in number_key:
        n=n
       
    for num in sub:
        if num >= 0:
            num=((num+(n*2))-1)
        else:
            num=((num*-1)+1)
        output.append(chr(ord('`')+num))
    ended=''.join([str(elem) for elem in output])
    print("\t", ended)
else:
    print("error in the input or in the key or the name\n please check and try again")
