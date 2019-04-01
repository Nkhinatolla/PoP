class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
class Node:

file = open("input_3.txt", "r") 
text = file.read().split('\n')

node1 = linkedListNode("3") # "3"
node2 = linkedListNode("7") # "7"
node3 = linkedListNode("10") # "10"

node1.nextNode = node2 
node2.nextNode = node3 

