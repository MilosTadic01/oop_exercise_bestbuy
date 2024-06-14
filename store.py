from products import Product


class Store:
    """Implementation of 'composition concept', where a class holds reference
    to one or more instances of other classes."""
    def __init__(self, items_list: list):
        if not items_list:
            raise ValueError("Can't open store with no items")
        for item in items_list:
            if not isinstance(item, Product):
                raise TypeError("Store may only stock products")
        self.stock = items_list

    def add_product(self, product: Product):
        """Verify that the parameter is of class Product, then include it in
        store stock (a list of all products)."""
        if not isinstance(product, Product):
            raise TypeError("Store may only stock products")
        self.stock.append(product)

    def remove_product(self, product: Product):
        """Will raise ValueError if product not in list due to how .remove()
        works. I'm choosing not to apprehend that, and rather let it crash
        as an indicator of other points of failure."""
        self.stock.remove(product)

    def get_total_quantity(self):
        """Return total count of all items in stock"""
        items_count = 0
        for product in self.stock:
            items_count += product.quantity
        return items_count

    def get_all_products(self):
        """Return a list of all active product objects"""
        active_products = []
        for product in self.stock:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list: list):
        """Perform .buy() method from products.py for each tuple in
        'shopping_list'. Sums grand_total and returns it as the total
        price. shopping_list is a list of tuples. Tuple format:
        (product, qty). It is static because it will not .remove() a product
        that goes out of stock, only deactivate it (attribute of Product)"""
        grand_total = 0
        for product, quantity in shopping_list:
            try:
                cost = product.buy(quantity)
            except ValueError as err:
                print(f"{product.name}: {err}")
                continue
            if cost > 0:
                print(f"Successfully ordered {quantity} of {product.name} "
                      f"for ${cost}")
            grand_total += cost
        return grand_total
