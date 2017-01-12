import timeit
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
                      
def time_QuadProb():
        """
        :pre: QuadProb class is defined
        :post: return number of collision and time taken
        :desc:  print number of collision and return time taken
        """
        a = QuadProb(1000081,1)
        filename = input("Enter file name: ")
        b= from_file(filename,a)
        start = timeit.default_timer()
        taken = (timeit.default_timer() - start)
        print(b.collision)
        return taken

              
class QuadProb:
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

    def __setitem__(self, key, data):
        """
        :pre: key and data is defined
        :post: new data is set
        :desc: to set data with a specific key
        """
        pos = self.hash(key)
        newPos = 0 
        pos = self.hash(key)
        for _ in range(self.table_size):
            self.collision += 1
            if self.array[pos] is None:
                self.array[pos] = (key,data)
                self.count += 1
                return
            elif self.array[pos][0] == key:
                self.array[pos]=(key,data)
                return
            else:# +1,+4,+9....
                newPos += 1
                pos = (pos+newPos*newPos)%self.table_size
        raise IndexError("Either full or key does not exist")
    
    def __getitem__(self,key):
        """
        :pre: key is defined
        :post: data with the key is returned
        :desc: to return data with its defined key
        """
        pos = self.hash(key)
        newPos = 0
        for _ in range(self.table_size):
            if self.array[pos] is None:
                return None
            elif self.array[pos][0] == key:
                return self.array[pos][1]
            else:
                newPos += 1
                pos = (pos+newPos*newPos)%self.table_size
        raise KeyError(key)
    
    def __contains__(self, item):
        """
        :pre: item is defined
        :post: return True/ False
        :desc: check if array contains the item
        """
        pos = self.hash(item)
        for i in range(self.table_size):
                #check every element in array with the item
            if self.array[pos][0] == item:
                return True #return true if found
        return False #else return false if array doesn't contain the item

    
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


if __name__ == "__main__":
        print(time_QuadProb())
        
