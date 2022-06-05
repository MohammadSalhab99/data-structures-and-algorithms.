class HashTable(object):
    def __init__(self, size = 1024):
    
        self.size = size
        self.map = [None]*size
        # self.map = [[]]*size
        # self.map = [LinkedList()]*size
    def _get_hash(self, key):
        """
        - ascii code of a key summation
        - encode chars in key into oct and add it to ascii sum
        - Prime = 19 then multiply it by ascii sum
        - mod the result over self.size
        - return the hashed value
        """
        # Hello
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch) #86
            sum_of_ascii+=ch_ascii
        hashed_key = (sum_of_ascii*19)%self.size

        return hashed_key

    def __setitem__(self, key, value):
    # def __setitem__(self, key, value):
        # get index from get_hash
        idx = self._get_hash(key)
        # check if the bucket at that index is empty, add the value there
        if not self.map[idx]:
            self.map[idx] = [[key, value]] # LinkedList().add({key, value})
        # if the bucker is not empty, append, add to the sotrage object(collision)
        else:
            self.map[idx].append([key, value])


    def contains(self,key):
        """This method takes a key and returns True if the key in the hash table else
        return False
        Args:
            key  
        Returns:
             Boolean: indicating if the key exists in the table already.
        """
        idx = self._get_hash(key)
        if self.map[idx] !=None:
            for i in self.map[idx]:
                if key == i[0]:
                    return True
            return False
        else:
            return False
        

    # def find(self, key):
    def __getitem__(self, key):
        # call the get hash method and send the key to it
        idx = self._get_hash(key)
        if(self.map[idx]==None):
            return None
        # get that index and look it up from the map
        # return the value stroed in that index
        for i in self.map[idx]:
                if key == i[0]:
                    return  i[1]
        
    
    def keys(self):
        """this method returns all the keys in the hash table
        Returns:
            list: collection of all the keys in the hash table
        """
        keys_list = []
        for i in self.map:
            if i != None:
                for k in i:
                    keys_list.append(k[0])
        return keys_list
                    

if __name__ == "__main__":
    hashtable = HashTable()
    hashtable.__setitem__("cloud", "AWS")
    hashtable.__setitem__("cloud", "Azure")
    hashtable.__setitem__("could", "Rainy")
    hashtable.__setitem__("name", "Python")
    print(hashtable["name"])
    print(hashtable.contains('Azure'))
    print(hashtable.keys())



    for item in enumerate(hashtable.map):
        if item is not None:
            print(item)