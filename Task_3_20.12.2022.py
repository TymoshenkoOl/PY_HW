# Создать список my_result в который вначале поместить элементы на четных местах из
# my_list_1, а потом все элементы на нечетных местах из my_list_2

my_list_1 = [0, 1, 3, 5, 7]
my_list_2 = [2, 4, 6, 34]
result = []
odd_index = even_index = 0
dif_len = len(my_list_1) - len(my_list_2)
if dif_len > 0:
    del my_list_1[(len(my_list_1) - dif_len):len(my_list_1)]
elif dif_len < 0:
    del my_list_2[(len(my_list_2) + dif_len + 1):len(my_list_2)]
result_len = len(my_list_1) + len(my_list_2)
for i in range(result_len):
    if i % 2 == 0:
        result.append(my_list_2[odd_index])
        odd_index += 1
    else:
        result.append(my_list_1[even_index])
        even_index += 1
print(result)
print()


my_list_1 = [0, 1, 3, 5, 7, 9, 14, 1]
my_list_2 = [2, 4, 6, 8, 10, 12]
result = my_list_1[1::2] + my_list_2[0::2]
print(result)
