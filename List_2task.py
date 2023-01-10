my_list = [3, 34, 646, 24, 64, 23, 46, 686, 1, 2]
n = len(my_list)
if n < 2:
    my_list.append(0)
else:
    my_list.append(my_list[n - 1] + my_list[n - 2])
print(my_list)
