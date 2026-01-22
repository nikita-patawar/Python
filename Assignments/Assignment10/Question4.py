# Print Even of No

def Even(No):
    fact = 1
    for i in range(2,No+1,2):
        print(i)
    

def main():
    No = int(input("Enter a No: "))
    Even(No)
    


if __name__ == "__main__":
    main() 