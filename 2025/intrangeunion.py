from bisect import bisect

# Example
# Suppose the current ranges are 5-20, 23-41, 50-65, 68-80, 90-96
# They are represented in x by the array (always of even length)
#  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9
#  5 | 20 | 23 | 41 | 50 | 65 | 68 | 80 | 90 | 96
#   ===       ===       ===       ===       ===
# (bars show the ranges)
#
# What if we want to add 30-67?
#
# The general algorithm is to find where 30 and 67 would fall in this.
# We do this efficiently using the bisect package.
#
# There are some edges cases to consider such as when there is an exact match,
# when the inserted range is at the ends, or when ranges are adjacent such as
# in this example where the new ranges will be 5-20, 23-80, 90-96 (because
# 67 and 68 are integer adjacent).
#


class IntRangeUnion:
    def __init__(self, rangearray=None):
        if rangearray is None:
            self.rangearray = []
        else:
            for i, (a, b) in enumerate(zip(rangearray, rangearray[1:])):
                if i % 2 == 0:  # a-b is a range
                    assert a <= b
                else:  # adjacent ranges: x-a, b-y
                    assert a < b - 1
            self.rangearray = rangearray

    def union(self, a, b):
        assert a <= b
        assert len(self.rangearray) % 2 == 0
        i = bisect(self.rangearray, a)
        j = bisect(self.rangearray, b, lo=i)
        insert = []
        if i % 2 == 0:
            # Start of range (a) lands outside a range or directly adjacent to one
            if i != 0 and (
                self.rangearray[i - 1] == a - 1 or self.rangearray[i - 1] == a
            ):
                # Adjacent => merge
                i -= 1
            else:
                insert.append(a)
        if j % 2 == 0:
            if j != len(self.rangearray) and self.rangearray[j] == b + 1:
                j += 1
            else:
                insert.append(b)
        newarray = self.rangearray = self.rangearray[:i] + insert + self.rangearray[j:]
        assert len(newarray) % 2 == 0
        self.rangearray = newarray

    def __len__(self):
        """Returns the number of ranges making up the union.
        We try to make this unique by ensuring there are no adjacent ranges.
        For instance, [1, 3] + [4, 5] would always be represented as [1,5] instead."""
        return self.rangearray // 2

    def area(self):
        total = 0
        for a, b in zip(self.rangearray[::2], self.rangearray[1::2]):
            assert a <= b
            total += b - a + 1
        return total

    def aslist(self):
        return self.rangearray
