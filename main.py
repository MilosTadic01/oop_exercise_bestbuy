"""
Hello dear evaluator. Before you judge my bloated error management, allow me
to note that I've asked the school for a more in-depth session about
differentiating between try-except blocks, if-else blocks and asserts.
If there are any remarks on your behalf, I welcome them and I ask that
you please exemplify what you mean. That would be great help to me.
Judging by the DEMO, error handling isn't the focus of this exercise,
but it's still something that I'm trying to get better at and the assignment
did ask specifically for certain try-except blocks in the OOP component.
Thanks for reading, and thanks for looking through my code.
"""

import sys
import products
from store import Store

MENU_CHOICES = "1234"
MENU = """
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""


def show_all_active_products(best_buy: Store):
    """This could've been an instance method, but it was not among project
    requirements. There is a vague possibility that the project implicitly
    wanted us to define functions like this, otherwise I'm not sure how
    I'd get the Demo result for menu options (other than bloating the start()
    function by a lot)."""
    print("------")
    active_products = best_buy.get_all_products()
    for i, product in enumerate(active_products):
        print(i + 1, '.', end=' ')
        print(product.show())
    print("------")


def show_total_quantity(best_buy: Store):
    """Contextualize and print the retval of get_total_quantity()"""
    print(f"Total of {best_buy.get_total_quantity()} items in store")


def make_an_order(best_buy: Store):
    """Lets the buyer interact with the stock via a shopping cart. Slightly
    more differentiated error messages than in Demo, but a much more bloated
    function as a result."""
    shopping_cart = []
    active_products = best_buy.get_all_products()
    show_all_active_products(best_buy)
    print("When you're ready to finalize your order, enter empty text.")
    while True:
        item_no = input("\nWhich product # do you want to add to the order? ")
        quantity = input("How many would you like? ")
        if not item_no or not quantity:  # done-adding-to-cart condition
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
        except IndexError as err:  # I'm aware that IndexErr != ideal ErrType...
            print(err)
            continue
        except ValueError:  # ...but I had to work around int() raising Value.
            print("Error adding product: product # and quantity "
                  "must be integers")
            continue
        shopping_cart.append((active_products[item_no - 1], quantity))
        print(f"\nYour request to add {quantity} of "
              f"<{active_products[item_no - 1].name}> to the shopping cart "
              "has been noted, I'll go look!\nAnything else? If not, press "
              "<RETURN> twice to finalize your order.")
    grand_total = best_buy.order(shopping_cart)
    if grand_total == 0:
        print("********\nHave you browsed our catalogue for more ideas?")
    else:
        print(f"********\nOrder success! Grand total: ${grand_total}")


def exit_program(best_buy: Store):
    """Only serves the purpose of maintaining readability of func_dict
    in start(). I validate best_buy to 'void' it and satisfy the style.
    I wanted to have 1, 2, 3, 4 in the dispatcher dict."""
    if best_buy:
        sys.exit(0)


def start(best_buy: Store):
    """Initialize dispatcher table once at start of runtime. Until exit,
    print interface menu for user and dispatch appropriate function."""
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
    product_list = [products.Product("MacBook Air M2", 1450, 100),
                    products.Product("Bose QuietComfort Earbuds", 250, 500),
                    products.Product("Google Pixel 7", 500, 250),
                    products.NonStockedProduct("Windows License", 125),
                    products.LimitedProduct("Shipping", 10, 250, 1)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
