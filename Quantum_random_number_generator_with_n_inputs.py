from projectq.ops import  H, Measure
from projectq import MainEngine
import binascii
"""
new qubit, Hadamard in superposition, measures the qubit to get a random 1 or 0. 
 
"""
def get(quantum):
    q = quantum.allocate_qubit()
    H | q
    Measure | q
    random = int(q)
    return random

# This list is used to store our random numbers
random = []

# initialises a new quantum backend

#Multiplied by 8 as bits make 1 ascii charecter
num=int(input())*8

#int(input("enter the no of bits you want to create, please enter digits over 12 so that you will get 4 digit numbers"))
# for loop to generate n random charecters in 1 and 0


new_list=[]
string=""
quantum = MainEngine()


for i in range(num):
    # calling the random number function and append the return to the list
    random.append(get(quantum))
# Flushes the quantum engine from memory
quantum.flush()

#printing random numbers in a list
#print(random_numbers_list,"\n")

#loop to convert the list into a string
for c in random:
    string+=str(c)


#printing the binary as a string

#the bellow code consists of conversion of bits into ascii with 8bits assigned per ascii
print(string)

n = 8
binary_values = string.split()

ascii_string = ""
for i in range(0, len(string), n):
    
    integer=int(string[i:i+n],2)
    ascii_char=chr(integer)
    ascii_string+=ascii_char
print(ascii_string)


#number refers to converting string into binary litrals

print(str(int(string,2)))
