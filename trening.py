"""Функция которая обьединяет данные из разных списков и оставляет
только уникальные значения в едином списке. C Тру списко сортируется,
без Тру, нет.
"""


def exclusuve_items(*args, key=False):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key == True:
        new_list.sort()
    return new_list


z = [1, 2, 3, 4, 5, 10]
x = [9, 8, 7, 10, 15]
c = [1, 1, 4, 7, 7, 9, 15]

t = exclusuve_items(z, x, c, key=True)
print(t)
