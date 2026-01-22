Numbers = (input("value: "))
listNumber = list(Numbers)
rev = ""
for i in range(len(listNumber)-1,-1,-1):
    rev = rev + listNumber[i]
    
if(int(Numbers) == int(rev)):
    print(Numbers," is palindrome")
else:
    print("Number is not palindrome")    