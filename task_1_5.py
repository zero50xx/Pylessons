'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
with open('Task_1_5.txt', 'w+', encoding='utf-8') as f_obj:
	while  True:
		fw = input('Введите строку для записи в файл: ')
		if fw != '':
			f_obj.write(fw + '\n')
		else:
			break