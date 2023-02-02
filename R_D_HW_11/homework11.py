import time


def name_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_name = func.__name__
        print(f'Function named {func_name} started at {time.ctime(start_time)}')
        return func(*args, **kwargs)

    return wrapper



class SepCode:
    def __enter__(self):
        print("=" * 10)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('=' * 10)
        if exc_val:
            print(f'{exc_type}: {exc_val}')
        return True



try:
    print('=' * 10)
except Exception as e:
    print(f' Some exception: {e}')
finally:
    print('=' * 10)


class MyCustomException(Exception):
    pass
raise MyCustomException('Custom exception is occured')
