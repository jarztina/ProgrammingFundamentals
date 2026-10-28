#never calls for input()

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
            return None

    def to_list(self):
        return [p.to_dict() for p in self.__products]
      