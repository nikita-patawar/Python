# Lambda function  return Multiplication

LargeNo = lambda No1,No2,No3 : No1  if (No1>No2 and No1>No3)  else (No2 if(No2>No3) else No3)

def main():
    
    No1 = int(input("Enter a No1: "))
    No2 = int(input("Enter a No2: "))
    No3 = int(input("Enter a No3: "))
    Ret = LargeNo(No1,No2,No3)
    print("Large No is",Ret)  
    #large = (lambda No1,No2:  No1 if No1 > No2 else No2 ) 
    #large2 =  lambda large,No3:  large if large > No3 else No3  
    # ret=large(No1,No2)
    # print(large2(ret,No3))

if __name__ == "__main__":
    main()