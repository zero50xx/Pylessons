'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
'''

a = []

words = [
		['One', 'Один'],
		['Two', 'Два'],
		['Three', 'Три'],
		['Four', 'Четыре'],
]
with open("task_4_5.txt", "r") as myfile:
	lines = myfile.readlines()
	for i in range(len(lines)):
	 	a.append(lines[i].split())
	 	if a[i][0] == words[i][0]:
	 		a[i][2] = words[i][1]
with open("task_4_5_1.txt", "w", encoding = 'utf-8') as myfile:
	for i in range(len(a)):
		myfile.write(f'{a[i][0]} - {a[i][2]}\n')
