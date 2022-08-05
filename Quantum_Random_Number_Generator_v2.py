from projectq.ops import  H, Measure
from projectq import MainEngine
import binascii

def rando(number):
    random = []
    for i in range(number):
        quantum = MainEngine()
        q = quantum.allocate_qubit()
        H | q
        Measure | q
        random.append(int(q))
    lists=random.reverse()
    print(lists)
    string=""
    for c in random:
        string+=str(c)

    print(string)
    return numb(string)
   
def numb(string):
    print(str(int(string,2)))

rando(int(input("type your number")))
