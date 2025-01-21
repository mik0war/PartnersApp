import psycopg2

from partner_types import Product, Partner, Sale

connection = psycopg2.connect("dbname=demo "
                                  "host=localhost "
                                  "port=5432 "
                                  "user=postgres "
                                  "password=root ")

cursor = connection.cursor()

cursor.execute("select * from products")
product_data_from_db = cursor.fetchall()
product_data = [Product(x[0], x[3], x[2], x[4]) for x in product_data_from_db]

cursor.execute("select * from partners")
partner_data_from_db = cursor.fetchall()
partner_data = [Partner(x[0], x[1], x[2], f'{x[3]} {x[4]} {x[5]}', x[6], x[7], f'{x[8]}, {x[9]}, {x[10]}, {x[11]}, {x[12]}', x[13], x[14]) for x in partner_data_from_db]

cursor.execute("select * from partner_products")
sale_data_from_db = cursor.fetchall()
sale_data = [Sale(x[0], x[2], x[1], x[3]) for x in sale_data_from_db]


cursor.close()
connection.close()


"""
Алгоритм расчета скидок:

+ 1. Получить все продажи по конкретному партнёру
+ 2. Получить цены товаров, которые были проданы 
    и установить соответствие
+ 3. Получить общую стоимость проданных товаров: 
    сумма произведений количество 
    товара в одной продаже на цену товара
+ 4. Рассчитать скидку по условиям

"""

def calculate_discount(partner : Partner):
    ### 1-й блок: получение итогового размера стоимости продаж
    partner_sale = []

    for sale in sale_data:
        if sale.partner == partner.partner_id:
            partner_sale.append(sale)

    sales_with_products = dict()

    for sale in partner_sale:
        for product in product_data:
            if sale.product == product.product_id:
                sales_with_products[sale] = product

    total_price = 0
    for sale in partner_sale:
        total_price += sale.count * sales_with_products[sale].cost

    ### 2-й блок: получение скидки
    if total_price < 10_000:
        partner.partner_discount = 0
    elif 10_000 <= total_price < 50_000:
        partner.partner_discount = 5
    elif 50000 <= total_price < 300000:
        partner.partner_discount = 10
    else:
        partner.partner_discount = 15

'''
    Алгоритм:
    1. Получить список партнёров
    2. Посчитать скидку для каждого
'''

def calculate_all_discounts():
    partners = partner_data

    for partner in partners:
        calculate_discount(partner)


if __name__ == '__main__':
    calculate_all_discounts()

    a=100

