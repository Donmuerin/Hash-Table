import timeit
from seperateChain_my_linked_list import *
def from_file(filename, hash_table):
        """
        :pre: filename is defined
        :post: return the array from file
        :desc: read from file and display all the value of it
        """
        infile = open(filename,'r')#read file
        #split it line by line and then read it
        contents = infile.read().splitlines()
        for i in contents:
                hash_table[i]=i
        infile.close()#close infile
        return hash_table
                      
def time_SeperateChain():
        """
        :pre: SeperateChain class is defined
        :post: return number of collision and time taken
        :desc:  print number of collision and return time taken
        """
        a = SeperateChain(250727,250726)
        filename = input("Enter file name: ")
        from_file(filename,a)
        start = timeit.default_timer()
        taken = (timeit.default_timer() - start)
        print(a.collision)
        return taken

              
class SeperateChain:
    """
    :pre: table size is the paramenter
    :post: array is changed
    :desc: a basic hash table function
    """
    def __init__(self, table_size, b):
        self.count = 0
        self.table_size = table_size
        self.b = b
        self.array = self.table_size * [None]
        self.collision = 0
        
    def __len__(self):
        """
        :pre: count is defined
        :post: count is returned
        :desc: return length
        """
        return self.count

    def __str__(self):
        """
        :pre: array is defined
        :post: result is returned
        :desc: print with the form of {:}
        """
        result = ""
        for item in self.array:
            if item is not None:
                (key, value)=item
                result += '{'+str(key)+':'+str(value)+'}'
        return result

    def __setitem__(self, key, value):
        """
        :pre: key and data is defined
        :post: new data is set
        :desc: to set data with a specific key
        """
        pos = self.hash(key)
        if self.array[pos] is None:
            counter = 1 #initial to 1
            start = Node((key,value), None)#link is None
            #number of element at that position and start is that node(eg(key,value))
            self.array[pos] = (counter,start)
            self.count += 1
        else:
            #if it's an existing position
            #'now' is my key and its value
            now = self.array[pos][1]# to access the node
            counter = self.array[pos][0]#to access the count
            head = now
            before = None
            while now is not None:#to check again not None
                if now.item[0] != key:
                    before = now# the previous one is the current item now
                    now = now.next# so the next time become now
                    self.collision += 1 #add collision
                    self.count+= 1
                else:# if the item is equal the key
                    now.item = (key,value)#update
                    return
            #initial the next key(which collision started at)
            before.next = Node((key, value), None)
            counter += 1#so that the number of element at that particular position
            self.array[pos] = (counter,head)
            #so now I update the count and only show the first item that placed at that position
                
                
    def __getitem__(self,key):
        """
        :pre: key is defined
        :post: data with the key is returned
        :desc: to return data with its defined key
        """
        pos = self.hash(key)
        now = self.array[pos][1]
        count = self.array[pos][0]
        head = now #assign to a new variable head
        before = None
        while now is not None:#so that directly skip None
            #read through all the key
            if now.item[0] != key:
                before = now
                #so that 'before' is the first element
                now = now.next
            else:#if equal to key
                #now.item is what the element we want to get
                return now.item[1]                     
        raise KeyError(key)
    
    def __contains__(self, key):
        """
        :pre: item is defined
        :post: return True/ False
        :desc: check if array contains the item
        """
        pos = self.hash(key)
        if self.array[pos] is None:
            return None
        else:
            now = self.array[pos][1]
            count = self.array[pos][0]
            head = now
            before = None
            while now is not None:
                #check if contains
                if now.item[0] != key:
                    return False
                else:
                    return True
        raise KeyError(key)
    
    def hash(self, key):
        """
        :pre: key is defined
        :post: value is returned
        :desc: to calculate the hash value for the given key
        """
        value = 0
        # pick two primes
        a = 31415
        b= self.b
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.table_size
            # each character has a randomly chosen base
            a = a * b % (self.table_size - 1)  # this is one way to do it
        return value

    def __iter__(self):
        """
        :pre: None
        :post: return iterator
        :desc: iterator function so that can access the key from hash table
        """
        return (item[0] for item in self.array if item is not None)
        
if __name__ == "__main__":
        print(time_SeperateChain())
        
