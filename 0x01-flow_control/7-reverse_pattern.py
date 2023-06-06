def print_reverse_pattern(number):
    for i in range(number, 0, -1):
        for a in range(i, 0, -1):
            print(a, end=' ')
        print()
num = int(input("Enter a number: "))
print_reverse_pattern(num)