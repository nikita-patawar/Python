import threading

def Sum(data,result):
    Sum =0
    for n in data:
        Sum =Sum + n
        
    result["value"] =Sum

def Mul(data,result):
    mul =1
    for n in data:
        mul = mul * n
        
    result["value"] =mul

def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
        result= {}
        result2 ={}
    
    t1 = threading.Thread(target=Sum, args=(data,result))
    t2 = threading.Thread(target=Mul, args=(data,result2))  

    t1.start()
    t1.join() 

    t2.start()
    t2.join()

    print("Sum is: ",result["value"])
    print("Multiplication is: ",result2["value"])

if __name__ == "__main__":
    main()