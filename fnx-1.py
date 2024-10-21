import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, laplace

'''
    Формирование двух выборок зщаданного объема
    При одинаковом законе распределения получившиеся гистограммы
    имеют различия
'''
def create_experimental_manual():
    mu = 4
    sigma = 2

    mu_laplace = 4
    sigma_laplace = 2

    rv_first = norm(loc=mu, scale=sigma)
    rv_second = laplace(mu, sigma)
    sample_size = 25

    sample_first = rv_first.rvs(size = sample_size)
    sample_second = rv_second.rvs(size = sample_size)


    plt.figure()
    plt.hist(sample_first, bins=10, edgecolor='k')
    plt.show()

    return


def create_experemental():
    # Параметры нормального распределения
    mu, sigma = 4, 2

    # Генерация данных
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

    # Теоретическая плотность вероятности
    pdf_theoretical = norm.pdf(x, mu, sigma)

    # Экспериментальная плотность вероятности
    sample_size = 1000
    sample = np.random.normal(mu, sigma, sample_size)
    pdf_experimental, bins = np.histogram(sample, bins=30, density=True)
    bins_center = (bins[:-1] + bins[1:]) / 2

    plt.figure(figsize=(10, 5))
    plt.plot(x, pdf_theoretical, 'r-', label='Theoretical PDF')
    plt.plot(bins_center, pdf_experimental, 'b-', label='Experimental PDF')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Theoretical and Experimental PDF of Normal Distribution')
    plt.legend()
    plt.show()
    return
