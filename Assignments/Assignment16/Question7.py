def checkNumDivisibleBy5(No):
     return (No % 5 == 0)
   

def main():
   
   No = int(input("Enter a No: "))
   ret = checkNumDivisibleBy5(No)
   print(ret) 
if __name__ == "__main__":
    main() 