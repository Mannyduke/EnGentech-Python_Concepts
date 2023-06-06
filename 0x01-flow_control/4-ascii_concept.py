def check(char):
    while True:
        if len(char) != 1:
            print("Not more than one character at a time, try again")
            char = input("Enter a single character: ")
            continue

        if not char.isalpha():
            print("Non-alphabetical character is not allowed, please try again")
            char = input("Enter a single character: ")
            continue

        if ord('a') <= ord(char) <= ord('z'):
            return f"The input {char} is a lower case character"
        else:
            return f"The input {char} is an upper case character"
print(check("a"))
print(check("G"))