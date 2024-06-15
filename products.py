ZERO_COST = 0
ZERO_QTY = 0


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
        if quantity < 0:
            raise ValueError("'quantity' may not have a negative value")
        if price < 0:
            raise ValueError("'price' may not have a negative value")
        self.name = name
        self._price = float(price)
        self._quantity = quantity
        self.active = True
        self._promotion = None

    @property
    def price(self):
        """self._price 'getter', the property way.
        Enables that 'obj.price' gets self._price."""
        return self._price

    @price.setter
    def price(self, price: (float, int)):
        """self._price 'setter', the property way.
        Enables that 'obj.price = ' sets self._price, while also granting
        the ability to perform error checks, which increases robustness."""
        if not isinstance(price, (float, int)):
            raise TypeError("Prices may only be numeric.")
        if price < 0:
            raise ValueError("'price' may not have a negative value")
        self._price = price

    @property
    def quantity(self):
        """self._quantity 'getter', the property way."""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """self._quantity 'setter', the property way.
        Also, deactivate if quantity == 0."""
        if not isinstance(quantity, int):
            raise TypeError("Item quantity may only be expressed in int")
        if quantity < 0:
            raise ValueError("'quantity' may not have a negative value")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()
        if self._quantity and not self.is_active():
            self.activate()

    def is_active(self):
        """Return the boolean value of the 'active' attribute"""
        return self.active

    def activate(self):
        """Set the 'active' attribute to True"""
        self.active = True

    def deactivate(self):
        """Set the 'active' attribute to False"""
        self.active = False

    @property
    def promotion(self):
        """Promotion 'getter', the property way."""
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """Promotion 'setter', the property way."""
        self._promotion = promotion

    def __repr__(self):
        """Contextualize and return an overview of name, price, qty."""
        me = f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
        me += ', Promotion: ' + f"{self.promotion}"
        return me

    def __lt__(self, other):
        """Overload '<'."""
        if not isinstance(other, Product):
            raise TypeError("Can't compare apples and oranges.")
        if self.price < other.price:
            return True
        return False

    def __gt__(self, other):
        """Overload '>'."""
        if not isinstance(other, Product):
            raise TypeError("Can't compare apples and oranges.")
        if self.price > other.price:
            return True
        return False

    def buy(self, quantity: int):
        """Subtract quantity parameter from Product instance's stock qty and
        return the cost of said subtraction if all checks are passed"""
        if not self.is_active():
            print(f"{self.name} had been deactivated.")
            return ZERO_COST
        if quantity > self.quantity:
            raise ValueError(f"No {quantity} in stock, try fewer.")
        self.quantity -= quantity
        if self.promotion:
            # this is madness, OOP is wild
            return self.promotion.apply_promotion(self, quantity)
        return quantity * self.price


class NonStockedProduct(Product):
    """Unlimited stock count subclass (ex.: digital licenses)"""
    def __init__(self, name: str, price: float):
        """Instantiate superclass with ZERO_QTY, this gets inherited"""
        super().__init__(name, price, ZERO_QTY)

    @property
    def quantity(self):
        """Return quantity of this instance of Product"""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Prevent updating the quantity of this instance of Product"""
        pass

    def buy(self, quantity: int):
        """Omit superclass' quantity checks and simply charge the buyer"""
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return quantity * self.price

    def __repr__(self):
        """Override; return an overview of name, price, 'Unlimited'."""
        me = f"{self.name}, Price: ${self.price}, Quantity: Unlimited"
        me += ', Promotion: ' + f"{self.promotion}"
        return me


class LimitedProduct(Product):
    """Limited purchase count per order (ex.: shipping)"""
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """Instantiate superclass, add 'maximum' attribute"""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int):
        """Only allow buying of 'self.maximum' quantity. Raise ValueError
        if user's quantity argument is too high."""
        if not self.is_active():
            print(f"{self.name} currently not available.")
            return ZERO_COST
        if quantity > self.maximum:
            print(f"Removed {self.name} from cart: Can't do {quantity}, only "
                  f"{self.maximum} {self.name} per order.")
            return ZERO_COST
        self.quantity = self.quantity - self.maximum
        return self.maximum * self.price

    def __repr__(self):
        """Override; return an overview of name, price, max."""
        me = f"{self.name}, Price: ${self.price}, Limited to "\
             f"{self.maximum} per order!"
        me += ', Promotion: ' + f"{self.promotion}"
        return me
