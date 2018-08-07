if __name__ == '__main__':
    
    add = lambda x, y: x + y
    print(add(3, 5))

    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[1])
    print(a)