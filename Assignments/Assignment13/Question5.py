def DefineGrade(marks):
    if(marks>=75):
        print("Distinction")
    elif(marks >= 60):
        print("First class")
    elif(marks >= 50):
        print("First class")
    else:
        print("Fail")            
def main():
    m = int(input("Enter a Marks: "))
    DefineGrade(m)


if __name__ == "__main__":
    main() 