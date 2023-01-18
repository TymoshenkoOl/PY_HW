persons = [{"name": "John", "age": 17}, {"name": "Ivan_ІV", "age": 15}, {"name": "Kolia", "age": 15},
           {"name": "Ibrahim", "age": 55}, {"name": "Oleh", "age": 35}]
list_longest_name = []
list_youngest_person = []
list_av_age = []
min_age = None
max_len_name = 0
av_age = 0
for i in range(len(persons)):
    if min_age is None:
        min_age = persons[i]['age']
    if persons[i]['age'] < min_age:
        min_age = persons[i]['age']
for i in range(len(persons)):
    if persons[i]['age'] == min_age:
        list_youngest_person.append(persons[i]['name'])
for k in range(len(persons)):
    if len(persons[k]['name']) > max_len_name:
        max_len_name = len(persons[k]['name'])
for k in range(len(persons)):
    if len(persons[k]['name']) == max_len_name:
        list_longest_name.append(persons[k]['name'])
for o in range(len(persons)):
    av_age = (persons[o]['age']) + av_age
av_age = av_age / (o + 1)
print('Наймолодші люди: ', list_youngest_person)
print('Найдовші імена в: ', list_longest_name)
print('Середній вік людей: ', av_age)
