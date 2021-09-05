class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def after(self,data):
        node = Node(data)
        
        if self.head is None:
            node.prev = None
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            
            cur.next = node
            node.prev = cur
            node.next = None
    def before(self, data):
        node = Node(data)
        
        if self.head is None:
            node.prev = None
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            node.prev = None
        return self.head
        
    def perticularPositions(self,data,pos):
        node = Node(data)
        if self.head == None:
            self.head = node
            return self.head
        else:
            count = 1
            cur = self.head
            while cur.next != None and count < pos:
                prev = cur
                cur = cur.next
                count += 1
            else:
                if cur.next != None:
                    nxt = cur.next
                    cur.next = node
                    node.next = nxt
                    node.prev = cur
                    nxt.prev = node
                else:
                    cur.next = node
                    node.prev = cur
        return self.head
        
    def deleteNode(self,key):
        if self.head == None:
            return
        else:
            cur = self.head
            while cur:
                if key == cur.data and cur == self.head:
                    # Case = 1
                    if not cur.next:
                        cur = None
                        self.head = None 
                        return
                    #case 2
                    else:
                        nxt = cur.next
                        cur.next = None
                        cur.prev = None
                        cur = None
                        nxt.prev = None
                        self.head = nxt
                # case 3
                elif cur.data == key:
                    if cur.next:
                        nxt = cur.next
                        prev = cur.prev
                        prev.next = nxt
                        nxt.prev = prev
                        cur.next = None
                        cur.prev = None
                        cur = None
                        return 
                # case 4
                    else:
                        prev = cur.prev
                        prev.next = None
                        cur.prev = None
                        cur = None
                        return
                cur = cur.next
                    
    def reersed(self):
        if self.head == None :
            return 
        cur = self.head
        prev = None
        while cur is not None:
            # keep prev pointer
            prev = cur.prev 
            
            # change direction
            cur.prev = cur.next
            cur.next = prev
            # traverse backwards
            cur = cur.prev
        if prev:
            self.head = prev.prev
        return self.head
            
        
                    
                    
    def PrntDoubleLLst(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

dllst = DoubleLinkedList()
dllst.after(1)
dllst.after(2)
dllst.after(3)
dllst.after(5)
dllst.after(6)
# dllst.before(10)
# dllst.perticularPositions(4,3)
dllst.PrntDoubleLLst()
print("new DoubleLinkedList")             
# dllst.deleteNode(6)
dllst.reersed()
dllst.PrntDoubleLLst()