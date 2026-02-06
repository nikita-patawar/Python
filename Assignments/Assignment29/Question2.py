
import os

def main():
    Name = input("Enter a File name ")
    if(os.path.exists(Name)):
         fobj=open(Name,"r")
         Data = fobj.read()
         print(Data)
       
    else:
        print("File not Present")    

if __name__ == "__main__":
    main() 