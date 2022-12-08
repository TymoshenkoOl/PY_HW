print("дії з числами: \n"
      "'+' - додавання\n"
      "'-' - віднімання\n"
      "'*' - множення\n"
      "'/' - ділення\n"
      "'^' - піднесення  до степеня")
print()
first_digit = float(input('Введіть перше число: '))
second_digit = float(input('Введіть перше число: '))
action = input('Введіть дію: ')
if '+' in str(action):
    result = first_digit + second_digit
    print(result)
elif '-' in str(action):
    result = first_digit - second_digit
    print(result)
elif '*' in str(action):
    result = first_digit * second_digit
    print(result)
elif '/' in str(action):
    result = first_digit / second_digit
    print(result)
elif '^' in str(action):
    result = first_digit ** second_digit
    print(result)
else:
    print('В наступних версіях буде більше функцій, а поки оберіть дію з нявних у списку')
