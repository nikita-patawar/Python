import threading

def SumOfEven(numList):
    sum=0
    for i in numList:
        if(i %2 ==0):
            sum =sum + i

    print("Sun of even factres: ",sum) 

def SumOfOdd(numList):
    sum=0
    for i in numList:
        if(i %2!=0):
            sum =sum + i

    print("Sun of Odd factres: ",sum)  

def main():
    Arraylist = [1,2,3,4,5,]
    t1 = threading.Thread(target=SumOfEven,args=(Arraylist,))
    t2 = threading.Thread(target=SumOfOdd,args=(Arraylist,))  

    t1.start()
    t2.start()

    t1.join() 
    t2.join()

if __name__ == "__main__":
    main()                                  
