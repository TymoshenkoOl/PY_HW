def qwerty(my_list):
    for i in my_list[:(len(my_list) + 1)]:
        if i[0] == 'a' or i[0] == 'A':
            new_list.append(i)
    return new_list


my_list = input('Enter list without commas: ').split(' ')
new_list = []
print(qwerty(my_list))
print()
