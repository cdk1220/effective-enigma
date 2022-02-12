""" This file implements binary trees and binary search trees """


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node: TreeNode) -> None:
        self.head = node

    def in_order_traversal(self, start_node: TreeNode) -> None:
        if start_node is None:
            return

        self.in_order_traversal(start_node.left)
        print(start_node.value)
        self.in_order_traversal(start_node.right)

    def pre_order_traversal(self, start_node: TreeNode) -> None:
        if start_node is None:
            return

        print(start_node.value)
        self.in_order_traversal(start_node.left)
        self.in_order_traversal(start_node.right)

    def post_order_traversal(self, start_node: TreeNode) -> None:
        if start_node is None:
            return

        self.in_order_traversal(start_node.left)
        self.in_order_traversal(start_node.right)
        print(start_node.value)

    def find_min(self, start_node: TreeNode) -> int:
        if start_node.left is None and start_node.right is None:
            return start_node.value

        current_value = start_node.value
        left_min = self.find_min(start_node.left)
        right_min = self.find_min(start_node.right)

        return min(current_value, left_min, right_min)

    def find_max(self, start_node: TreeNode) -> int:
        if start_node.left is None and start_node.right is None:
            return start_node.value

        current_value = start_node.value
        left_max = self.find_max(start_node.left)
        right_max = self.find_max(start_node.right)

        return min(current_value, left_max, right_max)


class BinarySearchTree(Tree):
    def __init__(self) -> None:
        super().__init__(None)

    def add_element(self, new_node: TreeNode, start_node: TreeNode) -> None:
        if self.head is None:
            self.head = new_node
            return

        if new_node.value >= start_node.value:
            if start_node.right is None:
                start_node.right = new_node
            else:
                self.add_element(new_node, start_node.right)
        else:
            if start_node.left is None:
                start_node.left = new_node
            else:
                self.add_element(new_node, start_node.left)

        return

    def search_element(self, value: int, start_node: TreeNode) -> bool:
        if start_node is None:
            return False

        if start_node.value == value:
            return True

        if value >= start_node.value:
            found = self.search_element(value, start_node.right)
        else:
            found = self.search_element(value, start_node.left)

        return found

    def remove_element(self, value: int, start_node: TreeNode) -> TreeNode:
        if start_node is None:
            return None

        if value > start_node.value:
            start_node.right = self.remove_element(value, start_node.right)
        elif value < start_node.value:
            start_node.left = self.remove_element(value, start_node.left)
        else:
            # Case 1: When the node has no children
            if start_node.left is None and start_node.right is None:
                start_node = None
            # Case 2: When the node has a single child either right or left
            elif start_node.left is None:
                start_node = start_node.right
            elif start_node.right is None:
                start_node = start_node.left
            # Case 3: When the node has children from both sides
            else:
                # Find the min of its right subtree (The min does not have any left child because it is the min)
                min_value = self.find_min(start_node.right)
                # This node to be deleted should get this min value
                start_node.value = min_value
                # Delete the min node which exists on the right subtree
                start_node.right = self.remove_element(min_value, start_node.right)

        return start_node

