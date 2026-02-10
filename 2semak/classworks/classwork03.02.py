class Shop:
    def __init__(self, price, name):
        self.price = price
        self.name = name
    def discount_price():
        pass
    
class Product1(Shop):
    def discount_price(self):
        return self.price - (self.price*0.9)
    
class Product2(Shop):
    def discount_price(self):
        return self.price - (self.price*0.7)
    
pr=[Product1(1000, "govno"), Product2(500, "ponos")]

for i in pr:
    print(i.discount_price())