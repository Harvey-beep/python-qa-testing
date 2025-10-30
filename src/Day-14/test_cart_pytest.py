import pytest
from cart import ShoppingCart

# A fixture is a function that sets up test data/objects
# It runs *before* the test that needs it.

@pytest.fixture
def empty_cart():
    print("FIXTURE: Creating an empty cart")
    return ShoppingCart()

# To use the fixture, add its name as a function argument
def test_add_one_item(empty_cart):
    empty_cart.add_item("apple")
    assert empty_cart.get_item_count() == 1
    assert "apple" in empty_cart.items

# Mini Project for Day 14
@pytest.mark.regression
def test_add_two_items(empty_cart):
    empty_cart.add_item("apple")
    empty_cart.add_item("banana")
    assert empty_cart.get_item_count() == 2

# You can mark tests
@pytest.mark.smoke
def test_remove_item(empty_cart):
    empty_cart.add_item("apple")
    empty_cart.remove_item("apple")
    assert empty_cart.get_item_count() == 0

