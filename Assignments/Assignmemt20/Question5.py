import threading

def printdigits(num):
    for i in range(1,num+1):
        print(i)


def printreversedigits(num):
    for i in range(num,0,-1):
        print(i)   

def main():
    No = int(input("Enter a No"))
    t1 = threading.Thread(target=printdigits,args=(No,))
    t2 = threading.Thread(target=printreversedigits,args=(No,))     

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()     

