import inspect

if __name__ == '__main__':
    
    # dir
    my_list = [1, 2, 3]
    print(dir(my_list))

    # type
    print(type(''))
    print(type([]))
    print(type({}))
    print(type(dict))
    print(type(3))

    # id
    name = 'Yasoob'
    print(id(name))

    # inspect
    print(inspect.getmembers(str))