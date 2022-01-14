"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ya = ['ping', 'yandex.ru']
ya_p = subprocess.Popen(ya, stdout=subprocess.PIPE)
for i in ya_p.stdout:
    res = chardet.detect(i)
    print(res)
    i = i.decode(res['encoding']).encode('utf-8')
    print(i.decode('utf-8'))

you = ['ping', 'youtube.com']
you_p = subprocess.Popen(you, stdout=subprocess.PIPE)
for i in you_p.stdout:
    res = chardet.detect(i)
    print(res)
    i = i.decode(res['encoding']).encode('utf-8')
    print(i.decode('utf-8'))