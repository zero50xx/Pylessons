'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

'''
class Matrix:
	def __init__(self, arr):
		self.matrix = arr
		self.string = ''


	def prepare(self):
		self.string = ''
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[i])):
				self.string +=str(self.matrix[i][j]) + ' '
			self.string +='\n'
		return self.string

	def __str__(self):
		return self.prepare()

	def __add__(self, other_Matrix):
		other = str(other_Matrix)
		string_2 = self.string
		finaly = ''
		for i in range(len(string_2)):
			try:
				if string_2[i] == '\n':
					finaly += '\n'
				if isinstance(int(string_2[i]), int):
					finaly += str(int(string_2[i]) + int(other[i])) + ' '
			except:
				pass
		return finaly

matrix_1 = Matrix([[1,1,1], [2,2,2], [3, 3, 3]])
matrix_2 = Matrix([[2,2,2], [3,3,3], [4, 4, 4]])
print(matrix_1)
print('+ + +\n')
print(matrix_2)
print('= = =\n')
print(matrix_1 + matrix_2)