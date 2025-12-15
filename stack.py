class Stack:
    def __init__(self): #lista vazia
        self.items = []

    def push(self, item): #adicionar item
        self.items.append(item)
        return item

    def pop(self): #remover o elemento
        if self.empty():
            return None
        return self.items.pop()

    def peek(self): # verificar o 1 elemento
        if self.empty():
            return None
        return self.items[-1]

    def size(self): #tamanho da lista
        return len(self.items)

    def empty(self): #verificar se a lista ta vazia ou não
        return len(self.items) == 0

q = Stack()
q.push("banana",)
q.push("morango")
y = q.peek()

print(q.push)