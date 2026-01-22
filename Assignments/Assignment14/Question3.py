# Lambda function  return large

CheckGreater = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    
    No1 = int(input("Enter a No1: "))
    No2 = int(input("Enter a No2: "))
    Ret = CheckGreater(No1,No2)
    print(Ret,"is greater")    

if __name__ == "__main__":
    main()
