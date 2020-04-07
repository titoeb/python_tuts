# Define iterator
class MyRange:
    
    def __init__(self, start, end):
        self.start = start
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        else:
            current = self.value
            self.value += 1    
            return current

# Define a generator
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

if __name__== "__main__":
    nums = MyRange(1, 10)
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))


    

    

    
