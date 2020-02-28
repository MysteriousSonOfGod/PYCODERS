class Stack:
    def __init__(self):
        self.Stack = []


    def add(self, dataval):
        if dataval not in self.Stack:
            self.Stack.append(dataval)
            return True
        else:
            return False

    def peak(self):
        return self.Stack[::-1]


insert = Stack()
insert.add("Mon")
insert.add("Tue")
insert.add("Wed")
print(insert.peak())