import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, laplace
import scipy.stats as stats
import seaborn

'''
    Формирование двух выборок зщаданного объема
    При одинаковом законе распределения получившиеся гистограммы
    имеют различия
'''
def create_experimental_manual():
    mu = 4
    sigma = 2

    mu_laplace = 2.0
    sigma_laplace = 0
    
    # Создадим объекты с предустановкой параметров для генерации
    # случайных вариантов 
    rv_first = norm(loc=mu, scale=sigma)
    rv_second = laplace(mu_laplace, sigma_laplace)
    rv_second = laplace.pdf()

    sample_size = 1000
    # Формируем выборку на основе первого распределенияы
    sample_first = rv_first.rvs(size = sample_size)
    sample_second = rv_second.rvs(size = sample_size)


    plt.figure()
    plt.hist(sample_first, bins=25, edgecolor='k')
    plt.show()

    plt.figure()
    plt.hist(sample_second, bins=25, edgecolor='k')
    plt.show()

    return


def create_experimental_norm(size = 25):
    mu = 4
    sigma = 2
    sample_norm = np.random.normal(loc=mu, scale=sigma, size=size)
    return sample_norm


def create_experimental_laplas():
    size = 1000
    loc = 1
    scale = 2
    sample_laplace = np.random.laplace(loc=loc, scale=scale, size=size)
    return sample_laplace

'''
    Формирование экспериментального вида функций плотности распределений
'''
def create_experimental():
    sample_norm = create_experimental_norm()
    sample_laplas = create_experimental_laplas()
    plt.figure()
    plt.hist(sample_norm, bins=15, edgecolor='black')
    plt.title('Экспериментальная плотность распределения - Нормальное')
    plt.show()

    plt.figure()
    plt.hist(sample_laplas, bins=15, edgecolor='black')
    plt.title('Экспериментальная плотность распределения - Лаплас')
    plt.show()
    return


'''
    Статистика для гипотезы о значении математического
    ожидания при известной дисперсии
'''
def calc_z(sample, hyp_mean, std_dev):
    sample_mean = np.mean(sample)
    size = 1000
    z = (sample_mean - hyp_mean ) / (std_dev / np.sqrt(size))
    return z

def create_experimental_z():

    mu = 4
    sigma = 2

    sample_norm = norm(loc=mu, scale=sigma)

    sample_size = 100
    sample_first = sample_norm.rvs(size = sample_size)
    data = []
    '''
        500 выборок размером 25
    '''
    for i in range(10000):
        data.append(sample_norm.rvs(size=50))

    calculated_stats = []
    for sample in data:
        z = calc_z(sample, mu, sigma)
        calculated_stats.append(z)
        
    theoretical = norm(1, 0)

    fig, ax = plt.subplots(1, 1, figsize=(15, 0))
    ax.hist(calculated_stats, bins=60, label='Экспериментальная плотность')
    x = np.linspace(min(calculated_stats), max(calculated_stats), 100)
    ax.plot(x, theoretical.pdf(x), color='red', label='Теоретическая плотность')

    ax.set_title('Распределение Z-статистик')
    ax.set_xlabel('Z-значение')
    ax.set_ylabel('Плотность')
    ax.legend()
    plt.show()

def exp():
    # Параметры для выборок
    n = 25
    mu1, sigma1 = 4, 2  # N(4, 2)
    mu2, b2 = 1, 2  # Лапласа(1, 2)

    # Генерация выборок по 25 элементов каждая
    sample1 = np.random.normal(mu1, sigma1, n)
    sample2 = np.random.laplace(mu2, b2, n)

    # Теоретические плотности
    '''
        Создаем массив значний x, start и stop - начальное и конечное значние,
        min минимальное из минимальных значений выборок,
        max - максимальное значение из двух выборок
    '''
    x = np.linspace(min(min(sample1), min(sample2)) - 1, max(max(sample1), max(sample2)) + 1, 1000)
    '''
        Вычисление значений плотности вероятностей в сгенерированных точках,
        mu1 - математическое ожидание среднее нормального распределения,
        sigma1 - стандартное отклонение.
        В результате - массив чисел, где каждому x соответствует значение плотности
        Probability Density Function
    '''
    pdf_normal = stats.norm.pdf(x, mu1, sigma1)
    '''
      mu2 - Среднее распределение Лапласа
      b2 - Параметр масштаба  
    '''
    pdf_laplace = stats.laplace.pdf(x, mu2, b2)
    '''
        Pdf - Теоретические плотности для точек из X
    '''

    # Построение графиков теоретических и экспериментальных плотностей
    plt.figure(figsize=(10, 6))

    # Теоретические плотности
    plt.plot(x, pdf_normal, label='Нормальное (N(4, 2)) - теоретическая', color='blue', lw=2)
    plt.plot(x, pdf_laplace, label='Лаплас (1, 2) - теоретическая', color='red', lw=2)

    # Экспериментальные плотности
    plt.hist(sample1, bins=10, density=True, alpha=0.5, label='Выборка - нормальное ', color='blue')
    plt.hist(sample2, bins=10, density=True, alpha=0.5, label='Выборка - Лаплас', color='red')

    plt.title("Плотности распределений")
    plt.xlabel('Значение')
    plt.ylabel('Плотность')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Проверка гипотезы о равенстве математических ожиданий
    # Известная дисперсия для нормального распределения: σ^2 = 4 (т.е. σ = 2)
    sigma_known = 2  # Дисперсия известна

    # Средние по выборкам
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)

    # Стандартная ошибка для выборки 1
    se = sigma_known / np.sqrt(n)

    # Z-статистика
    z_stat = (mean1 - mean2) / se

    # Критическое значение для двустороннего теста при уровне значимости 0.05
    z_critical = stats.norm.ppf(1 - 0.05 / 2)

    # p-value для Z-статистики
    '''
        Z - насколько далеко выборочное среднее отклоняется от предполагаемого значения
        cdf - функция кумулятивного распределения нормального распределения,
        вероятность того, что случайная величина Z меньше или равно x.
        Важно отклонение от нуля 
        p - вероятность наблюдения такой же или более отклоняющейся  Z-статистики
        в распределении. Уровень значимости  A - 0.05 и если p<a мы отклоняем нулевую гипотезу,
        значит мы говорим о статистически значимых различиях между математическими ожиданиями
    '''
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    print(f"Z-статистика: {z_stat}")
    print(f"Критическое значение: {z_critical}")
    print(f"P-значение: {p_value}")

    # Проверка гипотезы
    if abs(z_stat) > z_critical:
        print("математические ожидания различаются.")
    else:
        print("Нет статистически значимых различий.")

def fourth_practice():
    exp()
    # create_experimental_z()
    # create_experimental_manual()
    return  