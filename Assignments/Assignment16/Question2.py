def checkNum(No):
    if(No % 2 == 0):
        print("No is even")
    else:
        print("No is Odd")    

def main():
   
   No = int(input("Enter a No: "))
   checkNum(No)

if __name__ == "__main__":
    main() 