'''
Samples:

@pytest.fixture
def simple_fixture(): ...

@pytest.fixture(scope='session')
def session_fixture(): ...

@dataclass
class SimpleDataclass: ...

@dataclass(slots=True)
class SimpleDataclass:

В одном случае - 2 уровня вложенности, а в другом 3
Но всё решается просто - добавляем четвёртый уровень вложенности
Совмещаем обычный декоратор и декоратор с параметрами вместе и получаем:
'''
from functools import wraps


def schrodinger_decorator(
        call=None,
        *,
        arg1=None,
        arg2=None
):
    wrap_decorator = decorator_wrapper(arg1, arg2)

    # если мы использовали декоратор
    # как декоратор с параметрами
    if call is None:
        return wrap_decorator

    # если мы использовали декоратор как обычный
    # arg1 и arg2 при этом принимают
    # значения по умолчанию
    else:
        return wrap_decorator(call)


'''
При этом все аргументы должны иметь значения по умолчанию так как в одном случае у нас будет передаваться только call, 
в другом - только дополнительные аргументы

Затем мы отдельно пишем декоратор с параметрами ещё раз
'''


def decorator_wrapper(arg1, arg2):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(func.__name__, arg1, arg2)
            return func(*args, **kwargs)
        return wrapper
    return real_decorator


# call=func, arg1=None, arg2=None
@schrodinger_decorator
def func1(): ...


# call=None, arg1=1, arg2=2
@schrodinger_decorator(arg1=1, arg2=2)
def func2(): ...


if __name__ == '__main__':
    func1()
    func2()
