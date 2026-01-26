def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
    ret  = Min_no(data)
    print("Min No is",ret)

def Min_no(data):
    Min_No = data[0]
    for n in data:
        if n < Min_No:
            Min_No = n
    return Min_No

main() 