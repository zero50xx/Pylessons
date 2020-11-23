'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed. 

При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''
import random as rd

class Car():
	def __init__(self, speed, color, name, is_police):
		self.s = speed
		self.c = color
		self.n = name
		self.police_flag = is_police
	def go(self):
		return 'машина поехала...'
	def stop(self):
		return 'машина остановилась'
	def turn(self):
		return f'Машина повернула на {rd.randint(0, 360)} градусов на {"право" if rd.randint(0, 1) == 0 else "лево" }'
	def show_speed(self):
		return self.s

class TownCar(Car):
	def show_speed(self):
		if self.s < 60:
			return f'Внимание ваша скорость {self.s}, тогда когда разрешено только 60, а может вы анархист?'
		else:
			return self.s
class WorkCar(Car):
	def show_speed(self):
		if self.s < 40:
			return f'Внимание ваша скорость {self.s}, тогда когда разрешено только 40, а может вы анархист?'
		else:
			return self.s

class PoliceCar(Car):
	def thispolizei(self):
		return True


citizen_car = TownCar(64, 'red', 'mers', False)
worker_car = WorkCar(34, 'yello', 'largus', False)
polizei = PoliceCar(232, 'blue-white', 'camry', True)

print(citizen_car.show_speed())
print(citizen_car.stop())
print(citizen_car.go())
print(citizen_car.turn())


print(worker_car.show_speed())
print(worker_car.stop())
print(worker_car.go())
print(worker_car.turn())

print(polizei.show_speed())
print(polizei.stop())
print(polizei.go())
print(polizei.turn())
print(polizei.thispolizei())

		
