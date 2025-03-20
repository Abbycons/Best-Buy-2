from products import Product
from store import Store
from promotions import PercentageDisscount, SecondhalfPrice, BuyTwoGetOneFree

# Step 1: Define the LimitedProduct Class
class LimitedProduct(Product):
    def __init__(self, name, price, quantity, shipping_restriction):
        # Inherit from the Product class
        super().__init__(name, price, quantity)
        self.shipping_restriction = shipping_restriction

    def show(self):
        # Show product details including the shipping restriction
        product_details = super().show()
        return f"{product_details} | Shipping: {self.shipping_restriction}"

def list_products(store):
    """List all products in the store."""
    print("\nProducts in store:")
    for product in store.get_all_products():
        print(product.show())

def show_total_quantity(store):
    """Show the total quantity of items in the store."""
    total_amount = store.get_total_quantity()
    print(f"\nTotal amount in store: {total_amount} items")

def make_order(store):
    """Process an order for a selected product and quantity."""
    print("\nAvailable products:")
    for i, product in enumerate(store.get_all_products()):
        print(f"{i + 1}. {product.show()}")

    try:
        product_index = int(input("Select the product number: ")) - 1
        quantity = int(input("Enter the quantity: "))

        selected_product = store.get_all_products()[product_index]
        total_price = selected_product.buy(quantity)

        if total_price > 0:
            print(f"Order successful! Total price: ${total_price:.2f}")
        else:
            print("Order failed. Please check the product availability.")

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid product number and quantity.")

def main():
    """Main function to handle user interactions."""
    actions = {
        "1": list_products,
        "2": show_total_quantity,
        "3": make_order
    }

    # Step 2: Setup initial stock of inventory, including LimitedProduct
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=50),
        Product("Google Pixel 7", price=500, quantity=250),
        LimitedProduct("Special Edition iPad", price=999, quantity=30, shipping_restriction="No international shipping")
    ]

    best_buy = Store(product_list)

    # Add promotions to products
    product_list[0].set_promotion(PercentageDisscount("20% Off", 20))
    product_list[1].set_promotion(SecondhalfPrice("Second Half Price"))
    product_list[2].set_promotion(BuyTwoGetOneFree("Buy 2 Get 1 Free"))

    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "4":
            print("Thank you for shopping with us. Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action(best_buy)
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
