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
        quantum.flush()
        random.append(int(q))
    lists=random.reverse()
    string=""
    for c in random:
        string+=str(c)

    return numb(string)
   
def numb(string):
    if (int(string,2)) > 999 and (int(string,2)) < 10000 :
        print(int(string,2))
    else:
        return rando(21)

rando(21)
