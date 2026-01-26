def Add(No1,No2):
    return No1 + No2
    

def main():
   
   No1 = int(input("Enter a No1: "))
   No2 = int(input("Enter a No2: "))
   Sum = Add(No1,No2)
   print("Addition is: ",Sum)

if __name__ == "__main__":
    main() 