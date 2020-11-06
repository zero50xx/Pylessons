# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, 
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
good = ()
good_dict = {}
my_good_list = []
a_l = []
b_l = []
c_l = []
d_l = []
new_dict = {}

for i in range(3):
	good_dict['название'] = input('Введите название товара: ')
	good_dict['цена'] = int(input('Введите цену товара: '))
	good_dict['количество'] = int(input('Введите количество товара: '))
	good_dict['ед'] = input('Введите единицу измерения количества товара: ')
	if i == 0:
		a = good_dict.copy()
		good = (i + 1, a)
	elif i == 1:
		b = good_dict.copy()
		good = (i + 1, b)
	elif i == 2:
		c = good_dict.copy()
		good = (i + 1, c)
	my_good_list.append(good)

print(my_good_list)


for z in range(3):
	for i,j in my_good_list[z][1].items():
		if i == 'название':
			a_l.append(j)
			if z == 2:
				new_dict[i] = a_l
		if i == 'цена':
			b_l.append(j)
			if z == 2:
				new_dict[i] = b_l
		if i == 'количество':
			c_l.append(j)
			if z == 2:
				new_dict[i] = c_l
		if i == 'ед':
			d_l.append(j)
			if z == 2:
				new_dict[i] = d_l


print(new_dict)