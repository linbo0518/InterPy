def add_to(num, target=[]):
    target.append(num)
    return target


def add_to_modify(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target


if __name__ == '__main__':
    foo = ['hi']
    print(foo)

    bar = foo
    bar += ['bye']
    print(foo)

    print(add_to(1))
    print(add_to(2))
    print(add_to(3))

    print(add_to_modify(1))
    print(add_to_modify(2))
    print(add_to_modify(3))