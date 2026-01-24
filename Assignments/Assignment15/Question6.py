#Accept list of nos and return Mimimum No
from functools import reduce


def main():
    print("Enter the number of elements: ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = int(input("Enter Values: ")) 
        Data.append(Value)
    Minimum = reduce((lambda a,b: a if a<b else b),Data)
    print(Minimum)
main()