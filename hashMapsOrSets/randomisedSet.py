class RandomizedSet(object):

    def __init__(self):
        self.Set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.Set:
            return False
        else:
            self.Set.add(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.Set:
            self.Set.remove(val)
            return True
        else:
            return False

        

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(list(self.Set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
