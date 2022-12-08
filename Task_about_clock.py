number_of_seconds = int(input('Введіть кількість секунд: '))
if number_of_seconds >= 86400:  # якщо відлік не обнулився з якихось причин опівночі
    seconds_after_noon = number_of_seconds % 86400
    hours = seconds_after_noon // 3600
    minutes = int((seconds_after_noon / 3600 - hours) * 60)
    seconds = int(round((seconds_after_noon / 60 - seconds_after_noon // 60) * 60))
if number_of_seconds < 86400:
    seconds_after_noon = number_of_seconds
    hours = (seconds_after_noon // 3600)
    minutes = int((seconds_after_noon / 3600 - hours) * 60)
    seconds = int(round((seconds_after_noon / 60 - seconds_after_noon // 60) * 60))
print(f'Місцевий час: {hours}:{minutes}:{seconds}')
