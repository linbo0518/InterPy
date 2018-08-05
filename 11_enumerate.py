if __name__ == '__main__':

    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):
        print(c, value)

    counter_list = list(enumerate(my_list, 1))
    print(counter_list)