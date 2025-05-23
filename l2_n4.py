class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    @property
    def current_value(self):
        return self.value

counter = Counter()
print("Начальное значение счетчика:", counter.current_value)

counter.increment()
print("После увеличения:", counter.current_value)

counter.decrement()
print("После уменьшения:", counter.current_value)