class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


# BEGIN (write your solution here)
class LimitedCounter(Counter):
    def __init__(self, limit):
        # c помощью фунции super() обращаюсь к метроду предка
        # чтобы получить доступ к value
        super().__init__()
        self.limit = limit
    # новая функция инкремент через доступ к родительсокй 
    # функции с помощьют super() и проверкой условиия не 
    # превышения лимита счетчика
    def inc(self, amount=1):
        super().inc(amount)
        if self.value > self.limit:
            self.value = self.limit

counter = LimitedCounter(limit=10)
counter.inc()
counter.inc(7)
print(counter.value)  # 8
counter.dec(10)
print(counter.value)  # 0
counter.inc(7)
counter.inc(7)
print(counter.value)  # 10
# END
