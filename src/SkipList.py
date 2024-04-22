import random

class SkipList():
    def __init__(self, maxLevel=16):
        self.maxLevel = maxLevel
        self.head = Node(float('-inf'), 0, 1)
        self.tail = Node(float('inf'), 0, 1)
        self.head.next = self.tail

        temphead = self.head;
        temptail = self.tail;
        for x in range(maxLevel-1):
            temptail.down = Node(float('inf'), 0, temptail.level+1,None, None)
            temphead.down = Node(float('-inf'), 0, temphead.level+1, temptail, None)
            temphead = temphead.down
            temptail = temptail.down

    def search(self, key):
        curr = self.head
        prev = None
        while(curr is not None):
            print(curr,"->", end="")
            if curr.key < key:
                prev = curr
                curr = curr.next
            elif curr.key > key:
                curr = prev.down
                prev = curr
            else:
                return curr
        return None

    def insert(self, key, value = 0):
        curr = self.head
        level = self.roll()
        for x in range(self.maxLevel-level):
            curr = curr.down

        prev = None
        anchor = curr
        prevNewNode = None

        while(curr is not None):
            newNextNode = Node(key, value, curr.level)
            if(curr.key < key):
                prev = curr
                curr = curr.next
            elif(curr.key >= key):
                newNextNode.next = prev.next
                prev.next = newNextNode
                if prevNewNode is not None:
                    prevNewNode.down = newNextNode
                prevNewNode = newNextNode
                curr = prev.down


    def print(self):
        anchor = self.head
        curr = anchor
        for x in range(self.maxLevel):
            while curr is not None:
                print(curr, end = " ")
                curr = curr.next
            print("")
            anchor = anchor.down
            curr = anchor

    def roll(self):
        level = 1;
        while True:
            if level >= self.maxLevel:
                return level
            a = random.randint(0,1)
            if(a==1):
                level += 1
            else:
                return level





class Node:
    def __init__(self,  key, value, level, next = None, down = None):
        self.down = down
        self.next = next
        self.key = key
        self.value = value
        self.level = level

    def __str__(self):
        return "{0}".format(self.key)