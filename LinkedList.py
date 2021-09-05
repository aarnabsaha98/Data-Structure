

# 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9 
class Node:
    def __init__(self,data=None):
        self.next = None
        self.data = data
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def prepend(self,data):
        new_mode = Node(data)
        new_mode.next = self.head
        self.head = new_mode
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
             
    
    def  insertSpecificPos(self,data,pos):
        
        new_node = Node(data)
        count = 1
        cur = self.head
        if self.head is None :
            # new_node.next = self.head 
            self.head = new_node

        else:
            while cur.next is not None and count < pos:
                cur = cur.next
                count +=1 
            # coonection 1>new node to next node of that pos 
                        #2> cur node to the new node
            new_node.next = cur.next
            cur.next = new_node
            
            
    def deleteNode(self,pos):
        if pos == 0:
            self.head = self.head.next
            
        else:
            count = 1
            cur = self.head
            while cur.next is not None and count < pos:
                cur = cur.next
                count +=1
            cur.next = cur.next.next
        
    def ReversePrint(self):
        if self.head == None:
            return 
        else:
            stack = []
            rev = []
            cur = self.head
            while cur is not None:
                stack.append(cur.data)
                cur = cur.next
            while stack: 
                rev.append(stack.pop())
        print(rev)
        
    def reverse(self):
        if self.head is None:
            return
        else:
            prev = None
            cur = self.head
            while cur :
                nxt = cur.next 
                # change arrow direction t
                cur.next = prev 
                # shift nodes
                prev = cur
                cur = nxt 
            self.head = prev
            
            
            
    def lenght(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total
    
    

    def printLinkedList(self):
        cur = self.head
        elements = []
        while cur is not None:
            print(cur.data)
            cur = cur.next
            
        # print(elements)
        
mylist = LinkedList()
mylist.prepend(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
# mylist.insertSpecificPos(5,4)
# mylist.printLinkedList()
# mylist.deleteNode(5)
# (mylist.ReversePrint())
mylist.reverse()
mylist.printLinkedList()
# print(mylist.lenght())