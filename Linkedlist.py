class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        next_node = Node(data)

        if self.head == None:
            self.head = next_node
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = next_node

    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

    def display(self):
        cur = self.head
        while cur.next != None:
            print (cur.data)
            cur = cur.next


    def search(self, index):
        if index >= self.length():
            print(" Index out of bounds")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    def delete(self, index):
        if index >= self.length():
            print(" Index out of bounds")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                prev_node.next = cur_node.next
                return
            cur_idx += 1

    def insertAt(self, data, index):
        new_Node = Node(data)
        cur_idx = 0
        cur_node = self.head
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                temp = new_Node
                prev_node.next = temp
                temp.next = cur_node
                return
            cur_idx += 1

    def add_lists(self, my_list, my_list2):
        prev = None
        temp=None
        carry = 0

        while (my_list is not None or my_list2 is not None):
            fdata=0 if my_list is None else my_list.data
            sdata=0 if my_list2 is None else my_list2.data

            Sum = carry + fdata + sdata

            carry = 1 if Sum >= 10 else 0

            Sum = Sum if Sum < 10 else Sum % 10

            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if my_list is not None:
                my_list = my_list.next
            if my_list2 is not None:
                my_list2 = my_list2.next
            if carry > 0:
                temp.next = Node(carry)


my_list = linkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list2 = linkedList()
my_list2.append(8)
my_list2.append(7)
my_list2.append(4)
my_list2.append(5)
my_list2.display()
#summ = linkedList()
#summ.add_lists(my_list.head, my_list2.head)
#summ.display()
print("Element at 2nd index is:%d" % my_list.search(2))
my_list.insertAt(13, 0)
my_list.display()
