# https://www.youtube.com/watch?v=74NW-84BqbA&list=PLH4izthU8rXTbSRVJZvAJZojarwVfjQhA
# from 02:06:02 onwards

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None   # top node

    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)

        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

        else:
            return

    def insert(self, data):
        if self.root is None:  # checking if the root is none
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)


    def _search_recursive(self, blog_post_id, node):

        if blog_post_id == node.data["id"]:
            return node.data  # if we're searching for root node

        if blog_post_id < node.data["id"] and node.left is not None:
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            return self._search_recursive(blog_post_id, node.left)

        if blog_post_id > node.data["id"] and node.right is not None:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            return self._search_recursive(blog_post_id, node.right)
        return False

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False  # binary search tree is empty

        return self._search_recursive(blog_post_id, self.root)


