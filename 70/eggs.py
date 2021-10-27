from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit=0):
        self.limit = limit
        self.n = 1

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.limit:
            result = f"{choice(COLORS)} egg"
            self.n += 1
            return result
        else:
            raise StopIteration
