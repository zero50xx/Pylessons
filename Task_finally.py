import random
import os

class Matrix:
	def __init__(self,list_of_lists):

		self.result = '╔╦══╦╦══╦╦══╦╦══╦╦══╦╦══╦╦══╦╦══╦╦══╦╗\n'
		self.list_of_lists = list_of_lists
		for i in range(3):
			self.result += '║'
			for j in range(9):
				if self.list_of_lists[i][j] == 0:
					self.result += '║  ║'
				else:
					if self.list_of_lists[i][j] < 10:
						self.result += '║ ' + str(self.list_of_lists[i][j]) + '║'
					else:
						self.result += '║' + str(self.list_of_lists[i][j]) + '║'
			self.result += '║'
			if i != 2:
				self.result += '\n╠╬══╬╬══╬╬══╬╬══╬╬══╬╬══╬╬══╬╬══╬╬══╬╣\n'
			else:
				self.result += '\n╚╩══╩╩══╩╩══╩╩══╩╩══╩╩══╩╩══╩╩══╩╩══╩╝'
	def __str__(self):
		return self.result


class LotoCard:
	def __init__(self):
		self.n_l = []
		g = self.gen_num()
		self.numbers_matrix = [[next(g) for j in range(5)] for i in range(3)]
		for i in range(len(self.numbers_matrix)):
			self.numbers_matrix[i].sort()
		self.n_l = []
		self.number_or_null = 0
		self.index_table = []
		for i in range(3):
			self.index_table.append([])
			self.count_of_none = 4
			self.count_of_number = 5
			self.index = 0
			for j in range(9):
				self.number_or_none= random.randint(0,1)
				if ((self.number_or_none == 0) and (self.count_of_none > 0)) or (self.count_of_number == 0):
					self.count_of_none -= 1
					self.index_table[i].append(0)
				elif ((self.number_or_none != 0) and (self.count_of_number > 0)) or (self.count_of_none == 0):
					self.index_table[i].append(self.numbers_matrix[i][self.index])
					self.index += 1
					self.count_of_number -= 1
		self.numbers_matrix = self.index_table



	def get_matrix(self):
		self.get = Matrix(self.numbers_matrix)
		return self.get
	def gen_num(self):
		while True:
			n = random.randint(1, 90)
			if n not in self.n_l:
				self.n_l.append(n)
				yield n

class LotoGame:
	def __init__(self, one_player, two_player):
		self.one_player = one_player
		self.two_player = two_player
		self.list_of_numbers_game = []
		self.count = 90
		self.matrix1_1 = self.one_player.numbers_matrix
		self.matrix2_1 = self.two_player.numbers_matrix
		self.matrix1_2 = Matrix(self.matrix1_1)
		self.matrix2_2 = Matrix(self.matrix2_1)
		self.p1 = 15
		self.p2 = 15

	def print_game(self):
		print('Ваша карточка')
		print(self.matrix1_2)
		print('\nКарточка компьютера')
		print(self.matrix2_2)

	def game_start(self):
		hhod = self.get_random_number
		if hhod != 0:
			print(f'Новый бочонок: {hhod} (осталось {self.count})')
			self.print_game()
		
			reshenie = input('Зачеркнуть? (y/n)')
			if reshenie == 'y':
				if hhod in self.matrix1_1[0]:
					self.p1 -= 1
					for i in range(len(self.matrix1_1[0])):
						if hhod == self.matrix1_1[0][i]:
							self.matrix1_1[0][i] = 0
				elif hhod in self.matrix1_1[1]:
					self.p1 -= 1
					for i in range(len(self.matrix1_1[1])):
						if hhod == self.matrix1_1[1][i]:
							self.matrix1_1[1][i] = 0
				elif hhod in self.matrix1_1[2]:
					self.p1 -= 1
					for i in range(len(self.matrix1_1[2])):
						if hhod == self.matrix1_1[2][i]:
							self.matrix1_1[2][i] = 0
				else:
					print('вы проиграли')
					self.p2 = 0
				self.matrix1_2 = Matrix(self.matrix1_1)		
			else:
				if hhod in self.matrix1_1[0]:
					print('вы проиграли')
					self.p2 = 0
				elif hhod in self.matrix1_1[1]:
					print('вы проиграли')
					self.p2 = 0
				elif hhod in self.matrix1_1[2]:
					print('вы проиграли')
					self.p2 = 0
			if hhod in self.matrix2_1[0]:
				self.p2 -= 1
				for i in range(len(self.matrix2_1[0])):
					if hhod == self.matrix2_1[0][i]:
						self.matrix2_1[0][i] = 0
			elif hhod in self.matrix2_1[1]:
				self.p2 -= 1
				for i in range(len(self.matrix2_1[1])):
					if hhod == self.matrix2_1[1][i]:
						self.matrix2_1[1][i] = 0
			elif hhod in self.matrix2_1[2]:
				self.p2 -= 1
				for i in range(len(self.matrix2_1[2])):
					if hhod == self.matrix2_1[2][i]:
						self.matrix2_1[2][i] = 0
			self.matrix2_2 = Matrix(self.matrix2_1)
			os.system('cls||clear')
			if (self.p1 !=0) and (self.p2 != 0):
				self.game_start()
			else:
				if self.p1 < self.p2:
					print('Вы выиграли')
				elif self.p1 == self.p2:
					print('игра закончена у вас ничья')
				elif self.p1 > self.p2:
					print('Вы проиграли')
			
	@property
	def get_random_number(self):
		while True:
			n = random.randint(1, 90)
			if (n not in self.list_of_numbers_game) and (self.count != 0):
				self.list_of_numbers_game.append(n)
				self.count -= 1
				return n
		if self.count == 0:
			return 0

one = LotoCard()
two = LotoCard()
game = LotoGame(one, two)
game.game_start()
