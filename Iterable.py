SENTINEL = object()
class peeakable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.cache = SENTINEL
    def __iter__(self):
        return self
    def __next__(self):
        if self.cache is not SENTINEL:
            value, self.cache = self.cache, SENTINEL
            return value
        return next(self.iterable)
    def peek(self, default = SENTINEL):
        if self.cache is SENTINEL:
            self.cache = next(self.iterator,SENTINEL)
            if self.cache is SENTINEL:
                if default is SENTINEL:
                    raise StopIteration
                else:
                    return default
        return self.cache