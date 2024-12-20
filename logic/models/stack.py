# Stack Implementation using Python Programming Language
# This Stack has 8 methodes :
# 1.lenght() => to return the number of elements in Stack
# 2.MAX() => to return the largest element with num data type and the largest ascii value for another data types
# 3.MIN() => to return the smallest element with num data type and the smallest ascii value for another data types
# 4.push() => to insert a new element in the end of the Stack
# 5.pop() => to delete and return the last element in the Stack
# 6.print() => to print all or some of the elements in Stack
# 7.peek() => to get the current element
# 8.operator[] => to access any value by it's element - this methode is useful to loop on the Stack elements

# Mohand Elsebaey



from logic.models.linkedlist import Node


class Stack:
    def __init__(self):
        self.linkedlist = Node()

    #function to get stack lenght
    def lenght(self):
        return self.linkedlist.lenght
    
    # function to get the maximum element in the stack
    def MAX(self):
        return self.linkedlist.MAX()
    
    # function to get the minimum element in the stack
    def MIN(self):
        return self.linkedlist.MIN()
    
    # function to insert a new value to the stack
    def push(self,value):
        self.linkedlist.insert(value=value)
    
    # function to delete and return the last value of the stack
    def pop(self):
        if self.linkedlist.lenght == 0:
            print("Stack Under Flow !",end='')
        else:
            return self.linkedlist.pop()
    
    # function to print all or some of the elements in Stack
    def print(self,start = 0,end = -1):
        if self.linkedlist.lenght == 0:
            print("[]",)
        else:
            self.linkedlist.print_items(start=start,end=end)

    # function to get the current element
    def peek(self):
        if self.linkedlist.lenght == 0:
            print("[Stack Under Flow !]",end='')
        else:
            return self.linkedlist[self.linkedlist.lenght - 1]
    
    # operator overloading to an element from a a specific position
    def __getitem__(self,index):
        return self.linkedlist[index]
        