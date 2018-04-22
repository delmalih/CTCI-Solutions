class Node (object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printLinkedList(head):
    res = ""
    buffer = head
    while buffer:
        res += str(buffer.data) + " -> "
        buffer = buffer.next
    print(res)

def addHead(node, head):
    node.next = head
    return node

def addTail(node, head):
    buffer = head
    while buffer.next:
        buffer = buffer.next
    buffer.next = node
    return head