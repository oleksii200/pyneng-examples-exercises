# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов, которые есть
и в команде command1 и в команде command2 (пересечение).

В данном случае, результатом должен быть такой список: ['1', '3', '8']

Записать итоговый список в переменную result. (именно эта переменная будет
проверяться в тесте)

Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
res1 = command1.split()[-1]
res2 = command2.split()[-1]
res11 = res1.split(',')
res22 = res2.split(',')
res111 = set(res11)
res222 = set(res22)
res1111=list(res111)
res2222=list(res222)
res4=res111.intersection(res222)
result=list(res4)
result.sort()
#result=result1.sort(',')
#res3=res1+' '+res2
#res4=type(res3)
#res5=list(res3)
#res6=set(res5)
print (result)

