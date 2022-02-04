""" This file implements both min and max heaps """
from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self, size):
        self.__size = size
        self.__heap = [0] * size
        self.__curr_size = 0

    def get_current_size(self) -> int:
        return self.__curr_size

    def get_size(self) -> int:
        return self.__size

    def print_heap(self) -> None:
        string = ""
        for num in self.__heap:
            string = string + str(num) + ", "
        print(string[: -2])  # Removing the trailing comma and space

    def get_left_child_index(self, index) -> int:
        return (2 * index) + 1

    def has_left_child(self, index) -> bool:
        return True if self.get_left_child_index(index) <= self.__curr_size else False

    def get_right_child_index(self, index) -> int:
        return (2 * index) + 2

    def has_right_child(self, index) -> bool:
        return True if self.get_right_child_index(index) <= self.__curr_size else False

    def get_parent_index(self, index) -> int:
        return (index - 1) // 2

    def has_parent(self, index) -> bool:
        return True if (self.get_parent_index(index) >= 0) else False

    def is_full(self) -> bool:
        return True if (self.__curr_size == (self.__size - 1)) else False

    def is_empty(self) -> bool:
        return True if (self.__curr_size == 0) else False

    def swap_values(self, index_one, index_two) -> None:
        temp = self.__heap[index_one]
        self.__heap[index_one] = self.__heap[index_two]
        self.__heap[index_two] = temp

    def add_element(self, value) -> None:
        if not self.is_full():
            self.__heap[self.__curr_size] = value
            self.heapify_up()
            self.__curr_size += 1
        else:
            print("Can't add value. Heap full !!")

    @abstractmethod
    def heapify_up(self) -> None:
        current_index = self.__curr_size
        current_value = self.__heap[current_index]

        while self.has_parent(current_index) and current_value < self.__heap[self.get_parent_index(current_index)]:
            self.swap_values(current_index, self.get_parent_index(current_index))
            current_index = self.get_parent_index(current_index)
            current_value = self.__heap[current_index]

    @abstractmethod
    def heapify_up_recursive(self, index) -> None:
        current_index = index
        current_value = self.__heap[current_index]
        if not self.has_parent(current_index) or current_value >= self.__heap[self.get_parent_index(current_index)]:
            return

        self.swap_values(current_index, self.get_parent_index(current_index))
        current_index = self.get_parent_index(current_index)
        self.heapify_up_recursive(current_index)

    def remove_element(self) -> int:
        if not self.is_empty():
            min_value = self.__heap[0]
            self.__heap[0] = self.__heap[self.__curr_size - 1]
            self.__curr_size -= 1
            self.heapify_down()

            print(self.__curr_size)
            return min_value
        else:
            print("Can't remove value. Heap empty !!")

    @abstractmethod
    def heapify_down(self) -> None:
        current_index = 0
        smallest_index = current_index

        while current_index <= self.__curr_size and self.__heap[current_index] >= self.__heap[smallest_index]:
            if self.has_left_child(current_index):
                left_child_index = self.get_left_child_index(current_index)
                if self.__heap[smallest_index] > self.__heap[left_child_index]:
                    smallest_index = left_child_index
                if self.has_right_child(current_index):
                    right_child_index = self.get_right_child_index(current_index)
                    if self.__heap[smallest_index] > self.__heap[right_child_index]:
                        smallest_index = right_child_index

            if current_index != smallest_index:
                self.swap_values(current_index, smallest_index)
                current_index = smallest_index
            else:
                break

    @abstractmethod
    def heapify_down_recursive(self, index) -> None:
        current_index = index
        smallest_index = current_index

        if current_index >= self.__curr_size:
            return

        if self.has_left_child(current_index):
            left_child_index = self.get_left_child_index(current_index)
            if self.__heap[smallest_index] > self.__heap[left_child_index]:
                smallest_index = left_child_index
            if self.has_right_child(current_index):
                right_child_index = self.get_right_child_index(current_index)
                if self.__heap[smallest_index] > self.__heap[right_child_index]:
                    smallest_index = right_child_index

        if current_index != smallest_index:
            self.swap_values(current_index, smallest_index)
            self.heapify_down_recursive(smallest_index)

        return


class MinHeap(Heap):
    def __init__(self, size):
        super().__init__(size)

    def heapify_up(self) -> None:
        super().heapify_up()

    def heapify_up_recursive(self) -> None:
        super().heapify_up_recursive()

    def heapify_down(self) -> None:
        super().heapify_up()

    def heapify_down_recursive(self) -> None:
        super().heapify_up_recursive()



