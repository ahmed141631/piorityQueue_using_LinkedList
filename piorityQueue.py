# create the node class that will represent elements in the piorityqueue

#will create the piorityqueue using linkedlists


class Node():
    def __init__(self,item,piority):
        self.item = item
        self.piority = piority
        self.next = None
class PiorityQueue():
    def __init__(self):
        self.head = None

    def enqueue(self,item,piority):
        newnode=Node(item,piority)
        #case 1:
        if self.head is  None:
            self.head = newnode
            return
        #case 2:
        if piority > self.head.piority:
            newnode.next = self.head
            self.head = newnode
            return
        
        #case 3: iterate from the head until find the sutabile postion

        temp=self.head
        while temp is not None and temp.next.piority>=temp.piority:
            temp=temp.next
            newnode.next=temp.next
            temp.next=newnode
        

    def dequeue(self):
        if self.isEmpty():
           raise Exception("the queue is empty")
        element=self.head.item
        self.head=self.head.next
        return element
    

    def peek(self):
        if self.isEmpty():
            raise Exception("the queue is empty")
        return self.head.item

    def isEmpty(self):
       return self.head==None
        
    def isFull(self):
        return False
    
    def getsize(self):
        count=0
        temp=self.head

        while temp is not None:
            count=count+1
            temp=temp.next

        return count     
    def clear(self):
        self.head=None

    def remove(self,item):
        if self.isEmpty():
            raise Exception("the queue is empty")
        
        if self.head.item == item:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next is not None:
            if temp.next.item == item:
                temp.next = temp.next.next
                return
            current = current.next

        raise Exception("Item not found in queue")
    


    def changePiority(self,item,newPiority):
        self.remove(item)
        self.enqueue(item,newPiority)

        

    
        
        
        
