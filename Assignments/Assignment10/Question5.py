# Print odd of No

def Odd(No):
    fact = 1
    for i in range(1,No+1,2):
        print(i)
    

def main():
    No = int(input("Enter a No: "))
    Odd(No)

if __name__ == "__main__":
    main() 