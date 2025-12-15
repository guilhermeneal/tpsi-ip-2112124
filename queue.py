class bootle:
    def __init__(self):
        self.brand = None
        self.price = 0
        self.capacity = None
        self.origin = None

b1 = bootle()
b1.brand = "Miau"
b1.capacity = 3
b1.origin = "Africa"
b1.price = 5


class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):  # adicionar à lista
        self.items.append(item)

    def dequeue(self):  # remover 1 elemento
        if not self.empty():
            return self.items.pop(0)
        return None

    def size(self):  # tamanho da lista
        return len(self.items)

    def peek(self):  # primeiro elemento
        if not self.empty():
            return self.items[0]
        return None

    def empty(self):  # lista vazia
        return self.size()  == 0

    def clear(self):  # remover todos os elementos
        self.items = []


q = queue()
q.enqueue(5)
q.enqueue(3)
q.enqueue(4)
x = q.dequeue()
y = q.dequeue()
j = q.size()

