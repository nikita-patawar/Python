def Pattern(No):
    for i in range(1,No+2,1):
       for j in range(1,i):
            print(j ,end =" ")
       print()    

def main(): 
   No = int(input("Enter a No: "))
   Pattern(No)
if __name__ == "__main__":
    main() 