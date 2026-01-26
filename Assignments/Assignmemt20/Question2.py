import threading

def SumOfEvenFactores(num):
    sum=0
    for i in range(1,num+1):
        if(num % i == 0 and i %2 ==0):
            sum =sum + i

    print("Sun of even factres: ",sum) 

def SumOfOddFactores(num):
    sum=0
    for i in range(1,num+1):
        if(num % i == 0 and i %2!=0):
            sum =sum + i

    print("Sun of Odd factres: ",sum)  

def main():
    val = int(input("Enter a no:"))
    t1 = threading.Thread(target=SumOfEvenFactores,args=(val,))
    t2 = threading.Thread(target=SumOfOddFactores,args=(val,))  

    t1.start()
    t2.start()

    t1.join() 
    t2.join()

if __name__ == "__main__":
    main()                                  
