import unittest
from cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        # This runs BEFORE every single test method
        print("Setting up cart...")
        self.cart = ShoppingCart()

    def tearDown(self):
        # This runs AFTER every single test method
        print("Tearing down...")
        # Here you might self.cart.empty() or driver.quit()
        pass

    def test_add_one_item(self):
        self.cart.add_item("apple")
        self.assertEqual(self.cart.get_item_count(), 1)
        self.assertIn("apple", self.cart.items)

    def test_add_two_items(self):
        self.cart.add_item("apple")
        self.cart.add_item("banana")
        self.assertEqual(self.cart.get_item_count(), 2)
        self.assertIn("banana", self.cart.items)

    def test_remove_item(self):
        self.cart.add_item("apple")
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.get_item_count(), 0)
        self.assertNotIn("apple", self.cart.items)

if __name__ == "__main__":
    unittest.main()
