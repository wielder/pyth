"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
a = 'разработка'
b = 'администрирование'
c = 'protocol'
d = 'standard'

lst = [a, b, c, d]

bts = []
for i in lst:
    j = i.encode('utf-8')
    bts.append(j)

print(bts)
print()

strv = []
for i in bts:
    j = i.decode('utf-8')
    strv.append(j)


print(strv)
