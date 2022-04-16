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


llist = LinkList()
llist.append("1st node")
llist.append("2nd node")
llist.append("3rd node")
