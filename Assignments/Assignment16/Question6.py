def checkNum(No):
    if(No > 0):
        print("No is Positive")
    elif(No < 0):
        print("No is Negative")  
    elif(No == 0):   
        print("No is 0" )   

def main():
   
   No = int(input("Enter a No: "))
   checkNum(No)

if __name__ == "__main__":
    main() 