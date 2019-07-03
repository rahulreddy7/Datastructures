class node:
    def __init__(self, data=None):
        self.leftchild = None
        self.rightchild = None
        self.data = data
        self.parent=None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if (self.root == None):
            self.root = node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if (data < cur_node.data):
            if cur_node.leftchild == None:
                cur_node.leftchild = node(data)
                cur_node.leftchild.parent = cur_node
            else:
                self._insert(data, cur_node.leftchild)
        elif data > cur_node.data:
            if cur_node.rightchild == None:
                cur_node.rightchild = node(data)
                cur_node.rightchild.parent = cur_node
            else:
                self._insert(data, cur_node.rightchild)
        else:
            print("The value is already present")

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.leftchild, cur_height + 1)
        right_height = self._height(cur_node.rightchild, cur_height + 1)
        return max(left_height, right_height)

    def search(self, target):
        if self.root != None:
            self._search(self.root, target)
        else:
            return False

    def _search(self, cur_node, target):
        if target == cur_node.data:
            print("Found")
        elif target < cur_node.data and cur_node.leftchild != None:
            self._search(cur_node.leftchild, target)
        elif target > cur_node.data and cur_node.rightchild != None:
            self._search(cur_node.rightchild, target)
        return False

    def printtree(self):
        if self.root != None:
            self._printtree(self.root)

    def _printtree(self, cur_node):
        if cur_node != None:
            self._printtree(cur_node.leftchild)
            print(str(cur_node.data))
            self._printtree(cur_node.rightchild)

    def find(self, value):
        if self.root != None:
            return self._find(self.root, value)
        else:
            return None

    def _find(self, cur_node, value):
        if value == cur_node.data:
            return cur_node
        elif value < cur_node.data and cur_node.leftchild != None:
            return self._find(cur_node.leftchild, value)
        elif value > cur_node.data and cur_node.rightchild != None:
            return self._find(cur_node.rightchild, value)

    def delete(self, value):
        return self.delete_node(self.find(value))

    def min_node(self, n):
        current = n
        while current.leftchild != None:
            current = current.leftchild
        return current

    def num_children(self, cur_node):
        count = 0
        if cur_node.leftchild != None:
            count += 1
        if cur_node.rightchild != None:
            count += 1
        return count

    def delete_node(self, node):

        if node == None or self.find(node.data) == None:
            print("Node not found in tree")
            return None

        node_parent = node.parent

        num_children = self.num_children(node)

        if num_children == 0:
            if node_parent != None:
                if node_parent.leftchild == node:
                    node_parent.leftchild = None
                else:
                    node_parent.rightchild = None
            else:
                self.root = None

        if num_children == 1:
            if node.leftchild != None:
                child = node.leftchild
            else:
                child = node.rightchild

            if node_parent != None:
                if node_parent.leftchild == node:
                    node_parent.leftchild = child
                else:
                    node_parent.rightchild = child
            else:
                self.root = child
            child.parent = node_parent

        if num_children == 2:
            successor = self.min_node(node.rightchild)
            node.data = successor.data
            self.delete_node(successor)


my_tree = BST()
my_tree.insert(10)
my_tree.insert(5)
my_tree.insert(20)
my_tree.insert(4)
my_tree.insert(6)
my_tree.search(11)
print("The tree height is:%d" % (my_tree.height()))
my_tree.printtree()
my_tree.delete(6)
my_tree.printtree()
