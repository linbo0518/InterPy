if __name__ == '__main__':

    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    print(duplicates)

    duplicates = set([x for x in some_list if some_list.count(x) > 1])
    print(duplicates)

    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print(input_set.intersection(valid))
    print(input_set.difference(valid))

    a_set = {'red', 'blue', 'green'}
    print(type(a_set))