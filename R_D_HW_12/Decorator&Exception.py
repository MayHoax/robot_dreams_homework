import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        with open('decoratorLogs.txt', 'a') as dl:
            dl.write(f'{func.__name__} called at {datetime.datetime.now()}\n')
        return func(*args, **kwargs)
    return wrapper


class MyCustomException(Exception):
    with open("ErrorMessages", 'a') as em:
        em.write(f"MyCustomException is occured at {datetime.datetime.now()}\n")





