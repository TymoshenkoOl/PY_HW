class_1 = int(input('Кількість учнів в класі 1: '))
class_2 = int(input('Кількість учнів в класі 2: '))
class_3 = int(input('Кількість учнів в класі 3: '))
if class_1 % 2 == 0:
    desk_for_class_1 = (class_1 // 2)
if not class_1 % 2 == 0:
    desk_for_class_1 = (class_1 // 2 + 1)
if class_2 % 2 == 0:
    desk_for_class_2 = (class_2 // 2)
if not class_2 % 2 == 0:
    desk_for_class_2 = (class_2 // 2 + 1)
if class_3 % 2 == 0:
    desk_for_class_3 = (class_3 // 2)
if class_3 % 2 != 0:
    desk_for_class_3 = (class_3 // 2 + 1)
print(f'Необхідна кількість парт: {desk_for_class_1 + desk_for_class_2 + desk_for_class_3}')

