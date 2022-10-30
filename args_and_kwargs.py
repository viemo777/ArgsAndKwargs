def ten_percent_of_product(x, y):
    return (x * y) * 0.1


result = ten_percent_of_product(10, 20)
print(result)


def ten_percent_of_product_with_args(*args):
    prod = 1
    for number in args:
        prod = prod * number
    return prod


print(ten_percent_of_product_with_args(1, 4, 5, 1.5))


def percent_of_product_with_args(percent, *args):
    prod = 1
    for number in args:
        prod = prod * number
    return prod / 100 * percent


print(percent_of_product_with_args(3, 1, 4, 3))


def func_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print('Hello, {}!'.format(kwargs['name']))
    else:
        print('What is your name?')


func_with_kwargs(age=14, name='Vitalii')


def func_with_param_and_kwargs(greening, **kwargs):
    if 'name' in kwargs:
        print('{}, {}!'.format(greening, kwargs['name']))
    else:
        print('{}. What is your name?'.format(greening))


func_with_param_and_kwargs('Hi', age=14, name='Vitalii')

