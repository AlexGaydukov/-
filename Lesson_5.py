
from collections import namedtuple

b = {}
num = int(input ("Введите количество предприятий = "))
OOO = namedtuple('OOO', 'id_num name money ')

cost_n = 0
cost_nn = 0
for i in range(num):
    id_num = input ("Введите номер предприятия = ")
    name = input ("Введите имя предприятия = ")
    money = int(input ("Введите прибыль за 4-й квартал = "))
    b[i+1] = OOO(id_num, name, money)
    cost_n += b[i+1].money

cost_nn = cost_n/num
print()
for i in range (num):
    if (b[i+1].money - cost_nn) < 0:
        print ("У предприятия", b[i+1].name, "прибыль меньше среднего")
    else:
        print ("У предприятия", b[i+1].name, "прибыль вышего среднего")

