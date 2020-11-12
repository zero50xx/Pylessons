'''
    Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def f(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    

x = int(input('Введите делимое: '))
y = int(input('Введите делитель: '))
print(f'Результат деления {x} на {y} = {f(x, y)}' if f(x, y) != 'ZeroDivisionError' else 'ZeroDivisionError' )
