'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import time
import os
class TrafficLight:
	def __init__(self, color):
		self.__colr = color
	def running(self):
		while True:
			print(self.__colr[0])
			time.sleep(7)
			os.system('cls')

			print(self.__colr[1])
			time.sleep(2)
			os.system('cls')

			print(self.__colr[2])
			time.sleep(5)
			os.system('cls')


traf = TrafficLight(color=['red','yellow','green'])
traf.running()