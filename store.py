from products import Product

STOCK_TYPE_ERROR_MSG = "Store may only stock items of <class 'Product'>"


class Store:
    """Implementation of 'composition concept', where a class holds reference
    to one or more instances of other classes."""
    def __init__(self, items_list: list):
        if not items_list:
            raise ValueError("Can't add non-specified Products, abort")
        for item in items_list:
            if not isinstance(item, Product):
                raise TypeError(STOCK_TYPE_ERROR_MSG + f", not {type(item)}.")
        self.stock = items_list

    def add_product(self, product: Product):
        """Verify that the parameter is of class Product, then include it in
        store stock (a list of all products)."""
        if not isinstance(product, Product):
            raise TypeError(STOCK_TYPE_ERROR_MSG + f", not {type(product)}.")
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

    def __contains__(self, item):
        """Check if obj <item> is among stocked products."""
        if not isinstance(item, Product):
            raise TypeError(STOCK_TYPE_ERROR_MSG + f", not {type(item)}.")
        if item in self.stock:
            return True
        return False

    def __add__(self, other):
        """Combine the stocks of two stores to open a new store and remove
        the products from the original stores. If match between product names
        among the two stores, only update the quantity rather than adding as
        separate instance."""
        if not isinstance(other, Store):
            raise TypeError("May only concat <class 'Store'> with own type.")
        combined_products = []
        for product in self.get_all_products():
            combined_products.append(product)
            self.remove_product(product)
        for product in other.get_all_products():
            for stocked_in_new_store in combined_products:
                if product.name == stocked_in_new_store.name:
                    stocked_in_new_store.quantity += product.quantity
                    break
            else:
                combined_products.append(product)
            other.remove_product(product)
        return Store(combined_products)

    def __repr__(self):
        """Contextualize and print the retval of self.get_all_products().
        Transferred the function which was originally in main to present
        the products listing when overloading __repr__."""
        me = "------\n"
        active_products = self.get_all_products()
        for i, product in enumerate(active_products):
            me += f"{i + 1}. {product}\n"
        me += "------\n"
        return me

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
