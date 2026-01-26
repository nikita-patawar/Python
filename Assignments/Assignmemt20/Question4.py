import threading

def SmallCase(string):
    count = 0
    for i in string:
        if i.islower():
            count = count +1
    print(f"Number of samll case digit is {count}")

def CapitalCase(string):
    count = 0
    for i in string:
        if i.isupper():
            count = count +1
    print(f"Number of capital case digit is {count}")     


def Digits(string):
    count = 0
    for i in string:
        if i.isdigit():
            count = count +1
    print(f"Number of digit is {count}")

def main():
    str = input("Enter a string")
    t1 = threading.Thread(target=SmallCase,args=(str,))
    t2 = threading.Thread(target=CapitalCase,args=(str,))     
    t3 = threading.Thread(target=Digits,args=(str,)) 

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()     

