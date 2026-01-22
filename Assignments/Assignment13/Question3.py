#Perfect No

def PerfectNo(No):
    Sum_Divisor = 0
    for i in range(1,No):
        if No % i == 0:
            Sum_Divisor = Sum_Divisor + i
    return Sum_Divisor == No        



def main():
    No = int(input("Enter a No: "))
    ret = PerfectNo(No)

    if(ret):
        print("Number is perfect ")
    else:
        print("Number is not perfect no")

if __name__ == "__main__":
    main() 