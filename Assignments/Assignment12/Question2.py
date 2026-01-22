def find_factors(num):
    print(f"The factors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

number = int(input("Enter a number to find its factors: "))
find_factors(number)