import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def create_graph(data):    
    plt.hist(data, bins=30, edgecolor='k')
    plt.show()
    return 


def run():
    '''
        Зададим объем выборки
    '''
    n_main = 80
    rv_main = stats.cauchy
    '''
        Формируем выборку из распределения Коши
    '''
    data_main = rv_main.rvs(size = n_main)
    # Мат ожидание, отклонение и медиана

    # Математическое ожидание
    mu = np.mean(data_main)
    # Отклонение
    sigma = np.std(data_main)

    # Дисперсия
    D1 = np.var(data_main) 
    D2 = D1/5
    # Медиана
    median = np.median(data_main)

    '''
        на правом хвосте из распределения, полученного из распределения
        (Максвелл, параметры распределения —по формуле mu2 =
        = m1 + D2, D2 = D1/5);
        Распределение Максвелла
        Хвост справа из 10 элементов
    '''  
    n_right = 10
    mu_right = abs(mu + D2)
    sigma_right = abs(sigma / 6)
    rv_right = stats.maxwell(loc=mu_right, scale = sigma_right)
    data_right = rv_right.rvs(size=10)
    data_cauchy_maxwell = np.concat((data_main, data_right))

    '''
        На левом хвосте распределение экспонормальное
        математическое ожидание - 5й перценталь
    '''
    fifth_percental = np.percentile(data_main, 5)
    print(fifth_percental)
    k = 4
    rv_left = stats.exponnorm(k, loc=fifth_percental)
    data_left = rv_left.rvs(size=10)
    data_cauchy_maxwell_exponnor = np.concat((data_left, data_cauchy_maxwell))

    create_graph(data_main)
    create_graph(data_cauchy_maxwell)
    create_graph(data_cauchy_maxwell_exponnor)

    # create_graph(data_left)

    # plt.hist(data_main, bins=30, color='blue', alpha=0.4, edgecolor='k')
    # plt.show()
    # plt.hist(data_cauchy_maxwell, bins=30, alpha=0.4, color='red', edgecolor='k')
    # plt.show()
    # plt.hist(data_cauchy_maxwell_exponnor, bins=30, alpha=0.4, color='yellow', edgecolor='k')
    # plt.show()

    # create_graph(data_main)
    # create_graph(data_cauchy_maxwell)

    return



def main():
    run()
    return 