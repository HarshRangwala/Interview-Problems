#Creation of the new linked list
class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.header = None
    #Traversing the linked list
        
    def printNodes(self):
        printData = self.header
        while printData is not None:
            print(printData.val)
            printData = printData.next
    #Insert new values --> BEGINING
    def add_first(self, bdata):
        newVal = ListNode(bdata)
        newVal.next = self.header
        self.header = newVal
    #Insert new values --> End
    def add_end(self, edata):
        newVal = ListNode(edata)
        if self.header is None:
            self.header = newVal
            #return
        last = self.header
        while last.next:
            last = last.next
        last.next = newVal
    #Insert new values --> MIDDLE
    def add_middle(self, middle_node, newVal):
        if middle_node is None:
            print("Cannot add due to absence of node")
            return 
        newNode = ListNode(newVal)
        newNode.next = middle_node.next
        middle_node.next = newNode
    #Reverse the elements
    def reverse(self):
        current = self.header
        prev = None
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.header = prev
    #Remove the elements
    def removeNode(self, rm):
        headerVal = self.header
        if headerVal is not None:
            if headerVal.val == rm:
                self.header = headerVal.next
                headerVal = None
                return
        
        while headerVal is not None:
            if headerVal.val == rm:
                break
            prev = headerVal
            headerVal = headerVal.next
        if headerVal == None:
            return
        prev.next = headerVal.next
        headerVal = None

lilist = LinkedList()
lilist.header = ListNode("Monday")
listnext = ListNode("Tuesday")
listnextnext = ListNode("Wednesday")
lilist.header.next = listnext
listnext.next = listnextnext

lilist.add_first("Sunday")
lilist.add_end("Thursday")
lilist.add_middle(lilist.header.next,"Node added in between")
#Remove
lilist.removeNode("Monday")
#reverse the linkedlist
#lilist.reverse()
#Print the linked list
lilist.printNodes()
