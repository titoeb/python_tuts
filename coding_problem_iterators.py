

class Sentence:
    def __init__(self, string):
        self.string = string
        self.idx = 0
        self.words = string.split(' ')

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.words):
            self.idx += 1
            return self.words[self.idx - 1]
        else:
            raise StopIteration()

my_sentence = Sentence("This is a test")
for word in my_sentence:
    print(word)