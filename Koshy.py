# y´(x)= - y(x)+ cos(x), y(0)=1; h=0,1 N=10
from math import e, sin, cos, factorial


def solution(x):
    return 0.5 * (e ** (-x) + sin(x) + cos(x))


def foo(x, y):
    return -y + cos(x)


def taylor(x):  # следующий после 8 степени шла бы 11, а 11! = 39916800
    return 1 - (x**3) / 6 + (x**4) / 24 - (x**7)/factorial(7) + (x**8)/factorial(8)


def precise_solution():
    print('\nТаблица значений точного решения в равноотстоящих с шагом', h,'точках:')
    for i in range(-2, N + 1):
        print('x = {}, y = {}'.format(nodes[i+2], values[i+2]))


def euler():
    print('\n\nРешение методом Эйлера')
    euler_storage = [[x0 + k*h, 1] for k in range(N+1)]
    for i in range(1, N+1):
        euler_storage[i][1] = euler_storage[i-1][1] + h * foo(euler_storage[i-1][0], euler_storage[i-1][1])
        print('x =', euler_storage[i][0], 'y =', euler_storage[i][1])
    print('Абсолютная погрешность для последнего значения : ', euler_storage[N][1]-solution(euler_storage[N][0]))
    print('\nРешение улучшенным методом Эйлера I')
    euler_first = [[x0+h/2 + k*h, 0] for k in range(N)]
    for i in range(N):
        euler_first[i][1] = euler_storage[i][1] + h*foo(euler_storage[i][0], euler_storage[i][1])/2
        print('x =', euler_first[i][0], 'y =', euler_first[i][1])
    print('Абсолютная погрешность: ', euler_first[N-1][1]-solution((euler_first[N-1][0])))  # Улучшенный эйлер
    print('\nРешение улучшенным методом Эйлера II')
    for i in range(1, N+1):
        euler_storage[i][1] = euler_storage[i-1][1] + h*foo(euler_storage[i-1][0]+h/2,euler_storage[i-1][1]+h*foo(euler_storage[i-1][0],euler_storage[i-1][1])/2)
    print('Абсолютная погрешнось: ', euler_storage[N][1]-solution(euler_storage[N][0]))  # Эйлер 2
    print('\nРешение улучшенным методом Эйлера III')
    new_euler = [[x0 + k*h, 1] for k in range(N+1)]
    for i in range(1, N+1):
        new_euler[i][1] = new_euler[i-1][1] + h*0.5*(foo(new_euler[i-1][0], new_euler[i-1][1])
                                                     - foo(new_euler[i][0], euler_storage[i][1]))
    print('Абсолютная погрешность: ', new_euler[N][1]-solution(new_euler[N][0]))  # Эйлер 3


def runge_kutt():
    print('\n\nРешение методом Рунке-Кутты')
    storage = [[x0 + k*h, 1] for k in range(N+1)]
    for i in range(1, N+1):
        k1 = h*foo(storage[i-1][0],storage[i-1][1])
        k2 = h*foo(storage[i-1][0] + h/2, storage[i-1][1] + k1/2)
        k3 = h*foo(storage[i-1][0] + h/2, storage[i-1][1] + k2/2)
        k4 = h*foo(storage[i-1][0] + h, storage[i-1][1] + k3)
        storage[i][1] = storage[i-1][1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        print('x =', storage[i][0], 'y =', storage[i][1])
    print('Абсолютная погрешнось метода Рунге-Кутты: ', storage[N][1]-solution(storage[N][0]))  # Эйлер 2


def taylor_method():
    print('\n\nРешение методом Тейлора')
    result = [[x0 + k*h, 0] for k in range(-2,N + 1)]
    for i in range(len(nodes)):
        print('x = {}, y = {}, абсолютная погрешность = {}'.format(nodes[i], taylor(nodes[i]), abs(taylor(nodes[i]) - solution(nodes[i]))))
        if i < 5:
            result[i][1] = taylor(nodes[i])
    return result


def Экстраполяция_Адамса4(res):
    print('\n\nРешение экстраполяционным методом Адамса 4-го порядка')

    def trap(foo, a, b, m=50000):
        h1 = (b - a) / m
        xlist = [a + k * h1 for k in range(m + 1)]
        ylist = {x: foo(x) for x in xlist}
        common_sum = sum(ylist[x] for x in xlist) - ylist[xlist[0]] - ylist[xlist[-1]]
        return ((b - a) / (2 * m)) * (ylist[xlist[0]] + 2 * common_sum + ylist[xlist[-1]])

    def diff(j, k):
        if j == 1:
            return h*(foo(res[k+1][0], res[k+1][1])-foo(res[k][0], res[k][1]))
        return diff(j-1, k+1) - diff(j-1, k)

    def lb(j):
        def mult(x):
            res = 1
            for i in range(j):
                res *= (x+i)
            return res
        return lambda x: mult(x)
    def q(j):
        return h * foo(res[j][0], res[j][1])
    for m in range(4, N+2):
        res[m+1][1] = res[m][1] + q(m) + diff(1, m-1)/2 + 5*diff(2, m-2)/12 + 3*diff(3, m-3)/8 + 251*diff(4, m-4)/720
        print('x = {}, y = {}'.format(res[m+1][0], res[m+1][1]))
    print('Абсолютная погрешность последнего значения: {}'.format(abs(res[N+2][1]-solution(res[N+2][0]))))
while True:
    h = 0.01
    N = 10
    x0 = 0
    y0 = 1
    # h = float(input('Введите h: '))
    # # N = int(input('Введите N: '))
    nodes = [x0 + k * h for k in range(-2, N + 1)]
    values = [solution(node) for node in nodes]
    precise_solution()
    Экстраполяция_Адамса4(taylor_method())
    euler()
    runge_kutt()
    if input('Ввести новые параметры? (y/n): ') == 'n':
        break
