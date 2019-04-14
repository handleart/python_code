class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def __iter__(self):
        return iter(self.items)

        


        return val 

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def binary(num):
    x = Stack()

    while True: 
        if num < 1:
            x.push(1)
            break
        else:
            if num % 2 == 1:
                x.push(1)
            else:
                x.push(0)
            
            num = num // 2

    y = []
    while not x.isEmpty():
        y.append(str(x.pop()))
   
    return "".join(str(i) for i in y)


def binary(num):
    digits = "0123456789ABCDEF"
    x = Stack()

    while True: 
        if num < 1:
            x.push(1)
            break
        else:
            if num % 2 == 1:
                x.push(1)
            else:
                x.push(0)
            
            num = num // 2

    y = []
    while not x.isEmpty():
        y += str(digits[x.pop()])
 

    return y

def baseConverter(num, base):
    digits = "0123456789ABCDEF"
    x = Stack()

    while num > 0:    
        x.push(num % base) 
            
        num = num // base

    y = ''
    while not x.isEmpty():
        y += str(digits[x.pop()])
   

    return y

#f = binary(213)
f = baseConverter(25, 16)

print f


#print(parChecker('{{([][])}()}'))
#print(parChecker('[{()]'))