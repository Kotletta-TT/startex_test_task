from django.db import models
from .models import Product
import csv

"""
Сопоставление полей:
- Артикул = "ПТ"+"КодТовараПоставщика"
- Наименование товара = "НаименованиеТовараПоставщика"
- Цена закуп = 0.9 * "ЦенаПоставщика"
- Цена розница = если "ЦенаПоставщика" < 1000 руб, то 1.2 * "ЦенаПоставщика". иначе 1.1 * "ЦенаПоставщика
"""

filename = 'goods.csv'


def product_autoload():
    with open(filename, 'r', newline='') as file:
        csv_read = csv.reader(file, delimiter=';', quotechar=' ')
        for row in csv_read:
            try:
                sku = 'ПТ' + str(row[0])
                name = str(row[1])
                wholesale_price = round(0.9 * float(row[2]))
                price = round(1.2 * float(row[2])) if int(row[2]) < 1000 else round(1.1 * float(row[2]))
                product = Product(sku=sku, name=name, wholesale_price=wholesale_price, price=price)
                product.save()
            except ValueError as e:
                """
                Тут должен быть лог ошибки
                """
                continue

