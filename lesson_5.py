# Обзор функций
name = 'Pavel'


def hello(name):  # параметр
    print('Hello there ', name)


hello(name)  # аргументы


def sum_nums_with_print(a, b):
    sum = a + b
    print(sum)
    return sum


def sum_nums_without_print(a, b):
    sum = a + b
    return sum


sum_nums_with_print(243, 534)


sum_of_something = sum_nums_without_print(2132, 4123)
print(sum_of_something)


print(sum_nums_without_print(sum_nums_without_print(
    12, 77), sum_nums_without_print(134, 244353)), " last print")
