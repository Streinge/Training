class Counter:
    # инициализация класс счетчка с заданием начального
    # значения 0 и проверкой на неотрицательность
    def __init__(self, value=0):
        if value < 0:
            self.value = 0
        else:
            self.value = value
    # добавление метода который увеличивает значение
    # на дельту (по умолчанию 1) и ВОЗВРАЩАЕТ
    # новый экземпляр счетчика с прибавленным значением
    def inc(self, delta=1):
        # ЗДЕСЬ ВОЗРАЩАЕТСЯ ОБЪЕКТ СЧЕТЧИКА
        # то есть результатом исполнения МЕТОДА класса
        # будет ОБЪЕКТ ЭТОГО КЛАССА (ВНУТРИ КЛАССА ВЫЗЫВАЕТСЯ САМ КЛАСС)
        return Counter(self.value + delta)
    # здесь аналогично, только уменьшение счетчика
    # и есть проверка состояния счетчика на неотрицательность
    def dec(self, delta=1):
        if self.value - delta < 0:
            self.value = 0
        return Counter(self.value - delta)


c = Counter()
print(c.inc().inc(5).dec(2).value)

# Старый экземпляр не должен изменяться
d = c.inc(100)
print(d.dec().value)  # 99

forty_two = Counter(42)
print(forty_two.value)  # 42