from Product import Product
import os.path
import pickle
class MyStore(object):
    def __init__(self):
        self.plist = []
    def Products(self,file_name):
        lines = open(file_name)
        plist = [] 
        for line in lines:
            parts = line[:-1].split(',')
            pr = Product(int(parts[0]),parts[1],float(parts[2]),parts[3])
            self.plist.append(pr)
    def display_products(self):
        for pr in self.plist:
            print(pr, end='')  

            
    def get_product(self, prod_id):
        for pr in self.plist:
            if pr.product_id == prod_id:
                return pr
        return None
    def add_product(self,prod_id,prod_name,price,category):
        count=0
        if float(price)<0:
            count=1
        for pr in self.plist:
            if pr.product_id==int(prod_id):
                count=1
                print("\nPlease change the Product_id. same product Id already exists.")
                break
        if count==0:
            pr=Product(int(prod_id),prod_name,float(price),category)
            self.plist.append(pr)
            print("\n Item Added Successfully.")
            count=0
    def remove_product(self,prod_id):
        count=0
        for pr in self.plist:
            if pr.product_id==int(prod_id):
                count=1
                self.plist.remove(pr)
                print("\n Item Removed Successfully")
                break
        if count==0:
            print("Inavlid product Id")

    def pickling_file(self,plist,scart):
        pickle_file=os.path.isfile("ShoppingApp.pkl")
        if pickle_file == True:
            print("pickle file saved")
        else:
            python_pickling="ShoppingApp.pkl"
            with open(python_pickling,'wb') as sm:
                pickle.dump(plist,sm)
                pickle.dump(scart,sm)
                print("pickle file created")
