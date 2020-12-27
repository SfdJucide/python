from functools import reduce

new_gen = [num for num in range(100, 1001) if num % 2 == 0]
print(reduce(lambda x, y: x * y, new_gen))