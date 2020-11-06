# Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.


my_monthes_list = [{12, 1, 2}, 'зима', {3, 4, 5}, 'весна', {6, 7, 8}, 'лето', {9, 10, 11}, 'осень']
num = int(input('Введите номер месяца: '))

for i in range(len(my_monthes_list)):
	if (type(my_monthes_list[i]) == set) and (num in my_monthes_list[i]):
		print(f'Данный месяц относится к времени года {my_monthes_list[i + 1]}')
		break


number_of_monthes_list = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
my_monthes_dict = {number_of_monthes_list[0] : 'зима', number_of_monthes_list[1] : 'весна', number_of_monthes_list[2] : 'лето', number_of_monthes_list[3] : 'осень'}
num = int(input('Введите номер месяца: '))

for i in range(len(my_monthes_dict)):
	if num in number_of_monthes_list[i]:
		print(f'Данный месяц относится к времени года {my_monthes_dict[number_of_monthes_list[i]]}')
		break

