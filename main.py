import numpy as np
import random
import matplotlib.pyplot as plt
import second
import third
import fourth
import fifth
import fifth_2

def get_rand_int():
	 return random.randint(1,10)

'''
	Заполнить кв дратную матрицу заданной размерности
'''
def create_matrix(x, y):
	return np.array(
		[
			 [get_rand_int() for _ in range(x)] for _ in range(y)
		]
	)

'''
	Составить матрицу, состоящую из четных
	строк и столбцов исходной
'''
def modify_matrix(matrix):
	return matrix[1::2, 1::2]

'''
	Выполнить действия с матрицей,
	Транспонирование
'''
def action_matrix(matrix):
	return matrix.T

'''
	Первая часть задания
'''
def part_one():
	# Размерность матрицы
	shape = 12
	matrix = create_matrix(shape, shape)
	print('matrix \n', matrix)
	modified_matrix = modify_matrix(matrix)
	print('modified matrix \n', modified_matrix)
	actioned_matrix = action_matrix(modified_matrix)
	print('actioned matrix \n', actioned_matrix)
	return

'''
	заполнить массив из 20 элементов случайными числами, распре-
	деленными по заданному закону, Бета
'''
def get_beta_distributed_array(mean, dispersion, n = 20):
	return np.random.beta(mean, dispersion, n)

'''
	Построить гистограмму
'''
def create_plot_hist(array):
	minval = min(array)
	maxval = max(array)
	binwidth = (maxval - minval) / 7
	bins = np.arange(minval, maxval + binwidth, binwidth)
	plt.hist(x = array, bins = bins, edgecolor='k')
	plt.show()
	return

def create_boxplot(array):
	plt.boxplot(array)
	plt.show()
	return 

def part_two():
	mean = 6
	dispersion = 10
	distributed = get_beta_distributed_array(mean, dispersion, 20)
	print('beta-distributed array\n', distributed)
	std_deviation = np.std(distributed)
	print('standard deviation\n', std_deviation)
	create_plot_hist(distributed)
	create_boxplot(distributed)
	return


def main():
	# fifth_2.main()
	# fifth.fifth_practice()
	fourth.fourth_practice()
	# third.third_practice()
	
	# second.second_practice()
	# part_one()
	# part_two()


if __name__ == '__main__':
	main()