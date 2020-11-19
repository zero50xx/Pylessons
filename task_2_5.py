'''
 		Создать текстовый файл (не программно), сохранить в нем несколько строк,
 		выполнить подсчет количества строк, количества слов в каждой строке.
'''
import random
with open("task_2_5.txt", "a") as myfile:
	for i in range(random.randint(1, 20)):
		myfile.write(f'Строка номер {i} и плюшка в виде рандомного числа {random.randint(23, 193)}\n')
with open("task_2_5.txt", "r") as myfile:
	 lines = myfile.readlines() 
	 print(f'Строк в файле - {len(lines)}')
	 for i in range(len(lines)):
	 	print(f'Слов в строке номер {i+1} --- {len(lines[i].split())} ')


