'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и 
премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
	def __init__(self, name, surname, position, _income):
		self.nam = name
		self.sur = surname
		self.pos = position
		self._incc = _income

class Position(Worker):
	def get_full_name(self):
		return self.nam +' '+ self.sur
	def get_total_income(self):
		return self._incc['wage'] + self._incc['bonus']
	def get_full_info(self):
		return [f'Должность: {self.pos}', f'Имя и Фамилия: {self.get_full_name()}', f'Полный доход: {self.get_total_income()}']
			
d = {"wage": 100, "bonus": 50}
poss = Position('Drozdov', 'Vadim', 'Engineer', d)
print(poss.get_full_name())
print(poss.get_total_income())
print(poss.get_full_info())