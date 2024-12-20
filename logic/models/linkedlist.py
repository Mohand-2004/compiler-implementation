# LinkedList Implementation using Python Programming Language
# This linkedlist has 11 methodes :
# 1.lenght() => to return the number of elements in linkedlist
# 2.MAX() => to return the largest element with num data type and the largest ascii value for another data types
# 3.MIN() => to return the smallest element with num data type and the smallest ascii value for another data types
# 4.insert() => to insert a new element in the linkedlist in any place
# 5.print() => to print all or some of the elements in linkedlist
# 6.pop() => to delete an element from any place and return the deleted element value
# 7.remove() => to delete an element by it's value
# 8.update() => to update any element in the linkedlist
# 9.swap() => to swap any two elements in the linkedlist
# 10.copy() => to copy the elements of the linkedlist in a new linkedlist 
# 11.operator[] => to access any value by it's element - this methode is useful to loop on the linkedlist elements
# 12.operator= => to assign a list to the linkedlist easly
# 13.operator+ to Concatenate a new linkedlist to this linkedlist
# 14.indexof() => to get the index of a speceific value

# Mohand Elsebaey

class Node:
    # the value which will be stored in the node
    item = None
    # object to accsses next node
    next = None
    # this attribute to accsess linkedlist lenght
    lenght = 0
    def __init__(self,item = None):
        self.item = item
    
    # method to get the largest element in linkedlist
    def MAX(self):
        current = self
        large = current.item
        for _ in range(self.lenght):
            if current.item > large:
                large = current.item
            current = current.next
        return large

    # method to get the smallest element in linkedlist
    def MIN(self):
        current = self
        small = current.item
        for _ in range(self.lenght):
            if current.item < small:
                small = current.item
            current = current.next
        return small
    
    # method to insert a new value to linkedlist
    def insert(self,value,index = -1):
        # set index by default to linkedlist lenght
        if index == -1:
            index = self.lenght
        # check if index is in linkedlist range
        if index > self.lenght or index < 0:
            # handle out of range error
            print('Error , Out of Range Index !')
        else:
            # check if linkedlist is Empty
            if self.item == None:
                self.item = value
            else:
                # insert begganing case
                if index == 0:
                   node = Node(self.item)
                   third = self.next
                   self.item = value
                   self.next = node
                   node.next = third

                # insert at the end (the default case)
                elif index == self.lenght:
                    node = Node(value)
                    last = self
                    for _ in range(index-1):
                        last = last.next
                    last.next = node

                # insert at middle (the general case)
                else:
                    node = Node(value)
                    previous = self
                    next = self.next
                    for _ in range(index-1):
                        previous = previous.next
                        next = next.next
                    previous.next = node
                    node.next = next

            # increment linkedlist lenght
            self.lenght += 1

    # print all the elements of the linkedlist by defualt
    # print a part of the elements between start and end    
    def print_items(self,start = 0,end = -1):
        # set end to defualt value
        if(end == -1):
            end = self.lenght-1
        # check if linked list is Empty
        if self.item == None:
            print('LinkedList Is Empty !')
        else:
            # check if start and end are in range
            if start >= self.lenght or end >= self.lenght or start < 0 or end < 0:
                # handle out of range index
                print('Error , Out of Range Index !')
                # assert that end is bigger than start
            elif start > end:
                print("Error , End index must be bigger than Start index !")
            else:
                startNode = self
                # move start node to the start position
                for _ in range(start):
                    startNode = startNode.next
                # print the elements from start to end
                print('[',end='')
                for _ in range(start,end+1):
                    print(f'{startNode.item}, ',end='')
                    startNode = startNode.next
                print(']')

    # delete a specific element by index and return the deleted element
    def pop(self,index = -1):
        # set index by default to linkedlist lenght
        if index == -1:
            index = self.lenght-1
        # check if index is in range
        if index >= self.lenght or index < 0:
            # handle out of range error
            print('Error , Out of Range Index !')
        else:
            # decrement linkedlist lenght
            self.lenght -= 1

            # delete the only node in the linked list
            if self.lenght == 0:
                deletedItem = self.item
                self.item = None
                return deletedItem
            else:
                # delete element from begging
                if index == 0:
                    deletedItem = self.item 
                    third = self.next.next
                    self.item = self.next.item
                    self.next = third
                    return deletedItem
                
                # delete element from middle (general case)
                else:
                    previous = self
                    target = self.next
                    next = self.next.next
                    for _ in range(index-1):
                        previous = previous.next
                        target = target.next
                        next = next.next
                    previous.next = next
                    return target.item
            
    # delete element by value
    def remove(self,value):
        # remove the only node in the linkedlist
        if self.lenght == 1:
            if value == self.item:
                self.item = None
                self.lenght -= 1
            else:
                print("There is no element has this value !")
        else:
            # remove the first node value
            if value == self.item:
                third = self.next.next
                self.item = self.next.item
                self.next = third
                # decrement linkedlist lenght
                self.lenght -= 1

            # remove value of a node between 2 nodes
            else:
                found = False
                previous = self
                current = self.next
                Next = self.next.next
                for _ in range(self.lenght-2):
                    previous = previous.next
                    current = current.next
                    Next = Next.next
                    if(current.item == value):
                        found = True
                        break
                if found:
                    previous.next = Next
                    # decrement linkedlist lenght
                    self.lenght -= 1
                else:
                    print("There is no element has this value !")
    
    # method to update an index with a value
    def update(self,index,value):
        # check if index is in range
        if index >= self.lenght or index < 0:
            # handle out of range error
            print('Error , Out of Range Index !')
        else:
            target = self
            for _ in range(index):
                target = target.next
            target.item = value

    # method to swap values of two nodes
    def swap(self,firstIndex,secondIndex):
        # check if indexes in linkedlist range
        if firstIndex >= self.lenght or secondIndex >= self.lenght or firstIndex < 0 or secondIndex < 0:
            # handle out of range error
            print('Error , Out of Range Index !')
        else:
           firstNode = self
           secondNode = self
           # move the first node to the target position
           for _ in range(firstIndex):
               firstNode = firstNode.next
           # move the second node to the target position
           for _ in range(secondIndex):
               secondNode = secondNode.next
           temp = firstNode.item
           firstNode.item = secondNode.item
           secondNode.item = temp

    # function to get the index of a speceific value
    def indexof(self,value):
        current = self
        for i in range(self.lenght):
            if current.item == value:
                return i
            else:
                current = current.next
        print("Error , this value isn't exist in the linkedlist")

    # a function to return a copy of the linkedlist
    def copy(self):
        copy = Node()
        for i in range(self.lenght):
            copy.insert(value = self[i])
        return copy
    
    # operator overloading to Concatenate a new linkedlist to this linkedlist
    def __add__(self,list):
        origin = Node()
        for i in range(self.lenght):
            origin.insert(value = self[i])
        for i in range(list.lenght):
            origin.insert(value = list[i])
        return origin
    
    # return value by it's node index
    # this methode can be used if you want to loop on the linkedlist items
    # this methode is useful when linkedlist items is objects to accsess items methods 
    def __getitem__(self,index):
        # check if index is in range
        if index >= self.lenght or index < 0:
            # handle out of range error
            print('Error , Out of Range Index !')
        else:
            current = self
            for _ in range(index):
                current = current.next
            return current.item

    # operator overloading to assign an array easliy to our linkedlist
    def __eq__(self,list):
        for element in list:
            self.insert(element)