# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Введите результат первого дня пробежек в км: '))
b = int(input('Введите желаемый результат в км: '))
countofdays = 1

while a < b:
	countofdays += 1
	a = a * 1.1

print(f'Результат в {b} километров был достигнут на {countofdays}-й день!')

