def qwerty(my_list):
    for i in my_list[:(len(my_list) + 1)]:
        try:
            i = int(i)
        except:
            new_list.append(i)
            continue
    return new_list


my_list = input('Enter list with str and int without commas: ').split(' ')
new_list = []
print(qwerty(my_list))
print()
