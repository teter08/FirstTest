class InfinityIterator:
    def __init__(self):
        self.index = -10

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 10
        return self.index


a = iter(InfinityIterator())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
