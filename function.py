
def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

printMax(3, 4)

x = 5
y = 7

printMax(x, y)





x = 50

def func(x):
    print('x равен', x)
    x = 2   # локальная переменная
    print('замена локального х на', x)

func(x)
print('х по-прежнему', x)


