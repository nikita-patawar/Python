def Pattern(No):
    for i in range(1,No):
       for j in range(1,No +1):
            print(j ,end =" ")
       print()    

def main(): 
   No = int(input("Enter a No: "))
   Pattern(No)
if __name__ == "__main__":
    main() 



# or

# No = 5
# nums = list(range(1,No+1))
# for i in range(No):
#     print(nums)
