from functools import reduce

def main():
    print("Enter the number : ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        value = int(input("Enter a Value"))
        Data.append(value)
    
    Multiplication = reduce((lambda a,b:a *b),Data)
    print(Multiplication)

main()    
    