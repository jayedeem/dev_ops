class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print('Head Node created:', self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value", node.next.value)

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print('Head Node created:', self.head.value)
            return

        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        print("Prepended new Head node with value: ", current_node.next.value)
        print("Node following Head is: ", current_node.value)


llist = LinkList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
llist.prepend("Second Node")
llist.prepend("Inserted New second Node")
llist.prepend("Third Node")
