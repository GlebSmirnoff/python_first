def func_outer():
    x = 2
    print('x ravno', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальное сменилось на', x)


func_outer()