# Numbers = (input("value: "))

# rev = ""

# for digit in Numbers:
#     rev =  digit + rev
# print (int(rev))
 

Numbers = (input("value: "))
listNumber = list(Numbers)
rev = ""
for i in range(len(listNumber)-1,-1,-1):
    rev = rev + listNumber[i]
    
print(rev)



    
