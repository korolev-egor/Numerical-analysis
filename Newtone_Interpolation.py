from math import e
print('Интерполяция полиномомом Ньютона\nВариант 7')


def f(x):
    return e**(-x) - x*x/2


# a = 0
# b = 1
# node = 0.65
# n = 7
# m = 15


def abs_sort(domain, image, node):
    my_list = [[abs(domain[i] - node), domain[i], image[i]] for i in range(len(domain))]
    my_list.sort()
    new_domain = [i[1] for i in my_list][:n + 1]
    new_image = [i[2] for i in my_list][:n + 1]
    return new_domain, new_image


def newtone(x, nodes, values):
    def div_dif(first_ind, last_ind):
        if last_ind - first_ind == 1:
            return (values[last_ind] - values[first_ind]) / (nodes[last_ind] - nodes[first_ind])
        return (div_dif(first_ind+1, last_ind) - div_dif(first_ind, last_ind-1)) / (nodes[last_ind] - nodes[first_ind])
    result = values[0]
    def multip(i):
        res = 1
        for j in range(i+1):
            res *= (x-nodes[j])
        return res
    for i in range(1, n+1):
        result += div_dif(0, i) * multip(i)
    return result
while True:
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    m = int(input('Введите число значений в таблице минус один m: '))
    n = int(input('Введите степень многочлена n, оно должно быть меньше или равно {}: '.format(m)))
    h = (b-a)/m
    nodes = [a + k * h for k in range(m+1)]
    values = [f(node) for node in nodes]
    print(nodes)
    node = float(input('Введите точку интерполяции: '))
    nodes, values = abs_sort(nodes, values, node)
    newtone_res = newtone(node, nodes, values)
    print('Значение полинома Ньютона в точке интерполяции: {}\nЗначение абсолютной фактической погрешности: {}\n{:%}'
          .format(newtone_res, abs(newtone_res-f(node)),abs(newtone_res-f(node))/f(node)))
    if input('Ввести новые параметры? (y/n): ') == 'n':
        break
