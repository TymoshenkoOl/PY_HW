my_str = input('Введите строку: ')
my_list = list(my_str)
print(my_list)
unique_list = []
for i in my_list:
    if my_list.count(i) == 1:
        unique_list.append(i)
print(unique_list)