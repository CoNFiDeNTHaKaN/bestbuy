class Product:
  def __init__(self, name: str, price: float, quantity: int):
    if not name or not isinstance(name, str):
      raise ValueError("Product name cannot be empty.")
    if price < 0:
      raise ValueError("Price cannot be negative.")
    if quantity < 0:
      raise ValueError("Quantity cannot be negative.")

    self.name = name
    self.price = float(price)
    self.quantity = int(quantity)
    self.active = True
  
  def get_quantity(self) -> int:
    return self.quantity
  
  def set_quantity(self, quantity: int):
    if quantity < 0:
      raise ValueError("Quantity cannot be negative.")
    self.quantity = quantity
    if self.quantity == 0:
       self.deactivate()

  def is_active(self) -> bool:
    return self.active

  def activate(self):
    self.active = True

  def deactivate(self):
    self.active = False
  
  def show(self):
    print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

  def buy(self, quantity: int) -> float:
      if not self.active:
        raise Exception(f"Cannot purchase '{self.name}': product is inactive.")
      if quantity <= 0:
         raise ValueError("Purchase quantity must be greater than zero.")
      if quantity > self.quantity:
         raise ValueError(
             f"Insufficient stock for '{self.name}'. Available: {self.quantity}, Requested: {quantity}"
         )

      total_price = float(self.price * quantity)
      self.set_quantity(self.quantity - quantity)
      return total_price  