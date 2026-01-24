# Lambda function  return Multiplication

Multiplication = lambda No1,No2 : No1 * No2

def main():
    
    No1 = int(input("Enter a No1: "))
    No2 = int(input("Enter a No2: "))
    Ret = Multiplication(No1,No2)
    print("Multiplication is",Ret)    

if __name__ == "__main__":
    main()