def test_var_args(first_arg, *args):
    print('the first arg:', first_arg)

    for arg in args:
        print('the other arg:', arg)


def test_var_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('{0} == {1}'.format(key, value))


def test_args_kwargs(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)


if __name__ == '__main__':

    test_var_args('first', 'second', 'third', 'fourth')
    test_var_kwargs(name='Leon')

    args = ('one', 2, '五')
    test_args_kwargs(*args)
    kwargs = {'arg2': 2, 'arg3': '五', 'arg1': 'one'}
    test_args_kwargs(**kwargs)