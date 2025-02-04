
"""
Алгоритм расчета скидок для одного партнёра:

+ 1. Получить все продажи по конкретному партнёру
+ 2. Получить цены товаров, которые были проданы
    и установить соответствие
+ 3. Получить общую стоимость проданных товаров:
    сумма произведений количество
    товара в одной продаже на цену товара
+ 4. Рассчитать скидку по условиям

"""
from partner_types import Sale
from repository import get_connection


def calculate_discount(partner):
    ### 1-й блок: получение итогового размера стоимости продаж

    connection, cursor = get_connection()

    cursor.execute("SELECT partner, SUM(product_count * products.min_cost) "
                   "FROM partner_products JOIN products "
                   "ON products.product_id = partner_products.product "
                   "WHERE partner = %(id)s "
                   "GROUP BY partner;", {'id': partner.partner_id})
    sale_data_from_db = cursor.fetchall()
    sale_data = [Sale(x[0], x[1]) for x in sale_data_from_db]

    cursor.close()
    connection.close()
    total_price = 0
    for sale in sale_data:
        if sale.partner == partner.partner_id:
            total_price = sale.total_price
            break

    ### 2-й блок: получение скидки
    if total_price < 10_000:
        partner.partner_discount = 0
    elif 10_000 <= total_price < 50_000:
        partner.partner_discount = 5
    elif 50000 <= total_price < 300000:
        partner.partner_discount = 10
    else:
        partner.partner_discount = 15
