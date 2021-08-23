# https://www.youtube.com/watch?v=74NW-84BqbA&list=PLH4izthU8rXTbSRVJZvAJZojarwVfjQhA
# from 42:00

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        list = []
        if self.head is None:
            return list

        node = self.head
        while node:
            list.append(node.data)
            node = node.next_node
        return list

    def print_linked_list(self):
        linked_list_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            linked_list_string += f" {str(node.data)} =>"
            node = node.next_node
        linked_list_string += " None"
        print(linked_list_string)

# This is just to show how it works
# linked_list = LinkedList()
# node4 = Node("data4", None)
# node3 = Node("data3", node4)
# node2 = Node("data2", node3)
# node1 = Node("data1", node2)
# O/P=  data1 -> data2 -> data3 -> data4 -> None

    def insert_begining(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        new_node = Node(data, self.head)
        self.head = new_node

# linked_list = LinkedList()
# linked_list.insert_begining("data")
# linked_list.insert_begining("not data")
# linked_list.print_linked_list()
# O/P=  not data => data => None

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_begining(data)

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None
