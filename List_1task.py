from random import randint
list = [randint(0, 500) for i in range (30)]
for i in list:
    if i >= 100:
        print(i, end=' ')