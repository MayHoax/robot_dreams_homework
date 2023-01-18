def fibonacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

while True:
    fib = fibonacci_generator()
    n = int(input("Enter a number: "))
    for i in range(n):
        next_fib = next(fib)
    print(next_fib)
#

# lst = [1, 'I', 'am', 2, 5, 'list']
# lst_iter = iter(lst)
# helper = len(lst)
# while helper != 0:
#     print(next(lst_iter))
#
#
# class Itario:
#     value = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value == 10:
#             raise StopIteration()
#         tmp_value = self.value
#         self.value += 1
#         return tmp_value
#
# maza = Itario()
# for i in maza:
#     print(i)
#     print('okay, whats next')
#
# class FibonacciIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         fib = self.a
#         if fib > self.limit:
#             raise StopIteration
#         self.a, self.b = self.b, self.a + self.b
#         return fib
#
# fib_iterator = FibonacciIterator(100)
# for fib in fib_iterator:
#     print(fib)