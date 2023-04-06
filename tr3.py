"""функция высчитывающая обьем цилиндра в см3
большинство переменных локальны и блягодаря этому
не засоряется оперативная память. только 1 глобальная переменная PI."""
import math

PI = math.pi


def radius():
    n = float(input('диаметр цилиндра в см: '))
    n /= 2
    return n


def height():
    m = float(input('высота цилиндра в см: '))
    return m


def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h
    return v


print("обьем цилиндра",  volume(), "cм3")

def massa(g):
    n = float(input("удельный вес гр на см3: "))
    return g*n/1000


print("Вес цилиндра в кг: ", massa(volume()))
