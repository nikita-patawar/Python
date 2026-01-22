def Areaofrectangele(l,b):
    return l*b
def main():
    l = int(input("Enter a length: "))
    b = int(input("Enter a width: "))
    Area = Areaofrectangele(l,b)
    print("Area of rectangle :  ",Area)


if __name__ == "__main__":
    main() 