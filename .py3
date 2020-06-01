class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mis=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.mis:
            self.mis.append(val)
            return True
        else:
            self.mis.append(val)
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.mis:
            self.mis.remove(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.mis)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
