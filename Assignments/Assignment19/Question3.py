from functools import reduce

def main():
    number = int(input("Enter a numbers of list: "))
    data = list()
    for i in range(number):
        value = int(input("Enter a value: "))
        data.append(value)
    Fdata = list(filter((lambda a: a>=70 and a<90),data))
    print("Fdata: ",Fdata)
    mdata = list(map(lambda a: a+10,Fdata))
    print("Mdata: ",mdata)
    Sum = reduce((lambda A,B:A*B),mdata)
    print(Sum)
main() 