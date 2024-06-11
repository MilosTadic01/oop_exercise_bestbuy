ZERO_PRICE = 0


class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("The parameter 'name' may not be empty")
        if type(quantity) is not int:
            raise TypeError("Item quantity may only be expressed in int")
        if price < 0 or quantity < 0:
            raise ValueError("The parameters 'price' and "
                             "'quantity' may not have negative values")
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.is_active():
            print(f"{self.name} had been deactivated")
            return ZERO_PRICE
        if quantity > self.get_quantity():
            raise ValueError(f"No {quantity} in stock, try fewer.")
        self.set_quantity(self.get_quantity() - quantity)
        return quantity * self.price


# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()

        # try:
        #     self.price = float(price)
        # except TypeError:
        #     print("Price attribute takes floats")
        # except AttributeError as e:
        #     print(e, ": assignment failed")