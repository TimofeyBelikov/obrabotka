import numpy as np
from scipy.stats import cauchy, maxwell, expon, exponnorm, skew, kurtosis, ecdf
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

def machine():
    sample_size = 100
    sample_c = cauchy.rvs(size=int(0.8 * sample_size))

    # Вычисляем основные статистики для распределения Коши
    m1 = np.median(sample_c)  # медиана (50-й перцентиль)
    mu1 = np.mean(sample_c)   # математическое ожидание (не существует для распределения Коши)
    D1 = np.var(sample_c)     # дисперсия (не существует для распределения Коши)

    # Вычисляем левый экспонормальный выброс
    p5 = abs(np.percentile(sample_c, 5))  # 5-й перцентиль
    sample_left_tail = exponnorm.rvs(1, loc=0, scale=p5, size=int(0.1 * sample_size))

    # Вычисляем правый выброс из распределения Максвелла
    mu2 = m1 + D1
    D2 = D1 / 5
    sample_right_tail = maxwell.rvs(loc=mu2, scale=np.sqrt(D2), size=int(0.1 * sample_size))

    # Объединяем выборки в одну
    sample = np.concatenate((sample_c, sample_left_tail, sample_right_tail))

    # Проверяем размер выборки
    assert len(sample) == sample_size, "Размер выборки не равен 100"

    # Вычисляем первые четыре момента выборки
    moments = [np.mean(sample), np.var(sample), skew(sample), kurtosis(sample)]
    print("Первые четыре момента выборки:", moments)
    sample_normal = np.random.normal(loc=mu1, scale=np.sqrt(D1), size=sample_size)

    plt.figure(figsize=(12, 6))

    # Эмпирическая функция плотности для выборки из Коши
    plt.hist(sample, bins=40, density=True, alpha=0.5, label='Cauchy Sample')

    # Эмпирическая функция плотности для выборки из нормального распределения
    plt.hist(sample_normal, bins=40, density=True, alpha=0.5, label='Normal Sample')

    plt.title('Эмпирическая функция плотности распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Вычисляем эмпирическую функцию распределения
    plt.figure(figsize=(12, 6))

    grid = np.linspace(-50, 50, 100)
    # Эмпирическая функция распределения для выборки из Коши
    ecdf_c = ECDF(sample)
    ecdf_n = ECDF(sample_normal)
    # print(ecdf_c)
    plt.plot(grid, ecdf_c(grid), lw=3)
    plt.plot(grid, ecdf_n(grid), lw=3)

    # plt.step(ecdf_c.x, ecdf_c.y, label='Cauchy Sample')

    # Эмпирическая функция распределения для выборки из нормального распределения
    
    # plt.step(ecdf_normal.x, ecdf_normal.y, label='Normal Sample')

    plt.title('Эмпирическая функция распределения')
    plt.xlabel('Значение')
    plt.ylabel('Вероятность')
    plt.legend()
    plt.grid(True)
    plt.show()


def create_cauchy_example():
    sample_size = 100
    percent_cauchy = 0.8
    percent_outliers = 0.2

    data_cauchy = cauchy.rvs(size=int(sample_size * percent_cauchy))
    m1 = np.median(data_cauchy)  # медиана
    mu1 = np.mean(data_cauchy)
    D1 = np.var(data_cauchy)

    maxwell_tail = create_maxwell(D1, m1, sample_size, 0.1)
    data_right_tail = np.concatenate((data_cauchy, maxwell_tail))
    expons_tail = create_exponorm(data_cauchy)

    data_tailed = np.concatenate((expons_tail, data_right_tail))

    '''
        Вычисление четырех моментов выборки
    '''
    moments = [np.mean(data_tailed), np.var(data_tailed), skew(data_tailed), np.mean(data_tailed ** 4)]
    """
        Генерация второй выборки нормальное распределение
    """
    # mean_normal = mu1
    # var_normal = D1
    mean_normal = np.mean(data_tailed)
    var_normal = np.var(data_tailed)

    data_normal = np.random.normal(mean_normal, np.sqrt(var_normal), sample_size)
    '''
        Построение эмпирической функции плотности распределения и
        эмпирической функции распределения для каждой выборки
    '''
    # Эмпирическая функция плотности
    sns.kdeplot(data_tailed, label='Коши 80% + 20 % (Максвелл, Экспонормальное)')
    sns.kdeplot(data_normal, label='Нормальное распределение')
    plt.title('Эмпирическая функция плотности')
    plt.legend()
    plt.show()

    # Эмпирическая функция распределения
    plt.hist(data_tailed, bins=20, cumulative=True, label='Коши 80% + 20 % (Максвелл, Экспонормальное)')
    plt.hist(data_normal, bins=20, cumulative=True, label='Нормальное распределение')
    plt.title('Эмпирическая функция распределения')
    plt.legend(loc='upper left')
    plt.show()

    create_comulate_fns(data_tailed, 'С 20 % выбросами')
    create_comulate_fns(data_normal, 'Нормальное')
    return


def create_comulate_fns(data, label):
    data_sorted = np.sort(data)
    n = len(data_sorted)
    y = np.arange(1, n+1) / n
    plt.plot(data_sorted, y, label=label)
    plt.show()

def create_maxwell(D1, m1, sample_size = 100, percents = 0.1):
    D2 = D1 / 5
    mu2 = m1 + D2
    data_maxwell = maxwell.rvs(loc= mu2, scale=np.sqrt(D2), size=int(sample_size * percents))
    return data_maxwell

def create_exponorm(data_cauchy, sample_size = 100, percents = 0.1 ):
    percentile_5th = np.percentile(data_cauchy, 5)

    print('percentile 5', percentile_5th)
    if percentile_5th <= 0:
        percentile_5th = 0.1
    data_expon = exponnorm.rvs(1, loc=0, scale=percentile_5th, size=int(sample_size * percents))
    return data_expon
    # data_left_tail = np.concatenate((data_expon, data_right_tail))

def fifth_practice():
    # create_cauchy_example()
    machine()
    return  