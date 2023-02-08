# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X
#
# 5
# 1 2 3 4 5
# 6
# -> 5
num = int(input('Enter number of elements: '))
my_list = [0] * num
for i in range(len(my_list)):
    my_list[i] = int(input(f"Enter {i} element of list: "))
what_num = int(input("\nEnter num for for search: "))
i = 0
while what_num == my_list[i]:
    i += 1
search_num = my_list[i]
for list in my_list:
    if list != what_num:
        if abs(list - what_num) < abs(search_num - what_num):
            search_num = list
print(f"Nearest number for num {what_num} is {search_num}")
