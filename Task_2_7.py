'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы 
для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod
class Clothes(ABC):
	def __init__(self,name_of_clothes, vh):
		self.flag = False
		self.vh_ = vh
		if name_of_clothes == 'пальто':
			self.flag = True
		elif name_of_clothes == 'костюм':
			self.flag = False
		else:
			raise RuntimeError("Пожалуйста введите первым аргументом пальто или костюм") from None

	@abstractmethod
	def __str__(self):
		pass

	@abstractmethod
	def __add__(self):
		pass

	@abstractmethod
	def why_is_clothes(self):
		pass

class Cloth(Clothes):
	def __str__(self):
		if self.flag:
			return str(self.vh_/6.5 + 0.5)
		else:
			return str(2 * self.vh_ + 0.3)

	def __add__(self, other_cloth):
		other_c = str(other_cloth)
		if isinstance(other_cloth, Cloth):
			return float(self.__str__()) + float(other_c)
	@property
	def why_is_clothes(self):
		s = 'пальто' if self.flag else 'костюм'
		return s
		
palt = Cloth('пальто', 54)
costum = Cloth('костюм', 186)
print(palt)
print(costum)		
print(palt + costum)
print(palt.why_is_clothes)
print(costum.why_is_clothes)