import time


def countdown(x):
    while x:
        minutes, seconds = divmod(x, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\n")
        time.sleep(1)
        x -= 1
    print('BOOM')


x = input('enter time in seconds: ')

countdown(int(x))
