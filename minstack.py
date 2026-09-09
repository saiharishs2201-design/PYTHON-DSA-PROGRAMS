class minstack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push (self,value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    def pop (self):
        if not self.stack:
            return"stack is empty"
        value = self.stack.pop()
        if value  == self.min_stack[-1]:
            self.min_stack[-1]
        return value
    def get_min(self):
        if not self.min_stack:
            return "stack is empty"
        return self.min_stack[-1]
    s = minstack()
    s.push(10)
    s.push(5)
    s.push(20)
    s.push(2)
    print("minimum",s.get_min())
    s.pop()
    print('minimum after pop:',s.get_min())