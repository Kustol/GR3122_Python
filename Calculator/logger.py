from datetime import datetime as dt


def logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Log.txt', 'a') as file:
        file.write('{}\n{}\n'.format(time, data))
        file.write('\n')