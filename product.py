class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}")

    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name, "price": self.__price, "stock": self.__stock}
    
