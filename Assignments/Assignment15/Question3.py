def FilterEven(No):
    return No % 2 != 0

def main():
    print("Enter the number of elements: ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = int(input("Enter Values: ")) 
        Data.append(Value)
    Mdata = list(filter(FilterEven,Data) ) 
    print(Mdata)

main()