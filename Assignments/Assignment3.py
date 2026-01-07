# questtion1

def multiplication(parameter1, parameter2):
    return parameter1*parameter2

Ans = multiplication(2,3)  
print(Ans)  

# Function with parameter function without parameter

def ShowMessage(message):
    print(message)

ShowMessage("Hello Nikita")    

def returnMessage():
    return "Hello Nikita"

print(returnMessage())  


#Write a program to disply data type, memory address, Size in bytes value enteed by user
from sys import getsizeof
print("Enter a Name")
Name = input()
print(type(Name))
print(id(Name))
print(getsizeof(Name))


# predict the output

a=5
print(type(a))  # <class 'int'>
a=5.0
print(type(a))  # <class 'float'>  
a="python"
print(type(a))  # <class 'str'>

#. python is dynamically typed language


s = "hello"
s = s + " world" 
print (s)




