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
#Here we're getting an iterator from the given iterable and we're initializing a cache value to SENTINEL, which is a unique sentinel value that we've defined.

#We then make a __iter__ method that returns self (which is required of all iterators) and a __next__ method which will check whether self.cache has a non-SENTINEL value to be returned. If it does, we return self.cache and we call next on self.iterator otherwise.

#Our peekable object also has a peek method which is what populates self.cache. If we have nothing in our cache, we call next on self.iterator, passing self.SENTINEL as the default value to next. If SENTINEL was returned, we either raise a StopIteration exception or return default, depending on whether default is SENTINEL (no default was provided) or not.

#If no default value was returned and no StopIteration exception was raised, we return self.cache at the end of our peek method.
