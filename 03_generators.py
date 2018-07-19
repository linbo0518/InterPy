def generator_function():
    for i in range(10):
        yield i


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    for item in generator_function():
        print(item)

    for i in fibon(10):
        print(i)

    gen = generator_function()
    for i in range(11):
        try:
            print(next(gen))
        except StopIteration:
            print('Out of Range')

    my_str = 'Leon'
    try:
        next(my_str)
    except Exception as e:
        print(e)

    my_iter = iter(my_str)
    print(next(my_iter))