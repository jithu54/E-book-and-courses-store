class Product(object):
    def __init__(self, prod_id, prod_name, price, category):
        self.product_id = prod_id
        self.product_name = prod_name
        self.price = price
        self.category = category
    def __str__(self):
        return '\n' +str(self.product_id) + '\t' + self.product_name + '\t\t' + str(self.price) + '\t' + self.category
    def __repr__(self):
        return '\n'+str(self.product_id) + '\t' + self.product_name + '\t\t' + str(self.price) + '\t' + self.category
