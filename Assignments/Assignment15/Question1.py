

def main():
    print("Enter the number of elements: ")
    Size = int(input())

    Data = list()
    for i in range(Size):
        Value = int(input("Enter Values")) 
        Data.append(Value)
    Mdata = list(map((lambda a:a*a),Data)) 
    print(Mdata)

main()