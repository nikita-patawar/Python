#Accept list of no and return Count of even No

def main():
    print("Enter the number : ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = int(input("Enter Values: ")) 
        Data.append(Value)
    noarray = list(filter((lambda a: a%2==0 ),Data))
    print("Length of even no is",len(noarray))
main()