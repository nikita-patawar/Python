def DivisorsSum(No):
    Sum = 0
    for i in range(1,No,1):
        if(No % i == 0):
            Sum = Sum + i 
    return Sum

def main():
   
   No = int(input("Enter a No: "))
   ret = DivisorsSum(No)
   print("Divisors Sum  of ",No,"is",ret)

if __name__ == "__main__":
    main() 