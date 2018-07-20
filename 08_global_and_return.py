def add(value1, value2):
    return value1 + value2


def multipy(value1, value2):
    global result
    result = value1 * value2


def profile():
    name = "Leon"
    age = 23
    return name, age


if __name__ == '__main__':
    result = add(3, 5)
    print(result)

    multipy(3, 5)
    print(result)

    name, age = profile()
    print(name, age)