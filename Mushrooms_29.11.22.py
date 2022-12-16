mushrooms = int(input('Введіть кількість грибів: '))
if mushrooms % 9 == 0 or mushrooms % 8 == 0 or \
        mushrooms % 7 == 0 or mushrooms % 6 == 0 or mushrooms % 5 == 0 or mushrooms == 0:
    ending = 'ів'
elif mushrooms % 4 == 0 or mushrooms % 3 == 0 or mushrooms % 2 == 0:
    ending = 'a'
else:
    ending = ''
print(f'Марійка знайшла в лісі {mushrooms} гриб{ending}')