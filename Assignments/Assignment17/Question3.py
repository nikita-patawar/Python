def Fact(No):
    fact = 1
    for i in range(1,No+1,1):
        fact = fact * i
    return fact

def main():
   
   No = int(input("Enter a No: "))
   ret = Fact(No)
   print("facorial of ",No,"is",ret)

if __name__ == "__main__":
    main() 