my_dict_1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 44}
my_dict_2 = {11: 1, 2: 22, 33: 3, 4: 44, 5: 44}
keys_in_both_dicts = []
unique_keys_dict_1 = []
unique_items_dict_1 = {}
merged_dict = {}
for i in my_dict_1.keys():
    if i in my_dict_2:
        keys_in_both_dicts.append(i)
print('Спільні ключі в словниках: ', keys_in_both_dicts)
for k in my_dict_1.keys():
    if k not in my_dict_2:
        unique_keys_dict_1.append(k)
print('Унікальні ключі в словнику 1: ', unique_keys_dict_1)
for o in my_dict_1.items():
    if o not in my_dict_2.items():
        unique_items_dict_1.update({o})
print('Унікальні ключ та значення в словнику 1: ', unique_items_dict_1)
for p in my_dict_1:
    if p in my_dict_2:
        merged_dict.update([(p, [my_dict_1[p], my_dict_2[p]])])
    else:
        merged_dict.update([(p, my_dict_1[p])])
for q in my_dict_2:
    if q not in my_dict_1:
        merged_dict.update([(q, my_dict_2[q])])
print(merged_dict)
