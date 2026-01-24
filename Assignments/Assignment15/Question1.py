def Square(No):
    return No * No

def main():
    print("Enter the number of elements: ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = int(input("Enter Values")) 
        Data.append(Value)
    Mdata = list(map(Square,Data) ) 
    print(Mdata)

main()