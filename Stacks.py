class Stacks:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def Print(self):
        for i in self.items:
            print(i)

    def size(self):
        count = 0
        for i in self.items:
            count += 1
        print(count)

    def peep(self):
        return self.items[-1]

my_stack=Stacks()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.Print()
print("----")
my_stack.pop()
print("----")
my_stack.Print()
print("----")
my_stack.size()
print("----")
print(my_stack.peep())