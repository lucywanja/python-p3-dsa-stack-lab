class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = [] #Empty list that will hold the elements of the stack
        self.limit = limit

        for item in items:
            if(not self.full()):
                self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if(not self.full()):
            self.items.append(item) #Appends the item to the end of the list ,pushing it onto the stack
        else:
            return None    

    def pop(self):
        if self.isEmpty(): #Checks is the stack is empty
            return None # returns none if empty
        return self.items.pop() #if not it removes the last item from the list and returns it

    def peek(self):
        return self.items[len(self.items)] #returns the ltem at the top of the stack without removing it
    
    def size(self):
        return len(self.items) #returns the number of items in the stack

    def full(self):
        if(len(self.items) >= self.limit):
            return True
        return False

    def search(self, target): #method searches for an item in the stack and returns the position from the top if found; otherwise, it returns -1.
        for i in reversed(range(len(self.items))): #creates a reversed iterator over the indices of the list items. This ensures the search starts from the top of the stack.
# The for loop iterates over the indices in reversed order.
            if self.items[i] == target: #  checks if the current item matches the target.
                return len(self.items) -1 - i # calculates the distance from the top of the stack to the found item and returns it.
        return -1 #if the loop completes without finding the target, return -1 indicates that the item is not in the stack.

