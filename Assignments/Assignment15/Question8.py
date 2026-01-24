#Accept list of no and return no  Dovisible by 3 and 5

def main():
    print("Enter the number : ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = int(input("Enter Values: ")) 
        Data.append(Value)
    noarray = list(filter((lambda a: (a%3 == 0 and a%5 ==0) ),Data))
    print(noarray)
main()