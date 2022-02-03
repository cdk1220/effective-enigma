''' This file implements both min and max heaps '''

class MinHeap:
    def __init__(self, size):
        self.__size = size
        self.__heap = [0] * size
        self.__curr_size = 0

    def get_current_size(self):
        return self.__curr_size


    def get_size(self):
        return self.__size


    def print_heap(self):
        string = ""
        for num in self.__heap:
            string = string + str(num) + ", "
        print(string[: -2]) # Removing the trailing comma and space


    def get_left_child_index(self, index):
        return ((2 * index) + 1)


    def has_left_child(self, index):
        return True if self.get_left_child_index(index) <= self.__curr_size else False


    def get_right_child_index(self, index):
        return ((2 * index) + 2)


    def has_right_child(self, index):
        return True if self.get_right_child_index(index) <= self.__curr_size else False


    def get_parent_index(self, index):
        return ((index - 1) // 2)


    def has_parent(self, index):
        return True if (self.get_parent_index(index) >= 0) else False


    def is_full(self):
        return True if (self.__curr_size == (self.__size - 1)) else False

    def is_empty(self):
        return True if (self.__curr_size == 0) else False


    def swap_values(self, index_one, index_two):
        temp = self.__heap[index_one]
        self.__heap[index_one] = self.__heap[index_two]
        self.__heap[index_two] = temp


    def add_element(self, value):
        if not self.is_full():
            self.__heap[self.__curr_size] = value
            self.heapify_up()
            self.__curr_size += 1
        else:
            print("Can't add value. Heap full !!")


    def heapify_up(self):
        current_index = self.__curr_size
        current_value = self.__heap[current_index]

        while self.has_parent(current_index) and current_value < self.__heap[self.get_parent_index(current_index)]:
            self.swap_values(current_index, self.get_parent_index(current_index))
            current_index = self.get_parent_index(current_index)
            current_value = self.__heap[current_index]


    def heapify_up_recursive(self, index):
        current_index = index
        current_value = self.__heap[current_index]
        if not self.has_parent(current_index) or current_value >= self.__heap[self.get_parent_index(current_index)]:
            return

        self.swap_values(current_index, self.get_parent_index(current_index))
        current_index = self.get_parent_index(current_index)
        self.heapify_up_recursive(current_index)

    
    def remove_element(self):
        if not self.is_empty():
            min_value = self.__heap[0]
            self.__heap[0] = self.__heap[self.__curr_size - 1]
            self.__curr_size -= 1
            self.heapify_down()
            
            print(self.__curr_size)
            return min_value
        else:
            print("Can't remove value. Heap empty !!")


    def heapify_down(self):
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

    
    def heapify_down_recursive(self, index):
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