from logic import calculate_discount
from mainwindow import setupUI
from repository import get_partners


'''
    Алгоритм:
    1. Получить список партнёров
    2. Посчитать скидку для каждого
'''

def main():

    partner_data = get_partners()

    for partner in partner_data:
        calculate_discount(partner)

    setupUI(partner_data)

if __name__ == '__main__':
    main()


