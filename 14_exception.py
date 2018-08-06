if __name__ == '__main__':

    try:
        file = open('test.txt', 'rb')
    except (IOError, EOFError) as e:
        print('An error occurred. {}'.format(e.args[-1]))

    try:
        file = open('test.txt', 'rb')
    except EOFError as e:
        print('An EOFError occurred.')
        # raise e
    except IOError as e:
        print('An IOError occurred.')
        # raise e

    # finally
    try:
        file = open('test.txt', 'rb')
    except IOError as e:
        print('An IOError occured. {}'.format(e.args[-1]))
    finally:
        print('This would be printed whether or not an exception occured!')

    # try/else
    try:
        print('I am sure no exception is going to occur!')
    except Exception:
        print('exception')
    else:
        print(
            'This would only run if no exception occurs. And an error here would NOT be caught.'
        )
    finally:
        print('This would be printed in every case.')