# Lambda function  return Even

CheckOdd = lambda No1 : No1 % 2 != 0

def main():
    
    No1 = int(input("Enter a No1: "))
    
    Ret = CheckOdd(No1)
    print(Ret)
if __name__ == "__main__":
    main()
