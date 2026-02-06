
import os

def main():
    Name = input("Enter a File name ")
    if(os.path.exists(Name)):
        print("File Present")
    else:
        print("File not Present")    

if __name__ == "__main__":
    main() 