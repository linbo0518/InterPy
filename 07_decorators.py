from functools import wraps


def hi(name='Leon'):
    return 'hi ' + name


def hello(name='Leon'):
    print('now you are inside the hello() function')

    def greet():
        return 'now you are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    print(greet())
    print(welcome())
    print('now you are back in the hello() function')


def a(name='Leon'):

    def b():
        return 'you are in the b() function'

    def c():
        return 'you are in the c() function'

    if name == 'Leon':
        return b
    else:
        return c


def x():
    return 'hi Leon'


def run_before_x(func):
    print('run before executing x()')
    print(func())


def a_new_decorator(func):

    def warp_the_function():
        print('run before func()')
        func()
        print('run after func()')

    return warp_the_function


def a_function_requiring_decoration():
    print('the function which needs some decoration')


def another_decorater(func):

    @wraps(func)
    def another_warp_the_function():
        print('another run before func()')
        func()
        print('another run after func()')

    return another_warp_the_function


@another_decorater
def use_at_symbol():
    print('use @ to decorate a function')


def decorator_name(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return ("Function is running")


def log_it(logfile='out.log'):

    def logging_decorator(func):

        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@log_it()
def my_func():
    pass


@log_it(logfile='func2.log')
def my_func2():
    pass


if __name__ == '__main__':

    print(hi())
    nihao = hi
    del hi
    try:
        print(hi())
    except NameError as e:
        print(e)
    print(nihao())

    hello()
    try:
        greet()
    except NameError as e:
        print(e)
    try:
        welcome()
    except NameError as e:
        print(e)

    test = a()
    print(test)
    print(test())

    run_before_x(x)

    a_function_requiring_decoration()
    a_function_requiring_decoration = a_new_decorator(
        a_function_requiring_decoration)
    a_function_requiring_decoration()
    print(a_function_requiring_decoration.__name__)

    use_at_symbol()
    print(use_at_symbol.__name__)

    can_run = True
    print(func())
    can_run = False
    print(func())

    my_func()
    my_func2()