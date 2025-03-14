from abc import ABC, abstractmethod




class Promotion(ABC):
    """Abstract base class for promotion"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
      """Apply promotion to a product purchase and return discounted price"""


class PercentageDisscount(Promotion):
     """Promotion for percentage discount"""

     def __init__(self, name: str, discount_percent:float):
         super().__init__(name)
         self.discount_percent = discount_percent / 100


     def apply_promotion(self, product, quantity: int) -> float:
        from products import Product
        original_price = product.price * quantity
        discounted_price = original_price * (1 - self.discount_percent)
        return discounted_price

class SecondhalfPrice(Promotion):
    """Promotion second item is half price"""

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
         from products import Product
         if quantity < 2:
             return product.price * quantity

         pairs = quantity // 2
         singles = quantity % 2

         discounted_price = (pairs * product.price + (product.price * 0.5)) + (singles * product.price)
         return discounted_price


class BuyTwoGetOneFree(Promotion):
    """Promotion buying 2 items get 1 free"""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
         from products import Product
         if quantity < 3:
             return prduct.price * quantity

         sets_of_three = quantity // 3
         remainder = quantity % 3

         discounted_price = (sets_of_three * 2 * product.price) + (remainder * product.price)
         return discounted_price
