import matplotlib.pyplot as plt
from math import sqrt


def average_sample(data):
    summary = 0
    n = len(data)
    for i in range(n):
        summary += data[i]

    return summary / n


def standard_deviation(data):
    average = average_sample(data)

    n = len(data)
    summary2 = 0
    for i in range(n):
        summary2 += (data[i] - average) ** 2

    return summary2 / n


def sample_mean(array):
    return ((min(array) + max(array)) / 2) * len(array)


def sample_variance(array, sample_mean):
    return ((((min(array) + max(array)) / 2) - sample_mean) ** 2) * len(array)


def teor_ver(data):
    # вариационный ряд
    data.sort()
    print('Вариационный ряд:', data)

    # экстремальные значения
    min_value = data[0]
    max_value = data[-1]
    print('Минимум:', min_value, '\nМаксимум:', max_value)

    # Эмперическая функция распределения
    def empirical_distribution_function(x):
        n = len(data)
        summary = 0
        for i in range(n):
            if data[i] <= x:
                summary += 1
        return summary / n

    # График эмперической функции распределения
    plt.plot(data, [empirical_distribution_function(x) for x in data])
    plt.title('График эмперической функции распределения')
    plt.show()

    # Гистограмма и полигон частот группированных данных
    # группировка данных

    # количество групп
    k = 10
    # ширина группы
    h = (max_value - min_value) / k
    # границы групп
    borders = [min_value + h * i for i in range(k + 1)]
    # группы
    groups = [[] for _ in range(k)]
    for x in data:
        for i in range(k):
            if borders[i] <= x < borders[i + 1]:
                groups[i].append(x)
                break
    # частоты групп
    frequencies = [len(group) for group in groups]

    # Выборочное среднее
    acc = 0
    for x in groups:
        acc += sample_mean(x)
    sample_mean_param = round(acc / 100, 3)
    print('Выборочное среднее:', sample_mean_param)

    # Выборочная дисперсия
    acc = 0
    for x in groups:
        acc += sample_variance(x, sample_mean_param)
    sample_variance_param = round(acc / 100, 3)
    print('Выборочная дисперсия:', sample_variance_param)
    print('Выборочное среднее квадратическое отклонение:', round(sqrt(sample_variance_param), 3))

    # график гистограммы
    plt.bar(borders[:-1], frequencies, width=h)
    plt.title('Гистограмма частот')
    plt.show()
    # график полигона частот
    plt.plot(borders[:-1], frequencies)
    plt.title('Полигон частот')
    plt.show()


if __name__ == '__main__':
    array = [-5.44, -1.36, -2.49, -9.58, 1.63, 7.61, 0.07, -2.28, 0.12, -0.43,
             -1.25, 0.18, -5.05, 1.69, -7.94, 2.51, -1.96, 6.33, -2.12, -5.38,
             0.41, -8.29, 2.46, 5.74, 4.69, 0.91, 5.51, 1.48, 2.98, 1.24,
             -0.52, 3.56, -3.78, -4.47, 2.01, -7.32, 0.46, -1.75, 8.59, 3.15,
             -4.32, 0.95, -6.82, 0.92, -5.63, 1.94, -1.52, 4.19, -0.08, -3.51,
             8.24, 4.74, 3.37, 9.64, 2.68, -0.67, 8.37, 1.57, 5.63, 0.74,
             2.48, 2.16, 6.17, -0.07, -3.82, 6.41, -0.84, 5.93, 0.69, 9.89,
             -4.15, 6.57, 0.03, -4.83, -8.94, 0.55, -3.26, 1.79, 7.18, 1.85,
             -2.75, -3.03, -6.16, 0.38, -3.19, -0.38, -6.93, -9.86, 1.45, -4.56,
             1.74, 8.87, 2.87, 4.92, 1.09, 7.25, -1.72, 5.16, 3.64, -1.61]

    teor_ver(array)
