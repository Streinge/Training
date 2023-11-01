# использование декораторов для обработки исключений,
# мало что понятно, но можно все найти на хекслете в
# уроке про декораторы иименно такая конструкция
# заставляет Пайтон сначала принимать параметры
# декоратора, вложенный декортатор принимает саму
# оборачиваемую функцию, и следюущая обертка принимает
# параметры оборачиваемой функции - вот такая жесть
def suppress(exp, or_return=None):
    def inner(fun):
        def wrapper(*args, **kwargs):
            try:
                return fun(*args, **kwargs)
            except exp:
                # в этой строчке сбили с толку примерами
                # у них здесь стоит в примерах print,
                # то есть печатается что-то, а надо
                # возвращать это значение, по условию задачи,
                # а я невнимательно прочитал и промучался несколько часов
                return or_return
        return wrapper
    return inner


@suppress(ZeroDivisionError, or_return=42)
def foo():
    return 1 // 0


@suppress((KeyError, IndexError))
def get_item(key, structure):
    return structure[key]


@suppress(ZeroDivisionError, or_return=0)
def safe_div(a, *, b):
    return a // b


print(foo())  # 42

print(get_item(7, "foo") is None)  # True
print(get_item('a', {}) is None)  # True

print(safe_div(10, b=3))
print(safe_div(10, b=0))
