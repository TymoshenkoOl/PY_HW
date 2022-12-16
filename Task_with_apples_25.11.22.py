number_of_apples = float(input("Введіть кількість яблуk: "))  # припустимо, що в корзині може бути не ціле яблуко
number_of_pupils = int(input("Введіть кількість учнів: "))
apples_per_pupil = int(number_of_apples // number_of_pupils)
apples_in_a_basket = round(number_of_apples % number_of_pupils, 2)
print(f'Кількість яблук на одного учня: {apples_per_pupil}')
print(f'Залишок яблук в корзині: {apples_in_a_basket}')
