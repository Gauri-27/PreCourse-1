
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        
    def pop(self):
        if self.top == None:
            return None
        poppedNode = self.top
        self.top = self.top.next
        return poppedNode.data
    

    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result)
        
a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
        print(a_stack)
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
