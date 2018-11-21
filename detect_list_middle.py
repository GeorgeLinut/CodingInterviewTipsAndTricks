class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, start):
        self.start = start

    def detect_middle(self):
        if self.start.next is None:
            return self.start

        i = self.start
        j = self.start

        while j.next is not None:
            j = j.next.next
            if j is not None:
                i = i.next
            else:
                break
        if j is not None:
            return i.value
        return i.value, i.next.value


def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    
    l = LinkedList(n1)

    assert (l.detect_middle() == 3)

main()






