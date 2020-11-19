'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import random
sm = 0
with open("task_5_5.txt", "w", encoding = 'utf-8') as myfile:
	myfile.write(f'{random.randint(1, 20)} {random.randint(1, 20)} {random.randint(1, 20)} {random.randint(1, 20)} {random.randint(1, 20)} {random.randint(1, 20)}')

with open("task_5_5.txt", "r") as myfile:
	 line = (myfile.read()).split()
for i in range(len(line)):
	sm = sm + int(line[i]) 
print(f'Сумма чисел в файле task_5_5.txt = {sm}')