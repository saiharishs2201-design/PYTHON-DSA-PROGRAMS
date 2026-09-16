class fooditem:
    def __init__(self,item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
class restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
    def add_food(self,food):
        self.menu.append(food)
    def show_menu(self):
        print(f"\n====={self.name} Menu=====")
        for food in self.menu:
            print(f"{food.item_id}. {food.name} - ${food.price}")
class cart :
    def __init__(self):
        self.items = []
    def add_to_cart(self,food,quantity):
        self.items.append((food,quantity))
        print(f"{food.name} added to cart.")
    def calculate_total(self):
        total = 0
        for food, quantity in self.items:
            total += food.price * quantity
        return total
class order:
    def __init__(self, cart):
        self.cart = cart
        self.status = "placed"
    def place_order(self):
        total = self.cart.calculate_total()
        print("\n========== order details ==========")
        print(f"order status: {self.status}")
        print(f"total amount: ${total}")
        self.status = "confirmed"
        print("order confirmed!")
        self.status = "preparing"
        print("order is being prepared!")
        self.status = "out for delivery"
        print("order is out for delivery!")
        self.status = "delivered"
        print("order delivered successfully!")
restaurant = restaurant("ABC RESTURANT")
pizza = fooditem(1, "Pizza", 2)
burger = fooditem(2, "Burger", 1.5)
juice = fooditem(3, "Juice", 1)
restaurant.add_food(pizza)
restaurant.add_food(burger)
restaurant.add_food(juice)
cart = cart()
cart.add_to_cart(pizza, 2)
cart.add_to_cart(burger, 1)
cart.add_to_cart(juice, 3)
order = order(cart)
order.place_order()