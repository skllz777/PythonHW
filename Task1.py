# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X
#
# 5
# 1 2 3 4 5
# 3
# -> 1
num = int(input('Enter number of elements: '))
my_list = [0] * num
for i in range(len(my_list)):
    my_list[i] = int(input(f"Enter {i} element of list: "))
search_num = int(input("\nEnter number what you are finding: "))
while search_num not in my_list:
    search_num = int(input("There is no number in the list. Please type number again: "))
count = 0
for list in my_list:
    if list == search_num:
        count += 1
print(f"Number {search_num} meets {count} times")