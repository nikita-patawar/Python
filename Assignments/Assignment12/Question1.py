# Check Character Vowel of not
v = ['a','e','i','o','u','A','E','I','O','U']
def CheckVowel(char):
    if char in v:
        print("Character is a vowel")
    else:
        print("Character is NOT a vowel")        
def main():
    char = (input("Enter a Character: "))
    CheckVowel(char)


if __name__ == "__main__":
    main()       

