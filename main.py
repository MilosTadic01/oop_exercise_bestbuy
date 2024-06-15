import sys
import products
import promotions
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
    """Delegated the printout formatting to __repr__ of Store class."""
    print(best_buy)


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
        except IndexError as err:  # I'm aware that IndErr != ideal ErrType...
            print(err)
            continue
        except ValueError:  # ...but I had to work around int() raising ValEr.
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
    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    # Add promotions to products
    product_list[0].promotion = second_half_price
    product_list[1].promotion = third_one_free
    product_list[3].promotion = thirty_percent
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
