from promotions import Promotion


class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self._promotion = None

    def get_promotion(self) -> Promotion:
        return self._promotion

    def set_promotion(self, promotion: Promotion):
        if promotion is not None and not isinstance(promotion, Promotion):
            raise TypeError("promotion is an instance of Promotion class")
        self._promotion = promotion

    def is_active(self):
        return self.quantity > 0

    def buy(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock available")
        self.quantity -= amount
        if self._promotion:
          return self._promotion.apply_promotion(self, amount)
        return self.price * amount

    def show(self):
        promotion_text = f" - Promotion: {self._promotion.name}" if self._promotion else ""
        return f" {self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_text}"


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def is_active(self):
        return True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, amount):
        if amount > self.maximum:
            raise ValueError("Cannot purchase more than the allowed limit")
        return super().buy(amount)