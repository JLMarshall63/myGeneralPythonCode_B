#Example standard synchronous Python
#prints hello waits 3 sec the prints world
from time import sleep
def hello():
    print('Hello')
    sleep(3)
    print('World!')

if __name__ == '__main__':
    hello()