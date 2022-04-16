# class Node:
#     def __init__(self, value) -> None:
#         self.value = value
#         self.next = None


# class Queue:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None
#         self.num_nodes = 0

#     def size(self):
#         return self.num_nodes

#     def enqueue(self, value):
#         new_node = Node(value)

#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#         self.num_nodes += 1

#     def dequeue(self):
#         if self.head is None:
#             return None

#         dequeue_node_value = self.head.value
#         self.head = self.head.next
#         self.num_nodes -= 1
#         return dequeue_node_value


# q = Queue()
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')

# print("Pass" if (q.size() == 3) else "Fail")
# q.enqueue(4)
# print("Pass" if (q.size() == 4) else "Fail")

# print("Pass" if (q.dequeue() == 'a') else "Fail")
# print("Pass" if (q.dequeue() == 'd') else "Fail")
# print("Pass" if (q.size() == 2) else "Fail")

class Queue:
    def __init__(self):
        self.items = []


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("We do not offer that flavor")

        if scoops not in (1, 2, 3):
            print("We only except 1 to 3 scoops max")
        print("Order Created!")

        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.items = order
        print(self.orders.items)

    # def show_all_orders(self):
    #     print("All pending orders:")
    #     for order in self.orders.items:


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zack", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
# shop.show_all_orders()
