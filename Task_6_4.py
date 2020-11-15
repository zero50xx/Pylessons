'''
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''
import sys
import time
from itertools import count, cycle
k=0
argv = sys.argv[1:]
if 'h' in argv or 'help' in argv:
    print('Как работает наша программа. \nВведите в качестве аргумента "а" или "б"\n'
          'а) итератор, генерирующий целые числа, начиная с указанного\n'
          'б) итератор, повторяющий элементы некоторого списка, определенного заранее.')
if len(argv) == 1:
    if argv[0] == 'a':
        a = int(input('Введите начальное значение цикла: '))
        for i in count(start = a, step = 1):
            print(i)
            if i == a + 25:
                break
    elif argv[0] == 'b':
        b_list = [i for i in range(100) if i % 5 == 0]
        print(b_list)
        for bs in cycle(b_list):
            k+=1
            print(bs)
            time.sleep(1)
            if k >= len(b_list) * 2:
                break
            
        
