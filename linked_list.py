# ASSESSMENT 3.2 - LINKED LIST
# Name: JAMES PANOGALING

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, letter):
        new_node = Node(letter)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("NULL")

    def delete(self):
        if self.head:
            removed = self.head.data
            self.head = self.head.next
            return removed


def main():
    name = "JAMES PANOGALING".replace(" ", "")
    linked_list = LinkedList()

    print("=== LINKED LIST INSERTION ===")

    for letter in name:
        linked_list.insert(letter)

    linked_list.display()

    print("\n=== LINKED LIST DELETION ===")

    while linked_list.head:
        removed = linked_list.delete()
        print("Removed:", removed)
        print("Remaining:", end=" ")
        linked_list.display()

    print("\nFinal Linked List: EMPTY")


main()