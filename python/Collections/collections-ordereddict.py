from collections import OrderedDict

items = OrderedDict()

n = int(input())

for i in range(n):
    item, space, price = input().rpartition(" ")

    price = int(price)

    if item in items:
        items[item] += price
    else:
        items[item] = price

for item, price in items.items():
    print(item, price)
