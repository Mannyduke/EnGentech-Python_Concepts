def list_add():
    Lst1 = [8, 3, 9, 5]
    Lst2 = [2, 1, 4, 18]
    print("List1 =", Lst1)
    print("List2 =", Lst2)
    appended_list = Lst1 + Lst2
    print("Appended List =", appended_list)
    sum_appended = sum(appended_list)
    print("Sum Appended =", sum_appended)
    list_even_sorted(appended_list)
def list_even_sorted(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    even_numbers.sort()
    print("even & sorted: ", even_numbers)
list_add()
