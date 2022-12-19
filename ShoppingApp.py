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


from Product import Product
from ShoppingCart import ShoppingCart
from MyStore import MyStore
import pickle
import os.path
def main():
    fname = 'ProductsData.txt'
    store = MyStore()
    plist = store.Products(fname) 
    scart = ShoppingCart()
    main_menu = '1: View Products' + '\n' + '2: Shop' + '\n' + '3: Checkout' + '\n' +'4: Add Item' + '\n' +'5 : Remove Item' + '\n' + '0: Exit'
    shopping_menu = '\t1: Add Product to Cart' + '\n\t' + '2: Remove Product From Cart' + '\n\t' + '3: Show Cart' + '\n\t' +'4: Clear Cart' + '\n\t' + '0: back to main'
    menu_option = 1
    while menu_option > 0:
        print('\n'+main_menu)
        menu_option = input('please enter an option: ')
        menu_option = int(menu_option)
        if menu_option == 0:
            store.pickling_file(plist,scart)
            print('quitting application..')
            break 
        if menu_option == 1:
            store.display_products()
        if menu_option == 2:
            shopping_menu_option = 1
            while shopping_menu_option > 0: 
                print('\n'+shopping_menu)
                soption = input('\tplease enter a shopping option: ') 
                shopping_menu_option = int(soption)
                if shopping_menu_option == 1: # add to cart
                    prod_id_qty = input('\tplease enter productid,qty to buy (ex: 1001,3): ')
                    if (prod_id_qty.index(',')< 0):
                        print('invalid productid,qty specified..')
                    else:
                        parts = prod_id_qty.split(',')
                        prod_id = int(parts[0])
                        qty = int(parts[1])
                        pr = store.get_product(prod_id)
                        if pr != None:
                            scart.add_item(pr,qty)
                if shopping_menu_option == 2:
                    prod_id = input('\tplease enter productid to remove from cart:')
                    scart.remove_item(int(prod_id))
                if shopping_menu_option == 3:
                    scart.show_cart()
                if shopping_menu_option == 4:
                    scart.clear_cart()
        if menu_option == 3:
            total = scart.compute_total()
            print(total)
            total_after_discount = scart.apply_discount(total) 
            print('\n------check ot info---------') 
            print('Total Amount = ',total, ' Total Amount after discount=',total_after_discount)
        if menu_option==4: # add item to main_menu
            new_item=input("Please enter productid, productname, price and category: '+'\n(ex: 1002,badminton racquet,56.99,sports) : ");
            prod_id,prod_name,price,category=new_item.split(',')
            store.add_product(prod_id,prod_name,price,category)
        if menu_option==5: 
            remove_item=input("Please enter the product id that you want to remove : ")
            prod_id=int(remove_item)
            store.remove_product(prod_id)
main()
