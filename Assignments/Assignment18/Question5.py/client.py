import module

def SumofList(data):
    total =0
    for num in data:
        total+=num
    return total    

def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        if module.is_prime(value):
            data.append(value)
    total = SumofList(data)   
    print("Sum is: ",total) 
    Sum  = module.is_prime(data)
    print("Sum is",Sum)

main()    