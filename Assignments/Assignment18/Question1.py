def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
    print(data) 
    Sum  = sum(data)
    print("Sum is",Sum)

def sum(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum

main()       