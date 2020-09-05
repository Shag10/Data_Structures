class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_on_head(self, data):
        if self.head == None:
            node = Node(data, self.head)
            self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        listr = ""

        while itr:    
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data, self.head)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_by_value(self, data_after, data):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data==data:
                itr.next = itr.next.next
                break
            itr = itr.next
            
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_on_head(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        

if __name__ == "__main__":
    ll = Linkedlist()
    head = ll.insert_values([7, 47, 89, 65])
    ll.insert_at(3, 70)
    ll.print()
    ll.insert_at(4, 24)
    ll.print()
    ll.insert_at_end(60)
    ll.print()
    ll.insert_by_value(24, 10)
    ll.print()
