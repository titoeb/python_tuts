import itertools

# counter = itertools.count()

# data = [100, 200 , 300, 400]

# daily_data = list(zip(counter, data))

# print(daily_data)

# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400]

# daily_data = list(itertools.zip_longest(range(10), data))

# print(daily_data)

# Iterate iterator infinitely.
# counter = itertools.cycle([1, 2, 3])

# for _ in range(20):
#     print(next(counter))


# counter = itertools.repeat(2, times=3)

# for element in counter:
#     print(element)

# letters = ['a', 'b' , 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['Corey', 'Nicole']

# result = itertools.permutations(letters, 2)

# for item in result:
#     print(item)

with open('test.log', 'r') as f:
    header = itertools.islice(f, 3)
    for line in header:
        print(line, end = '')