def is_prime(n):
    if n <= 1:
        return False   # 0 and 1 are not prime
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def main():
   
   No = int(input("Enter a No: "))
   ret = is_prime(No)
   if is_prime(No):
        print("Prime number")
   else:
    print("Not a prime number")

if __name__ == "__main__":
    main() 