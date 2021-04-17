class Queqe:

    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def pushFront(self, item):
        self.items.insert(0, item)
    def pushBack(self, item):
        self.items.append(item)
    def popFront(self):
        return self.items.pop(0)
    def popBack(self):
        return self.items.pop()
    def Front(self):
        return self.items.pop(0)
    def Back(self):
        return self.items.pop()

Q = Queqe()
File = open("Input.txt", 'r')
for Line in File:
    Letter = Line[0:1]
    Value = Line[2:]
    if Letter == 'A':
        Q.pushFront(Value)
    elif Letter == 'B':
        Q.pushBack(Value)
        Q.pushBack(Value)
    elif Letter == 'C':
        Q.popFront()
    elif Letter == 'D':
        Q.popBack()
    elif Letter == 'E':
        print(Q.Front())
    elif Letter == 'F':
        print(Q.Back())
