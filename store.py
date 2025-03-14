from typing import List
from products import Product


class Store:
    """Represents a store with products."""
    def __init__(self, product_list: List[Product]):
        """Initialize the store with a list of products."""
        if not isinstance(product_list, list) or not all(isinstance(p, Product) for p in product_list):
            raise TypeError("product_list must be a list of Product instances.")
        self.products = product_list

    def add_product(self, product: Product):
        """Add a product to the store's inventory."""
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product.")
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store's inventory."""
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product.")
        if product not in self.products:
            raise ValueError("Product does not exist in the store.")
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Process an order for a list of products and quantities.

        Args:
            shopping_list: A list of tuples containing products and their quantities.

        Returns:
            The total price of the order.

        Raises:
            ValueError: If a product in the shopping list is not available.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if not isinstance(product,Product) or not isinstance(quantity, int):
                raise TypeError("Each item in the shopping list must be a tuple of (Product, int quantity).")
            if product in self.products and product.is_active():
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Product {product.name} is not available.")
            return total_price
