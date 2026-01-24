#Accept list of nos and return addition
from functools import reduce


def main():
    print("Enter the number of elements: ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = int(input("Enter Values: ")) 
        Data.append(Value)
    Sum = reduce((lambda A,B:A+B),Data)
    print(Sum)

main()