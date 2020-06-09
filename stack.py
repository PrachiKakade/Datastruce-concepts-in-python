from sys import maxsize
#class stack:
def createstack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + "pushed to stack")

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
    return stack[len(stack) - 1]

stack = createstack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + "poped from stack")




# Python program for linked list implementation of stack 
'''  
# Class to represent a node 
class StackNode: 
  
    # Constructor to initialize a node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class Stack: 
      
    # Constructor to initialize the root of linked list 
    def __init__(self): 
        self.root = None
  
    def isEmpty(self): 
        return True if self.root is None else  False 
  
    def push(self, data): 
        newNode = StackNode(data) 
        newNode.next = self.root  
        self.root = newNode 
        print "% d pushed to stack" %(data) 
      
    def pop(self): 
        if (self.isEmpty()): 
            return float("-inf") 
        temp = self.root  
        self.root = self.root.next 
        popped = temp.data 
        return popped 
      
    def peek(self): 
        if self.isEmpty(): 
            return float("-inf") 
        return self.root.data 
  
# Driver program to test above class  
stack = Stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 
  
print "% d popped from stack" %(stack.pop()) 
print "Top element is % d " %(stack.peek()) 
  '''





    
'''
    def __init__(self):
        self.stack = []
    def add(self,dataval): #append menthod is use to add the elemnet
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self): #diplay the stack 
            return self.stack[-1]
    def remove(self): #pop method to reove the elememt
        if len(self.stack) <= 0:
            return ("No element in the stack")
        else:
            return self.stack.pop()


astack = stack()
astack.add("mon")
astack.add("Tus")
astack.add("wed")
astack.add("Thu")
print(astack.remove())
print(astack.remove())
'''
        
