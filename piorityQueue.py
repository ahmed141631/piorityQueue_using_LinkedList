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

    def enqueue(self, item, piority):
     newnode = Node(item, piority)

    # case 1: the queue is empty
     if self.head is None:
        self.head = newnode
        return

    # case 2: the new node has higher priority than the head
     if  piority> self.head.piority:
        newnode.next = self.head
        self.head = newnode
        return

    # case 3: the new node has lower or equal priority than the head
     temp = self.head
     while temp.next is not None and temp.next.piority >= piority:
        temp = temp.next

     newnode.next = temp.next
     temp.next = newnode

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
            temp = temp.next

        raise Exception("Item not found in queue")
    


    def changePiority(self,item,newPiority):
        self.remove(item)
        self.enqueue(item,newPiority)
    def print(self):
        temp = self.head

        while temp is not None:
            print((temp.item,temp.piority))
            temp = temp.next


if __name__ == '__main__':
    # main body starts here...
        pq = PiorityQueue()
        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)

        pq.print()


    
        
        
        
