class Queue:
    def __init__(self) -> None:
        self.items: list = []


class IceCreamShop:
    def __init__(self, flavors) -> None:
        self.flavors: str = flavors
        self.orders: list[dict] = Queue()

      # take order
    def take_order(self, customer: str, flavor: str, scoops: int) -> None:
        order: dict = {'customer': customer, 'flavor': flavor, 'scoops': scoops}
        if not flavor in self.flavors:
            print(f"{order['customer']}, don't make {order['flavor']}!")
            return None

        if scoops > 3 or scoops == 0:
            print(f"{order['customer']}, Please no more than 3 scoops please!\nChoose between 1-3 scoops\n")
            return None      
        self.orders.items.append(order)
        print(
            f"Order Created For = {self.parse_order(order)}")

      # show all orders
    def show_all_orders(self) -> None:
        if not len(self.orders.items):
            print("No orders pending!")
            return None

        print("All Pending Ice Cream Orders:")
        for order in self.orders.items:
            print(
                f"Customer: {self.parse_order(order)}")

        # next order
    def next_order(self) -> None:
        if not len(self.orders.items):
            print("No orders pending!")
            return None
        else:
            order: list = self.orders.items.pop(0)
            print(
                f"\nNext Order Up!\n{self.parse_order(order)}")

    def parse_order(self, order: list) -> str:
        return f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}"


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
