class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
             self.arr[h].append((key,val))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


if __name__ == "__main__":
    t = Hashtable()
    t["march 6"] = 400
    t["march 6"] = 74
    t["march 9"] = 43
    t["april 20"] = 700
    t["march 17"] = 300
    
    print(t.arr)
    del t["march 6"]
    print(t.arr)
