import pytest
from products import Product, NonStockedProduct, LimitedProduct

def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100

def test_create_product_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)

def test_product_becomes_inactive():
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.is_active() == False

def test_product_purchase():
    product = Product("MacBook Air M2", price=1450, quantity=10)
    total_price = product.buy(3)
    assert product.quantity == 7
    assert total_price == 4350

def test_buying_more_than_exists():
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        product.buy(10)
