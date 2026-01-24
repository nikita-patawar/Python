# Lambda function  return Divisible 5

CheckDivisible = lambda No1 : No1 % 5 == 0

def main():
    
    No1 = int(input("Enter a No1: "))
    
    Ret = CheckDivisible(No1)
    print(Ret)
if __name__ == "__main__":
    main()
