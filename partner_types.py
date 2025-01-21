
class Partner:

    def __init__(self,
                 partner_id,
                 partner_type,
                 name,
                 director,
                 email,
                 phone,
                 address,
                 inn,
                 rating,
                 discount=0
                 ):
        self.partner_id = partner_id
        self.partner_type = partner_type
        self.partner_name = name
        self.partner_director = director
        self.partner_email = email
        self.partner_phone = phone
        self.partner_address = address
        self.partner_inn = inn
        self.partner_rating = rating
        self.partner_discount = discount


class Product:

    def __init__(self, product_id, articul, name, cost):
        self.product_id = product_id
        self.articul = articul
        self.name = name
        self.cost = cost

class Sale:

    def __init__(self, sale_id, partner, product, count):
        self.sale_id = sale_id
        self.partner = partner
        self.product = product
        self.count = count
