from node import Node

class unorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)

		self.head = temp

	def size(self):

		current = self.head
		count = 0

		while current != None:
			count += 1

			current = self.getNext()

		return count

	def search(self, item):
		current = self.head
		found = false

		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.next()

		return found

	def remove(self, item):

		previous = None
		current = self.head
		found = None



		while not found and current != None:
			if current.getData() == item:
				found = True

			else:
				previous = current
				current = current.getNext();


		if found:
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())

	def pop(self, index = 0):
		previous = None
		current = self.head
		found = None

		counter = 0

		while not found and current != None:
			if counter == index:
				found = True

			else:
				previous = current
				current = current.getNext()
				counter += 1


		if found:
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())

		current = self.head
		

		


	def append(self, item):
		current = self.head
		temp = Node(item)

		if current:
			while current.getNext() != None:
				current = current.getNext()
			
			current.setNext(temp) 
		else:
			self.head = temp


		

	def index(self, item):
		current = self.head
		counter = 0
		if current:
			while current.getNext() != None and current.getData != item:
				current = current.getNext()
				counter += 1
			
			current.setNext(temp) 
	
		return counter

	def insert(self, item, index = 0):
		current = self.head
		temp = Node(item)
		counter = 0

		if current:
			while current != None:
				if current.getData() == item:
					break

				current = current.getNext()

				counter += 1
		
		else:
			counter = None

		return counter
	


temp = Node(93)
print temp.getData()

mylist = unorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

mylist2 = unorderedList()
mylist2.add(31)
mylist2.add(77)
mylist2.append(1)
mylist2.pop(1)

print mylist2.head.getData()
print mylist2.head.getNext().getData()


