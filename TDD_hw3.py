import math


'''
Домашняя работа №3 Задания 1-6.
В этой дз практически нет подводных камней, поэтому
написал короткий код функций для тестов и затем еще минимизировал его.
В 5 и 6 задании слегка изменил условие, в комментариях указал.

P.S. Написал "практически" потому что возможно какие-то не заметил :D
'''

def prime_numder(n):
    '''Определить, является ли введенное число простым'''
    if n % 2 == 0:
        return False
    k = 3
    while k **2 <= n and n % k != 0:
        if n % k == 0:
            return False
        k += 2
    return True


def HOD(a,b):
    '''Нахождение наибольшего общего делителя'''
    return math.gcd(a, b)


def HOK(a,b):
    '''Нахождение наименьшего общего кратоного'''
    return(a * b // HOD(a,b))


def xor(stroka,key):
    """XOR шифрование
    На вход строка и ключ
    Возвращает зашифрованное XORом сообщение
    """
    s = ""
    for symbol in stroka:
        s += chr(ord(symbol)^key)
    return s


def usedigits(start,end,n):
    """Частота использования цифры в диапазоне чисел
    На вход начало и конец диапазона и цифра
    Возвращает количество вхождений n
    """
    st = ''
    for s in range(start,end+1):
        st += str(s)
    n = str(n)
    return st.count(n)


def usealpha(stroka,n):
    """Частота использования символа в тексте
    На вход строка и символ
    Возвращает количество вхождений n
    """
    stroka, n = str(stroka), str(n)
    return stroka.count(n)


print(usealpha(' ',''))