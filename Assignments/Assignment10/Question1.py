# Print table of entered no

def DisplayTable(No):
    for i in range(1,11):
        print(No*i)

def main():
    No = int(input("Enter a No: "))
    DisplayTable(No)


if __name__ == "__main__":
    main()   

