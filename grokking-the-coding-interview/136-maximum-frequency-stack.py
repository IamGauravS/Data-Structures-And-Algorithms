class FreqStack:
    def __init__(self):
        self.stack = []
        self.value_count = {}

    def push(self, value):
        self.stack.append(value)
        if value not in self.value_count:
            self.value_count[value] = [0, -1]
        curr = self.value_count[value]
        curr[0] += 1
        curr[1] = len(self.stack)
        self.value_count[value] = curr

    def pop(self):
        max_frequency = 0
        max_index = -1
        max_value = None

        for value, (frequency, index) in self.value_count.items():
            if frequency > max_frequency or (frequency == max_frequency and index > max_index):
                max_frequency = frequency
                max_index = index
                max_value = value

        if max_value is not None:
            self.value_count[max_value][0] -= 1
            return max_value
