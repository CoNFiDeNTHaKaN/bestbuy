import products
import store

def list_products(store_obj: store.Store):
    """Displays all active products in the store with an index number."""
    print("------")
    active_products = store_obj.get_all_products()
    for index, product in enumerate(active_products, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("------")

def show_total_amount(store_obj: store.Store):
    """Displays the total quantity of all items available in the store."""
    total_items = store_obj.get_total_quantity()
    print(f"Total of {total_items} items in store")

def make_order(store_obj: store.Store):
    """Prompts the user to select products and quantities, then processes the order."""
    active_products = store_obj.get_all_products()
    if not active_products:
        print("No active products available in the store.")
        return

    list_products(store_obj)
    print("When you want to finish order, enter empty text.")

    shopping_list = []
    while True:
        product_choice = input("Which product # do you want? ").strip()
        if product_choice == "":
            break

        amount_input = input("What amount do you want? ").strip()
        if amount_input == "":
            break

        try:
            product_index = int(product_choice) - 1
            amount = int(amount_input)

            if product_index < 0 or product_index >= len(active_products):
                print("Error: Invalid product number.")
                continue

            if amount <= 0:
                print("Error: Amount must be greater than zero.")
                continue

            selected_product = active_products[product_index]
            shopping_list.append((selected_product, amount))
            print("Product added to list!\n")

        except ValueError:
            print("Error: Please enter valid numeric values.")

    if shopping_list:
        try:
            total_cost = store_obj.order(shopping_list)
            print("********")
            print(f"Order made! Total payment: ${total_cost}")
        except Exception as error:
            print(f"Order failed: {error}")

def start(store_obj: store.Store):
    """Runs the interactive CLI menu loop for the given store."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total_amount(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error with your choice! Try again!")

def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)

    start(best_buy)

if __name__ == "__main__":
    main()