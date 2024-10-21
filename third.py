import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats

def create_beta_samples(n = 60):
    alpha, beta = 2, 5
    beta_samples = np.random.beta(2, 5, 60)
    return beta_samples

def create_maxwell_samples(n = 60):
    a = 4
    maxwell_sample = np.random.rayleigh(a, 60)
    return maxwell_sample

'''
    Построить их гистограммы с количеством интервалов равным 5,
    равным 10, и равных объему выборки
'''
def create_hists(data, title):
    fig, axs = plt.subplots(1, 3)
    # 5 интервалов
    axs[0].hist(data, bins=5)
    axs[0].set_title(f'{title} - 5 интервалов')
    # 10 интервалов
    axs[1].hist(data, bins=10)
    axs[1].set_title(f'{title} - 10 интервалов')
    # 60 интервалов
    axs[2].hist(data, bins=len(data))
    axs[2].set_title(f'{title} - {len(data)} интервалов')
    
    plt.tight_layout()
    plt.show()


def create_str_disrt_hist(means, title):
    plt.hist(means, bins=60, edgecolor='black')
    plt.title(f'Центральная предельная теорема- {title}')
    plt.xlabel('Среднее значние')
    plt.ylabel('Частота')
    plt.show()

'''
    Проверить центральную предельную теорему,
    построив распределение средних значений по 10 000 выборкам,
    сформированным по заданным распределениям
'''
def chech_theor(num_samples):
    means = []
    for _ in range(num_samples):
        sample = create_beta_samples()
        sample_mean = np.mean(sample)
        means.append(sample_mean)
    return means

def chech_theor_maxwell(num_samples):
    means = []
    for _ in range(num_samples):
        sample = create_maxwell_samples()
        sample_mean = np.mean(sample)
        means.append(sample_mean)
    return means



def third_practice():
    
    print('third practice')

    beta_samples = create_beta_samples()
    maxwell_samples = create_maxwell_samples()

    create_hists(maxwell_samples, 'Распределение Максвелла')

    beta_means = chech_theor_maxwell(10000)
    create_str_disrt_hist(beta_means, 'Распределение Максвелла')
    return 