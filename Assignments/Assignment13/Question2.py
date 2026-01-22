def AreaofCircle(r):
    return 3.14*r*r
def main():
    r = int(input("Enter a radius: "))
   
    Area = AreaofCircle(r)
    print("Area of Circle is :  ",Area)


if __name__ == "__main__":
    main() 