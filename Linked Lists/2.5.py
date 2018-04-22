from lib import *

def createLinkedList(number):
    number = str(number)
    head = Node(number[-1])
    buffer = head
    for i in range(0, len(number)-1):
        buffer.next = Node(int(number[len(number)-2-i]))
        buffer = buffer.next
    return head

def linkedListToNumber(head):
    res = 0
    buffer = head
    counter = 0
    while buffer:
        res += int(buffer.data) * 10**counter
        counter += 1
        buffer = buffer.next
    return res

def sumLists(list1, list2):
    number1 = linkedListToNumber(list1)
    number2 = linkedListToNumber(list2)
    sum = number1 + number2
    list = createLinkedList(sum)
    return list

list1 = createLinkedList(617)
list2 = createLinkedList(295)

sumList = sumLists(list1, list2)
printLinkedList(sumList)