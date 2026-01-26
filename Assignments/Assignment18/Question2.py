def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
    ret  = Max_no(data)
    print("Large No is",ret)

def Max_no(data):
    Max_No = data[0]
    for n in data:
        if n > Max_No:
            Max_No = n
    return Max_No

main() 