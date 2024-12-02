"""

PIMA : Pain In My ASS!!!!

- so i fuckin' loved the theoratical tought of hashing with chaning
  but now that i saw the implementation here's what i realized:

  - its beautiful 💕 but takes time ⏳



"""


class ListNode:
    def __init__(self,key,val,next=None):
        self.key=key
        self.val=val
        self.next=next


class MyHashMap(object):

    def __init__(self):
        self.map = [None] * 1000 
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None

        here i gotta like insert key value into the index that i
        get by mapping.
        - first get index of map to search in.
        - there are 3 possibilities.
          1. indexed linked list has nothing
             - if so then create a new node and place it there
          2. There is a duplicate key inside the indexed LL.
             - if so then traverse thru find it and replace.
          3. doesn't exist:
            - traverse till end place at end.

        """

        #gettin' index bitches!!
        index = key % 1000
        LinkedList = self.map[index]

        if not LinkedList:
            self.map[index] = ListNode(key,value)
            return 
        
        while LinkedList:
            if LinkedList.key == key:
                LinkedList.val=value
                return 
            if LinkedList.next == None:
                break
            LinkedList=LinkedList.next

        LinkedList.next = ListNode(key,value)

        

    def get(self, key):
        """
        :type key: int
        :rtype: int

        - There are 3 possibilities:

           1. The indexed thing doesn't exist
              - if so then return -1

           2. The indexed thing exists but there isnt a key in
              that indexed linkedList.
              - again return -1

           3. The indexed thing and the key exists.
               - if so then return the val of that keyed linkedlist
        """
        index = key % 1000
        LinkedList = self.map[index]

        if not LinkedList:
            return -1

        while LinkedList:
            if LinkedList.key == key:
                return LinkedList.val
            LinkedList=LinkedList.next

        return -1

         

        
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None

        Here There are _ possibilities.

        1. if indexed linked list doesnt exist return
        2. if indexed linked list exis and there isnt a key
           searched
        3. indexed linked list exists and there is a key, then
           remove it.

        """

        index = key % 1000
        LinkedList = self.map[index]

        if not LinkedList:
            return 

        if LinkedList.key == key:
            self.map[index]=LinkedList.next
            return
        prev=None
        while LinkedList:
            if LinkedList.key == key:
                prev.next=LinkedList.next
                return 
            
            prev=LinkedList
            LinkedList = LinkedList.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
