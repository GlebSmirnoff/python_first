x = 50

def func():
    global x

    print('x равен', x)
    x = 2
    print('заменяем глобальное значение х на', x)

func()
print('Значение х состовляет', x)