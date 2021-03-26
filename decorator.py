import time


def benchmark(func):
    '''Если я правильно понял benchmark должен показвать время выполнения функции'''
    def my_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения составило {end-start} секунд(ы).')
    
    return my_func


def logthis(fnc):
    def my_func(*args, **kwargs):
        print('До шифрования было:', args[0])
        res = fnc(*args, **kwargs)
        print('После шифрования стало:', res)
        return res
    return my_func


def counter(func):
    def my_func(*args, **kwargs):
        my_func.count += 1
        res = func(*args, **kwargs)
        print(f'{func.__name__} была вызвана: {my_func.count} раз(а)')
        return res
    my_func.count = 0
    return my_func


@benchmark
@logthis
@counter
def xor(stroka,key):
    """XOR шифрование
    На вход строка и ключ
    Возвращает зашифрованное XORом сообщение
    """
    s = ""
    for symbol in stroka:
        s += chr(ord(symbol)^key)
    #print(s)
    return s


xor('12345',3)
print()
xor('21076',3)
