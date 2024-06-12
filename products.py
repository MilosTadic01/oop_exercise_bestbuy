ZERO_COST = 0


class Product:
    """Class of items to stock with attributes name, price, quantity and
    with another attribute 'active' which will matter to the container"""
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("The parameter 'name' may not be empty")
        if not isinstance(price, (float, int)):
            raise TypeError("Price may only be expressed as purely numeric")
        if not isinstance(quantity, int):
            raise TypeError("Item quantity may only be expressed in int")
        if quantity < 1:
            raise ValueError("'quantity' must be 1+ to activate in stock")
        if price < 0:
            raise ValueError("'price' may not have a negative value")
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return quantity of this instance of Product"""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Update the quantity attribute to a new value.
        Also deactivate if quantity == 0."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return the boolean value of the 'active' attribute"""
        return self.active

    def activate(self):
        """Set the 'active' attribute to True"""
        self.active = True

    def deactivate(self):
        """Set the 'active' attribute to False"""
        self.active = False

    def show(self):
        """Contextualize and return an overview of name, price, qty."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int):
        """Subtract quantity parameter from Product instance's stock qty and
        return the cost of said subtraction if all checks are passed"""
        if not self.is_active():
            print(f"{self.name} had been deactivated")
            return ZERO_COST
        if quantity > self.get_quantity():
            raise ValueError(f"No {quantity} in stock, try fewer.")
        self.set_quantity(self.get_quantity() - quantity)
        return quantity * self.price
