def qwerty(my_list):
    n = 0
    for i in my_list[n:(len(my_list) + 1)]:
        if n % 2 == 0:
            new_list.append(i[::-1])
        else:
            new_list.append(i)
            n += 2
    return new_list


my_list = input('Enter a list separated by commas: ').split(', ')
new_list = []
print(qwerty(my_list))
print()