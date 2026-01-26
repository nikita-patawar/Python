from functools import reduce

def is_prime(n):
    if n <= 1:
        return False   # 0 and 1 are not prime
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
        
    Fdata = list(filter(is_prime,data))
    print("Fdata: ",Fdata)
    mdata = list(map(lambda a: a*2,Fdata))
    print("Mdata: ",mdata)
    Sum = reduce((lambda A,B:A if A>B else B),mdata)
    print(Sum)
main() 