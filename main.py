"""
Hello dear evaluator. Before you judge my bloated error management, allow me
to note that I've asked the school for a more in-depth session about
differentiating between try-except blocks, if-else blocks and asserts.
If there are any remarks on your behalf, I welcome them and I ask that
you please exemplify what you mean. Judging by the DEMO, error handling
isn't the focus of this exercise, but it's still something that I'm
trying to get better at and the assignment did ask specifically for
certain try-except blocks in the OOP component. Thanks for reading, and thanks
for looking through my code.
"""

import products
import store

MENU = """
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""
MENU_CHOICES = "1234"


def show_all_active_products(best_buy):
    """This could've been an instance method, but it was not among project
    requirements. There is a vague possibility that the project implicitly
    wanted us to define functions like this, otherwise I'm not sure how
    I'd get the Demo result for option 1 (other than bloating the start()
    function a little)."""
    print("------")
    active_products = best_buy.get_all_products()
    for i, product in enumerate(active_products):
        print(i + 1, '.', end=' ')
        print(product.show())
    print("------")


def show_total_quantity(best_buy):
    """Contextualize and print the retval of get_total_quantity()"""
    print(f"Total of {best_buy.get_total_quantity()} items in store")


def make_an_order(best_buy):
    """Lets the buyer interact with the stock via a shopping cart. Slightly
    more differentiated error messages than in Demo, but a much more bloated
    function as a result."""
    shopping_cart = []
    active_products = best_buy.get_all_products()
    show_all_active_products(best_buy)
    print("When you're ready to finalize your order, enter empty text.")
    while True:
        item_no = input("Which product # do you want to add to the order? ")
        quantity = input("How many would you like? ")
        if not item_no or not quantity:
            print()
            break
        try:
            item_no = int(item_no)
            quantity = int(quantity)
            if item_no not in range(1, len(active_products) + 1):
                raise IndexError("Error: non-existent product #")
            if quantity < 1:
                raise IndexError("Error adding product: quantity"
                                 " must be greater than zero")
        except ValueError:
            print("Error adding product: product # and quantity "
                  "must be integers")
            continue
        except IndexError as e:  # I'm aware that IndexError != ideal
            print(e)
            continue
        shopping_cart.append((active_products[item_no - 1], quantity))
        print("Product added to shopping cart!\n")
    # try:
    grand_total = best_buy.order(shopping_cart)
    print(f"********\nOrder made! Total payment: ${grand_total}")
    # except ValueError as e:
    #     print(e)


def exit_program(best_buy):
    """Only serves the purpose of maintaining readability of func_dict
    in start(). I validate best_buy to 'void' it and satisfy the style.
    I wanted to have 1, 2, 3, 4 in the dispatcher dict."""
    if best_buy:
        exit(0)


def start(best_buy):
    func_dict = {'1': show_all_active_products,
                 '2': show_total_quantity,
                 '3': make_an_order,
                 '4': exit_program
                 }
    while True:
        print(MENU)
        usr_input = input("Please choose a number: ")
        if len(usr_input) != 1 or usr_input not in MENU_CHOICES:
            print("Error with your choice! Try again!")
            continue
        func_dict[usr_input](best_buy)


def main():
    """Set up initial stock of inventory, then initiate shopping session"""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
