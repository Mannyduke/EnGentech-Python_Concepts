def print_hash_shape(number):
    for i in range(1, number + 1):
        print('#' * i)
while True:
    user_input = input("Enter an integer: ")
    if user_input.isdigit():
        num = int(user_input)
        print_hash_shape(num)
        break
    else:
        print("Only integer characters are allowed. Please try again")