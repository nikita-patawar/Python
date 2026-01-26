def Pattern(No):
    for i in range(No,0,-1):
       print("*"*i)

def main(): 
   No = int(input("Enter a No: "))
   Pattern(No)
if __name__ == "__main__":
    main() 