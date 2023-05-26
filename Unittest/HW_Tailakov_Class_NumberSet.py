class NumberSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)