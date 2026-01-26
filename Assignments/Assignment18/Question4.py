def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
    Value = int(input("Enter a value to find count"))    
    ret  = Count(data,Value)
    print(f"Count of{Value} is",ret)

def Count(data,Value):
    Count = 0
    for n in data:
        if n == Value:
            Count=Count+1
    return Count

main() 