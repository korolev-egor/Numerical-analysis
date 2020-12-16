from math import sin
from math import pi
from math import cos
from math import e

def problem2(domain, image, node, n):
    new_domain = []
    new_image = []

    def abs_sort():
        nonlocal new_domain
        nonlocal new_image
        my_list = [[abs(domain[i] - node), domain[i], image[i]] for i in range(len(domain))]
        my_list.sort()
        new_domain = [i[1] for i in my_list][:n+1]
        new_image = [i[2] for i in my_list][:n+1]


def trap(foo, a, b, m=50000):
    h = (b - a) / m
    nodes = [a + k * h for k in range(m + 1)]
    values = {x: foo(x) for x in nodes}
    common_sum = sum(values[x] for x in nodes) - values[nodes[0]] - values[nodes[-1]]
    return ((b - a) / (2 * m)) * (values[nodes[0]] + 2 * common_sum + values[nodes[-1]])


def w(x):
    return abs(x - 1 / 2)


def f(x):
    return sin(x)


def g(x):
    return f(x)*w(x)


def fmeler(x):
    return g(x)*((1-x**2)**0.5)


ANSWER = 0.1124687546654206
NEW_ANSWER = 0
# a = 0
# b = 1
# m = 50000
# a = float(input('Введите а: '))
# b = float(input('Введите b: '))
# m = int(input('Введите m: '))
t1 = -1/(3 ** (1/2))
t2 = -t1


def КФ_Гаусса():
    print('\nПриближенное вычисление интеграла с помощью КФ Гаусса с двумя узлами')

    def gtk(a, b, t):
        return g(t * (b - a) / 2 + (b + a) / 2)

    h = (b - a) / m
    nodes = [a + k * h for k in range(m + 1)]
    result = 0
    for i in range(m):
        result += 0.5 * (nodes[i+1] - nodes[i]) * (gtk(nodes[i], nodes[i + 1], t1) + gtk(nodes[i], nodes[i + 1], t2))
    print('Полученный ответ: {}\nМодуль невязки: {}\n{:%}'.format(result, abs(result-ANSWER),abs(result-ANSWER) / ANSWER))


def КФ_типа_Гаусса():
    print('\nПриближенное вычисление интеграла с помощью КФ типа Гаусса с двумя узлами')
    moment0 = trap(w, a, b)
    moment1 = trap(lambda x: w(x) * x, a, b)
    moment2 = trap(lambda x: w(x) * x ** 2, a, b)
    moment3 = trap(lambda x: w(x) * x ** 3, a, b)
    print('Вычисленные моменты весовой функции:\n0: {}\n1: {}\n2: {}\n3: {}'.format(moment0, moment1, moment2, moment3))
    a1 = (moment0 * moment3 - moment2 * moment1) / (moment1 ** 2 - moment2 * moment0)
    a2 = (moment2 ** 2 - moment3 * moment1) / (moment1 ** 2 - moment2 * moment0)
    x1 = (-a1 - (a1 ** 2 - 4 * a2) ** (1 / 2)) / 2
    x2 = (-a1 + (a1 ** 2 - 4 * a2) ** (1 / 2)) / 2
    print('Ортогональный многочлен: x*x + {:.5f}x + {:.5f}'.format(a1, a2))
    print('Корни многочлена:\nx1 = {}\nx2 = {}'.format(x1, x2))
    if x1 == x2:
        print('x1 равно x2')
    if not (a <= x1 <= b and a <= x2 <= b):
        print('x1 или x2 не принадлежат [', a, ',', b, ']', sep='')
    A1 = (moment1 - x2 * moment0) / (x1 - x2)
    A2 = (moment1 - x1 * moment0) / (x2 - x1)
    print('Коэффициенты КФ:\nA1 = {}\nA2 = {}'.format(A1, A2))
    print('A1 + A2 равно нулевому моменту?: ', A1 + A2 == moment0)
    result = A1 * f(x1) + A2 * f(x2)
    print('Полученный ответ: {}\nМодуль невязки: {}\n{:%}'.format(result, abs(result-ANSWER), abs(result-ANSWER) / ANSWER))


def new_w(x):
    return 1/((1-x**2)**0.5)


def КФ_Мелера():
    print('\nПриближенное вычисление интеграла с помощью КФ Мелера с {} узлами'.format(n))
    _sum = 0
    for k in range(1, n+1):
        _sum += f(cos(pi*(2*k-1)/(2*n)))
    result = (pi/n)*_sum
    print('Полученный ответ: {}\nМодуль невязки: {}'.format(result, abs(result - ANSWER)))

def foo(x):
    return e**(-x) - x*x/2
def Newtone():
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    m = int(input('Введите m: '))
    n = int(input('Введите n: '))


while(True):
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    m = int(input('Введите m: '))
    КФ_типа_Гаусса()
    КФ_Гаусса()
    a = -1
    b = 1
    n = int(input('\nВведите количество узлов в КФ Мелера N: '))
    КФ_Мелера()
    if input('Ввести новые параметры? (y/n) :') != 'y':
        break