'''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). 

Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 

В каждом из классов реализовать переопределение метода draw. 

Для каждого из классов методы должен выводить уникальное сообщение. 

Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
	def __init__(self, title):
		self.tit = title
	def draw(self):
		return 'Запуск отрисовки(' + self.tit + ')'
	

class Pen(Stationery):
	def draw(self):
		return 'Запуск написания(' + self.tit + ')'

class Pencil(Stationery):
	def draw(self):
		return 'Запуск черчения(' + self.tit + ')'

class Handle(Stationery):
	def draw(self):
		return 'Запуск выделения(' + self.tit + ')'

pen = Pen('Ручка')
pencil = Pencil('Марандаш')
handle = Handle('Маркер')

print(pen.draw())
print(pencil.draw())
print(handle.draw())