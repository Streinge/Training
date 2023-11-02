class HourClock:
    def __init__(self, hour=0):
        self.hour = hour
    # здесь все очень хитро казалось бы все можно сделать без свойства
    # но значение после например clock.hours += 5 меняется уже в ячейке
    # если поставить условия как в строках 14 и 16, то программа туда
    # уже на заходит
    @property
    def hours(self):
        return self.hour
    # сеттер нужен потому что при попытке сделать clock.hours += 5
    # появляется ошибка "AttributeError: can't set attribute".
    # это связано с атрибутами и свойствами, в общем я не понял.
    # но без сеттера нифига не работает
    @hours.setter
    def hours(self, new):
        self.hour = new
        # здесь я сделал условия посколькоу это 12 часовые часы 
        # чтобы стрелка находилась в пределах от 0 до 11
        if self.hour > 11:
            self.hour = self.hour - (self.hour // 12) * 12
        if self.hour < 0:
            self.hour = abs(self.hour - (self.hour // 12) * 12)


clock = HourClock()
print(clock.hours)  # 0
# в начале часовая стрелка всегда на нуле
clock.hours += 5
# ^ эквивалентно clock.hours = clock.hours + 5
print(clock.hours) # 5
clock.hours += 5
print(clock.hours)   # 10
clock.hours += 5
print(clock.hours)   # 3
clock.hours -= 4
print(clock.hours)   # 11
clock.hours = 123
print(clock.hours)   # 3