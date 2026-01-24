# Lambda function  return Even

CheckEven = lambda No1 : No1 % 2 == 0

def main():
    
    No1 = int(input("Enter a No1: "))
    
    Ret = CheckEven(No1)
    print(Ret)
if __name__ == "__main__":
    main()
