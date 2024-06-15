from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """An Abstract Class. Itself not capable of applying promotions.
    To satisfy the 'real abstract class' requirements in Python, this class
    also contains at least one abstract method. The 'pass' in it mandates
    that subclasses must actually define an implementation, 'override' it."""
    def __init__(self, name):
        """Only init the name in the Abstract parent class."""
        self._name = name

    def __repr__(self):
        """This did the trick so that __repr__ of Product instances, when no
        promotion applied, actually concatenate 'None' to the str."""
        return self._name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int):
        """Does specify the taking of 'self' because those subclasses which
        override this function will not be abstract, and neither will their
        overrides of this method."""
        pass


class SecondHalfPrice(Promotion):
    """Subclass of Abstract Class 'Promotion'. Itself non-abstract."""
    def __init__(self, name):
        """Initialize 'self._name' by doing so in superclass."""
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """Abstract Class subclass' methods do take self. As they themselves
        are not abstract. What's abstract about superclass is that it needs no
        instantiation or defined functionalities - it's able to just exist
        as a conceptual blueprint holder for any future subclasses."""
        total_after_promotion = 0
        items_count_half_price = quantity // 2
        items_count_full_price = quantity - items_count_half_price
        total_after_promotion += (items_count_full_price * product.price +
                                  items_count_half_price * product.price / 2)
        return total_after_promotion


class ThirdOneFree(Promotion):
    """Subclass of Abstract Class 'Promotion'. Itself non-abstract."""
    def __init__(self, name):
        """Initialize 'self._name' by doing so in superclass."""
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """Each third item comes at zero cost. 1st, 2nd and 4th are full $."""
        total_after_promotion = 0
        items_count_no_cost = quantity // 3
        items_count_full_cost = quantity - items_count_no_cost
        total_after_promotion += items_count_full_cost * product.price
        return total_after_promotion


class PercentDiscount(Promotion):
    """Subclass of Abstract Class 'Promotion'. Itself non-abstract."""
    def __init__(self, name, percent):
        """Initialize 'self._name' by doing so in superclass. Then set %."""
        super().__init__(name)
        self._percent = percent

    def apply_promotion(self, product, quantity):
        """If $100.00 headphones are 30% off, return float(70.00)"""
        discounted = product.price * (100 - self._percent) / 100 * quantity
        return discounted
