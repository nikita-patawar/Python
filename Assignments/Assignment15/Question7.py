#Accept list of string and return length  > 5 No string
from functools import reduce


def main():
    print("Enter the number of words: ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = (input("Enter Values: ")) 
        Data.append(Value)
    strarray = list(filter((lambda a: len(a) > 5),Data))
    print(strarray)
main()