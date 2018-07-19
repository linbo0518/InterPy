from functools import reduce


def add(x):
    return x + x


def multiply(x):
    return x * x


if __name__ == '__main__':

    items = [1, 2, 3, 4, 5]
    squared = map(lambda x: x**2, items)
    print(list(squared))

    func_list = [add, multiply]
    for i in range(5):
        value = map(lambda x: x(i), func_list)
        print(list(value))

    number_list = [-1, -2, -3, 4, 5, 6]
    less_than_zero = filter(lambda x: x < 0, number_list)
    print(list(less_than_zero))

    product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
    print(product)