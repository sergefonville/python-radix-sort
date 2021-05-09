from radix_sort import RadixSorter
from random import shuffle
import unittest

class RadixSortTests(unittest.TestCase):
    def test_small_list(self):
        ns = list(range(0,2**6))
        shuffle(ns)
        rsorter = RadixSorter(ns)
        sorted_ns = rsorter.sort()
        self.assertTrue([0,1,2,3] == sorted_ns[:4] and [60,61,62,63] == sorted_ns[-4:])

    def test_medium_list(self):        
        ns = list(range(0,2**16))
        shuffle(ns)
        rsorter = RadixSorter(ns)
        sorted_ns = rsorter.sort()
        self.assertTrue([0,1,2,3] == sorted_ns[:4] and [65532,65533,65534,65535] == sorted_ns[-4:])

    def test_large_list(self):
        ns = list(range(0,2**24))
        shuffle(ns)
        rsorter = RadixSorter(ns)
        sorted_ns = rsorter.sort()
        self.assertTrue([0,1,2,3] == sorted_ns[:4] and [16777212,16777213,16777214,16777215] == sorted_ns[-4:])

if __name__ == '__main__':
    unittest.main()