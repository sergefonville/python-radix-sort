from functools import reduce

class BucketRadixSorter():
    def __init__(self, ns):
        self.__empty_buckets()
        self.__ns = ns

    def sort(self):
        for index in range(self.__max_digits()):
            for n in self.__ns:
                bucket = self.__select_bucket(n, index)
                self.__buckets[bucket].append(n)
            self.__flatten()
            self.__empty_buckets()
        return self.__ns
    
    def __select_bucket(self, n, index):
        bucket = (n // (10**index)) % 10
        return bucket

    def __flatten(self):
        self.__ns = reduce(lambda x,y: x + y, self.__buckets)

    def __max_digits(self):
        highest_n = max(self.__ns)
        digits = len(str(highest_n))
        return digits

    def __empty_buckets(self):
        self.__buckets = [[] for i in range(10)]