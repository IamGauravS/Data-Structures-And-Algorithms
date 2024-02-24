class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, val):
        while i <= self.size:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        sum = 0
        while i:
            sum += self.tree[i]
            i -= i & -i
        return sum

    def range_query(self, i, j):
        return self.query(j) - self.query(i - 1)