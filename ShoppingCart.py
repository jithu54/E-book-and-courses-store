class ShoppingItem(object):
    def __init__(self, prod, qty):
        self.product = prod
        self.quantity = qty
class ShoppingCart(object):
    def __init__(self):
        self.items = []
    def add_item(self, product, qty):
        sitem = ShoppingItem(product, qty)
        self.items.append(sitem)
    def remove_item(self, prod_id):
        for item in self.items:
            if item.product.product_id == prod_id:
                item_to_remove = item
        if item_to_remove != None:
            self.items.remove(item_to_remove)
    def compute_total(self):
        total = 0
        for item in self.items:
            total = total + item.product.price * item.quantity
        return total
    def apply_discount(self, total):
        if total > 100 and total < 750:
            total = total - (total * 20/100)
        elif total > 750 and total < 1000:
            total = total - (total * 25/100)
        else:
            total = total - (total * 5/100)
        return total
    def show_cart(self):
        for item in self.items:
            print('\t\t'+item.product.__str__().replace('\n','') + '\tqty=' + str(item.quantity))
    def clear_cart(self):
        for i in self.items:
            n=self.items.index(i)
            self.items.pop(n)
