# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        linked_pair = self.storage[idx]

        if not linked_pair:
            self.storage[idx] = LinkedPair(key, value)
        else:
            while linked_pair:
                if linked_pair.key == key:
                    linked_pair.value = value
                    break
                elif not linked_pair.next:
                    linked_pair.next = LinkedPair(key,value)
                    break
                
                linked_pair = linked_pair.next
                    


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        cur_node = self.storage[index]
        prev_node = None

        if not self.storage[index]:
            print(f"[WARNING]: key {key} not found.")
        else:
            self.storage[index] = None
        pass
        
        # else traverse the list
        # else:
            
        #     while cur_node.next:
        #         prev_node = cur_node
        #         cur_node = cur_node.next

        #         if cur_node.key == key:
        #             prev_node.next = cur_node.next
        #             return
            
            # if key is not in the list
        # else:
        #     print('ERROR: Key not found.')
        
        # return None
            

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        cur_node = self.storage[index]


        while cur_node:
            # print('cur_node', cur_node.key)
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next
            

        return None
        



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double capacity
        self.capacity = self.capacity * 2
        
        # save old array
        old_storage = self.storage

        # create new/larger array
        self.storage = [None] * self.capacity

        # transfer all key/value pairs
        for linked_pair in old_storage:
            while linked_pair:
                self.insert(linked_pair.key, linked_pair.value)
                linked_pair = linked_pair.next
            # self.storage.insert(old_storage[i].key, old_storage[i].value)
        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
