class deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		return self.items.append(item)

	def removeFront(self):
		return self.items.pop(item)

	def addRear(self, item):
		return self.items.insert(0, item)

	def removeRear(self):
		return self.items.pop(0)

def palchecker(aString):
	chardeque = Deque()

	for ch in aString:
		chardeque.addRear(ch)
