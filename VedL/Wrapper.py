import time
import datetime
# import django

def timeis(functime):
    def wrap(*args, **kwargs):
        start = time.time()
        result = functime(*args, **kwargs)
        end = time.time()

        print(functime.__name__, end-start)
        return result
    return wrap

@timeis
def countd(n):
    while n > 0:
        n -= 1

countd(5)
countd(1000)

