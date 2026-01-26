import threading

def Max_no(data):
    Max_No = data[0]
    for n in data:
        if n > Max_No:
            Max_No = n
    print("Max No:", Max_No)


def Min_no(data):
    Min_No = data[0]
    for n in data:
        if n < Min_No:
            Min_No = n
    print("Min No:", Min_No)



def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
    
    t1 = threading.Thread(target=Max_no, args=(data,))
    t2 = threading.Thread(target=Min_no, args=(data,))  

    t1.start()
    t2.start()

    t1.join() 
    t2.join()

if __name__ == "__main__":
    main()