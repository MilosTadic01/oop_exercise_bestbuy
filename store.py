from products import Product


class Store:
    """Implementation of 'composition concept', where a class holds reference
    to one or more instances of other classes."""
    def __init__(self, items_list):
        if not items_list:
            raise ValueError("Can't open store with no items")
        for item in items_list:
            if not isinstance(item, Product):
                raise TypeError("Store may only stock products")
        self.stock = items_list

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Store may only stock products")
        self.stock.append(product)

    def remove_product(self, product):
        """Will raise ValueError if product not in list"""
        # if product not in self.products:
        #     return
        self.stock.remove(product)

    def get_total_quantity(self):
        items_count = 0
        for product in self.stock:
            items_count += product.get_quantity()
        return items_count

    def get_all_products(self):
        active_products = []
        for product in self.stock:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        grand_total = 0
        for product, quantity in shopping_list:
            try:
                grand_total += product.buy(quantity)
            except ValueError as e:
                print(f"{product.name}: {e}")
        return grand_total
