import threading

def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

def Check_prime(numList):
    data = []
    for i in numList:
        if is_prime(i):
            data.append(i)
    print("Prime No:", data)

def Check_nonprime(numList):
    data = []
    for i in numList:
        if not is_prime(i):
            data.append(i)
    print("Non Prime No:", data)

def main():
    Arraylist = [1, 2, 3, 4, 5]
    
    t1 = threading.Thread(target=Check_prime, args=(Arraylist,))
    t2 = threading.Thread(target=Check_nonprime, args=(Arraylist,))  

    t1.start()
    t2.start()

    t1.join() 
    t2.join()

if __name__ == "__main__":
    main()
   

                                 
