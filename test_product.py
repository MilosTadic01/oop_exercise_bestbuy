"""It appears that it is not possible to have multiple function calls within
the same 'with' block, which might make sense logically, but was a surprise"""

import pytest
from products import Product


def test_product_obj_instantiation_regular():
    """My intuition is that a single test suffices to confirm the base case"""
    product = Product('Earplugs', 20, 50)
    assert isinstance(product, Product)


def test_product_obj_instantiation_invalid_args():
    """Test for invalid values as well as for invalid arg types"""
    with pytest.raises(ValueError):
        Product('', 20, 50)
    with pytest.raises(ValueError):
        Product('Earplugs', 20, -1)
    with pytest.raises(ValueError):
        Product('Earplugs', 20, -50)
    with pytest.raises(ValueError):
        Product('Earplugs', -20, 50)
    with pytest.raises(TypeError):
        Product('Earplugs', 20, 1.22)
    with pytest.raises(TypeError):
        Product('Earplugs', 20, 'cat')
    with pytest.raises(TypeError):
        Product('Earplugs', 20, {1: 20})
    with pytest.raises(TypeError):
        Product('Earplugs', 20, [1, 2])
    with pytest.raises(TypeError):
        Product('Earplugs', 20, None)
    with pytest.raises(TypeError):
        Product('Earplugs', {1: 20}, 50)
    with pytest.raises(TypeError):
        Product('Earplugs', [], 50)
    with pytest.raises(TypeError):
        Product('Earplugs', 'cat', 50)
    with pytest.raises(TypeError):
        Product('Earplugs', type('cat'), 50)
    with pytest.raises(TypeError):
        Product('Earplugs', None, 50)


def test_product_obj_deactivated_and_reactivated():
    product = Product('Earplugs', 20, 50)
    assert product.is_active()
    product.buy(50)
    assert not product.is_active()
    product = Product('Earplugs', 20, 50)
    product.quantity = 0
    assert not product.is_active()
    product.quantity = 1
    assert product.is_active()


def test_product_obj_purchasing_properly():
    """Test that product purchase modifies qty and returns correct value"""
    product = Product(' Earplugs', 20, 50)
    assert product.buy(2) == 40
    assert product.quantity == 48
    assert product.buy(48) == 960
    assert product.quantity == 0
    assert product.buy(2) == 0


def test_product_obj_buy_too_much():
    """Test that qty > stock raises a ValueError"""
    product = Product('Earplugs', 20, 50)
    with pytest.raises(ValueError):
        product.buy(51)


pytest.main()
