from datetime import datetime, timedelta, date
from random import randint


def print_db(dct: dict):
    print(tuple(dct))
    for el in zip(*dct.values()):
        print(f'{el},')


start = datetime(2020, 1, 1)
end = datetime(2023, 1, 1)

purchases = {'purchaseId': [], 'userId': [], 'itemId': [], 'date': []}
for i in range(1, 2001):
    purchases['purchaseId'].append(i)
    purchases['userId'].append(randint(1, 100))
    purchases['itemId'].append(randint(1, 500))
    purchases['date'].append(date.isoformat(start + timedelta(randint(0, (end - start).days))))

users = {'userId': [], 'age': []}
for j in range(1, 101):
    users['userId'].append(j)
    users['age'].append(randint(18, 80))

items = {'itemId': [], 'price': []}
for j in range(1, 501):
    items['itemId'].append(j)
    items['price'].append(randint(1000, 150_000))

print_db(users)
print_db(purchases)
print_db(items)