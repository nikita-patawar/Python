'''
Write a program to display value,type,memory address

'''

a = 10
b = 10

print(a)
print(type(a))
print(id(a))

'''
What is difference between a = 10 & b = 10 also a=[10] & b= [10]

Ans:   Python stores 10 in memory and both a and b point to the same object is id will print same memory address
      for a = [10] & b=[10] it is list . list is mutable so it will print different memory address.

'''
print(id(a), id(b))


'''
Write a program to accept the two numbers and perform addition, substraction, multiplication and didvision
'''
print("Enter a no1")
No1 = int(input())
print("Enter a no2")
No2 = int(input())
Addition = No1 + No2
print("Addition of the number is",Addition)
substraction = No1 - No2
print("substraction of the number is",substraction)
multiplication = No1 * No2
print("multiplication of the number is",multiplication)
division = No1 / No2
print("division of the number is",division)


'''
Write a program to take user's name and age and display
'''

print("Enter a Name")
Name = input()
print("Enter a Age")
Age =  int(input())

print("Hello ",Name,"you will turn",Age + 1, "next year")



