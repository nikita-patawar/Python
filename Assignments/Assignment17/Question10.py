def Sum_of_digits(No):
    Sum = 0
    for i in No:
        Sum = Sum + int(i)
    return Sum


def main():
    No = input("Enter No; ")
    Ret=Sum_of_digits(No)
    print(Ret)

main()    
