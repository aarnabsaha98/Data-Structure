class Stack(object):
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items .pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()
        
class Queue(object):
    def __init__ (self):
        self.items = [ ]
    def enqueue(self,data):
        self.items.insert(0,data)

    def dequeue(self):
        if not self. is_empty():
            return self.items.pop()
    def is_empty(self):
        return  len(self.items) == 0
    def __len__(self):
        return self.size()

    def peek(self):
        if not self. is_empty():
            return self.items[-1].value
    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self,data):
        self. value = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root,  " ")    
        elif traversal_type == 'inorder':
            return self.inorder_tree(tree.root," ")
        elif traversal_type == 'postorder':
            return self.postorder_tree(tree.root," ")
        elif traversal_type == 'levelorder':
            return self.level_traversal(tree.root)
        elif traversal_type == "reverse_levelorder_print":
            return self.reverse_levelorder(tree.root)
    def preorder_print(self,start,traversal):
        #root_left_right
        if start != None:
            traversal += (str(start.value) + "-" ) 
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def inorder_tree(self,start,traversal):
        #left > right > root
        if start:
            traversal = self.inorder_tree(start.left,traversal)
            traversal += (str(start.value) + '_')
            traversal = self.inorder_tree(start.right,traversal)
        return traversal
    def postorder_tree(self,start,traversal):
        # left > root > right
        if start:
            traversal = self.postorder_tree(start.left,traversal)
            traversal = self.postorder_tree(start.right,traversal)
            traversal += (str(start.value) + '_')
        return traversal

    def level_traversal(self,root):
        if root == None:
            return
        else:
            queue = Queue()
            queue.enqueue(root)
            show_tree = ' '
            while len(queue) > 0:
                show_tree = show_tree + str( queue.peek()) + "..>"
           
                root = queue.dequeue()
                if  root.left :
                    queue.enqueue(root.left)
                if  root.right:
                    queue.enqueue(root.right)
            return show_tree
    def reverse_levelorder(self,start):
        if start is None:
            return
        else:
            queue = Queue()
            stack = Stack()
            queue.enqueue(start)
            display = ""
            while len(queue) > 0:
                node = queue.dequeue()
                stack.push(node)
                if node.right :
                    queue.enqueue(node.right)
                if node.left:
                    queue.enqueue(node.left)
            while len(stack) > 0:
                #node = stack.pop()
                display = display + str(stack.pop().value) + "..> "
            return display
            
    def Height_tree(self , node):
        if node is None:
            return -1

        left_height = self.Height_tree(node.left)
        right_height = self.Height_tree(node.right)
        return 1 + max(left_height,right_height)

    def size_tree(self,node):
        if node is None:
            return 0
        else:
            count = 0
            stack = Stack()
            stack.push(node)
            count = count + 1
            while len(stack) > 0:
                node1 = stack.pop()
                if node1.left:
                    count +=1
                    stack.push(node1.left)
                if node1.right:
                    count +=1
                    stack.push(node1.right)
            
            return count 
    def size(self,node):
        if node is None:
            return 0
        
        else:
            count1 = self.size(node.left)
            count2 = self.size(node.right)
        return 1 + (count1+count2)
    
        
tree = BinaryTree(10)
tree.root.left = Node(5)
tree.root.right = Node(15)
tree.root.left.left = Node(3)
tree.root.left.left.right = Node(4)
tree.root.left.right = Node(8)
tree.root.left.right.left = Node(6)
tree.root.right.right = Node(16)
tree.root.right.left = Node(13)
#print(tree.size_tree(tree.root))
#print(tree.size(tree.root))
#print(tree.Height_tree(tree.root.left))
#print('preorder  ')
#print(tree.print_tree('preorder'))
#print('inorder  ')
#print(tree.print_tree('inorder'))
#print('postorder  ')
#print(tree.print_tree('postorder'))
print('levelorder')
print(tree.print_tree('levelorder'))
print('reverse_levelorder_print')
print(tree.print_tree('reverse_levelorder_print'))ka