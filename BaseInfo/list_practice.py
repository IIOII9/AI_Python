class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def search(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


ll = LinkedList()
ll.insert(3)
ll.insert(5)
ll.insert(2)
ll.display()
print(ll.search(2))


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print("binary search:", binary_search([1, 3, 5, 7, 9], 5))
