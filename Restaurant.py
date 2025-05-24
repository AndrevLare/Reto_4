class MenuItem():
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name:str):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price:float):
        self.price = price

class MainCourse(MenuItem):
    def __init__(self, flour:str, protein:str, salad:str, name:str, price:float):
        super().__init__(name, price)
        self.flour = flour
        self.protein = protein
        self.salad = salad
        
    def get_flour(self):
        return self.flour

    def set_flour(self, flour:str):
        self.flour = flour

    def get_protein(self):
        return self.protein

    def set_protein(self, protein:str):
        self.protein = protein

    def get_salad(self):
        return self.salad

    def set_salad(self, salad:str):
        self.salad = salad

    def __str__(self):
        return f"{self.name} ({self.flour}, {self.protein}, {self.salad}) - ${self.price:.2f}"

class Dessert(MenuItem):
    def __init__(self, name:str, price:float, type:str):
        super().__init__(name, price)
        self.type = type

    def get_type(self):
        return self.type

    def set_type(self, type:str):
        self.type = type

    def __str__(self):
        return f"{self.name} ({self.type}) - ${self.price:.2f}"
    
class Drink(MenuItem):
    def __init__(self, name:str, price:float, size:str, hasSugar:bool):
        super().__init__(name, price)
        self.size = size
        self.hasSugar = hasSugar

    def get_size(self):
        return self.size

    def set_size(self, size:str):
        self.size = size

    def get_hasSugar(self):
        return self.hasSugar

    def set_hasSugar(self, hasSugar:bool):
        self.hasSugar = hasSugar

    def __str__(self):
        return f"{self.name} ({self.size}) - ${self.price:.2f}"

class Order():
    def __init__(self, items:list[MenuItem]):
        self.items = items
    
    def get_items(self):
        return self.items

    def set_items(self, items:list[MenuItem]):
        self.items = items

    def add_item(self, item:MenuItem):
        self.items.append(item)
    
    def __calcSubcounts(self, partial):
        dicounts = 0
        if len(self.items) >= 3:
            dicounts += 0.1 * partial
        return dicounts
            
    def getTotalBill(self):
        self.partial = sum(item.price for item in self.items)
        self.discounts = self.__calcSubcounts(self.partial)
        return self.partial - self.discounts

    def get_partial(self):
        return getattr(self, 'partial', 0)

    def get_discounts(self):
        return getattr(self, 'discounts', 0)
    
    def __str__(self):
        return "\n".join(str(item) for item in self.items)
    
class MedioPago:
  def __init__(self):
    pass

  def pagar(self, monto):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Tarjeta(MedioPago):
  def __init__(self, numero, cvv):
    super().__init__()
    self.__numero = numero
    self.__cvv = cvv
  def set_numero(self, numero):
        self.__numero = numero
  def set_cvv(self, cvv):
        self.__cvv = cvv
  def get_numero(self):
        return self.__numero
  def get_cvv(self):
        return self.__cvv

  def pagar(self, monto):
    print(f"Pagando {monto} con tarjeta ...1{self.get_numero()[-4:]}")

class Efectivo(MedioPago):
  def __init__(self, monto_entregado):
    super().__init__()
    self.monto_entregado = monto_entregado

  def pagar(self, monto):
    if self.monto_entregado >= monto:
      print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - monto}")
    else:
      print(f"Fondos insuficientes. Faltan {monto - self.monto_entregado} para completar el pago.")
    
if __name__ == "__main__":
    # Example usage
    grilled_Chicken = MainCourse("Wheat", "Chicken", "Caesar Salad", "Grilled Chicken", 12.99)
    cake = Dessert("Chocolate Cake", 4.99, "Cake")
    coke = Drink("Coke", 1.99, "Medium", True)
    taco = MainCourse("Corn", "Beef", "Greek Salad", "Taco", 8.99)
    lemonade = Drink("Lemonade", 2.49, "Large", False)
    coockies = Dessert("Cookies", 3.49, "Cookies")
    burrito = MainCourse("Wheat", "Chicken", "Greek Salad", "Burrito", 10.99)
    hotdog = MainCourse("Corn", "Beef", "Caesar Salad", "Hot Dog", 5.99)
    beer = Drink("Beer", 4.99, "Large", True)
    candy = Dessert("Candy", 1.99, "Candy")
    
    order = Order([grilled_Chicken, cake, coke, taco, lemonade, coockies, burrito, hotdog, beer, candy])
    print("Order Details:")
    print(order)
    print(f"Total Bill: ${order.getTotalBill():.2f}")
    print(f"aplicable discounts: ${order.discounts:.2f}")
    payment_method = int(input("Select payment method (1 for Card, 2 for Cash): "))
    if payment_method == 1:
        card_number = input("Enter card number: ")
        cvv = input("Enter CVV: ")
        payment = Tarjeta(card_number, cvv)
    elif payment_method == 2:
        cash_amount = float(input("Enter cash amount: "))
        payment = Efectivo(cash_amount)
    else:
        print("Invalid payment method selected.")
        exit(1)
        
    payment.pagar(order.getTotalBill())
    print("Payment successful!")