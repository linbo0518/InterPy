if __name__ == '__main__':
    
    is_fat = True
    state = 'fat' if is_fat else 'not fat'
    print(state)

    fat = True
    fitness = ("skinny", "fat")[fat]
    print(fitness)

    condition = True
    print(2 if condition else 1 / 0)

    try:
        print((1 / 0, 2)[condition])
    except Exception as e:
        print(exit)