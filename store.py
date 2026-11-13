import products


class Store:
    def __init__(self, product_list=None):
        if product_list is None:
            self.products = []
        else:
            self.products = list(product_list)

    def add_product(self, product: products.Product):
        self.products.append(product)

    def remove_product(self, product: products.Product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product '{product.name}' is not sold in this store.")
            total_price += product.buy(quantity)
        return total_price