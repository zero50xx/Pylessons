'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.sort(reverse = True)
    return int(my_list[0]) + int(my_list[1])


print(my_func(x = input('Введите 1е число: '), y = input('Введите 2е число: '), z = input('Введите 3е число: ')))   # дабы не перегружать данную строку int'ами я их убрал в return ф-ции
