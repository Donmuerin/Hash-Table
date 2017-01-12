import timeit
def from_file(filename, hash_table):
        """
        :pre: filename is defined
        :post: return the array from file
        :desc: read from file and display all the value of it
        """
        infile = open(filename,'r')
        #split it line by line and then read it
        contents = infile.read().splitlines()
        for i in contents:
                hash_table[i]=i
        infile.close()#close infile
        return hash_table

def freq_file(filename, hash_table):
        """
        :pre: filename and hash_table are defined
        :post: return the <word,frequency>
        :desc: read from file and display all the value of it
        """
        infile = open(filename,'r')
        contents = infile.read().splitlines()
        for i in contents:
            for a in i.split():
                #if the word is previously in hash table
                if a in hash_table:
                    hash_table[a]+=1
                else:
                    hash_table[a]=1

        infile.close()
        return hash_table

def zip_laws1(max_freq, hash_table):
        """
        :pre: max_freq and hash_table are defined
        :post: return the rank
        :desc: ask user to type a word and return its rank
        """
        a = input('Enter word: ')
        num = hash_table[a]
        if num >= int((max_freq / 100)) or num == int((max_freq/ 100)):
                print('Common')
        elif num >= int((max_freq / 1000))or num == int((max_freq / 1000)):
                print('Uncommon')
        else:
                print('rare')
                
def find_max(hash_table):
        """
        :pre: hash_table is defined
        :post: return the maximum value
        :desc: read in a hash_table and return max value
        """
        count = 0
        for bla in hash_table:
            if bla is not None:
                num = hash_table[bla]
                if num is not None:
                    #print(num)
                    if num > count:
                        count = num
        return count
                
def zip_laws(max_freq, hash_table):
        """
        :pre: max_freq and hash_table are defined
        :post: return the hash_table
        :desc: return a result in <word,rank>
        """
        for a in hash_table:
            if a is not None:#prevent to read in any None
                num = hash_table[a]
                if num is not None:#prevent to read in any None
                    #use int because num cannot compare to float
                    if num >= int((max_freq / 100)) or num == int((max_freq/ 100)):
                        hash_table[a]='Common'
                    elif num >= int((max_freq / 1000))or num == int((max_freq / 1000)):
                        hash_table[a]='uncommon' 
                    else:
                        hash_table[a]='rare'
        return hash_table
                        
def another_file(hash_table):
        """
        :pre: hash_table is defined
        :post: return a new hash_table called 'a'
        :desc: return a compared hash_table that contains<word,rank>
        """
        a = QuadProb(1000081,1)
        file = input("File name: ")
        infile = open(file,'r')
        contents = infile.read().splitlines()
        for i in contents:
            for b in i.split():
                #if the word is previously in hash table
                if b in a:
                    a[b]+=1
                else:
                    a[b]=1

        infile.close()
        for j in a:
            if j is not None:#prevent to read in any None
                for v in hash_table:# bei compare
                    if v is not None:
                        if j == v:
                            #print(j)
                            num = hash_table[v]
                            #print(num)
                            a[j] = num
        for j in a:
            if a[j] != 'Common' and a[j] != 'uncommon' and a[j] != 'rare':
                a[j] = 'mispelled'

        return(a)

   
def rank_percent(hash_table):
    """
    :pre: read in another_file(hash_table)
    :post: return the percentage of the words
    :desc: return the percentage
    """
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    total = len(hash_table)
    print(total)
    for i in hash_table:
        if hash_table[i] == 'Common':
            count1 += 1
        elif hash_table[i] == 'uncommon':
            count2 += 1
        elif hash_table[i] == 'rare':
            count3 += 1
        else:
            count4 += 1
    print("Percentage of Common: "+ str((count1/total)* 100)+ "%")
    print("Percentage of Uncommon: "+ str((count2/total)* 100)+ "%")
    print("Percentage of Rare: "+ str((count3/total)* 100)+ "%")
    print("Percentage of Mispelled: "+ str((count4/total)* 100)+ "%")                 

def time_QuadProb():
        """
        :pre: QuadProb class is defined
        :post: return number of collision and time taken
        :desc:  print number of collision and return time taken
        """ 
        a = QuadProb(1000081,1)
        filename = input("Enter file name: ")
        b = from_file(filename,a)
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
            else:#As from the LN, we know that it is +1,+4,+9....
                newPos += 1
                pos = (pos+newPos*newPos)%self.table_size
        self.rehash(self.table_size*100+1)
        self.__setitem__(key,data)
        
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
            else:#technically I need to write pos+(self.collision**2)
                #But I will check 1 by 1 if there has different key
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
        for _ in range(self.table_size):
            if self.array[pos] is None or self.array[pos][0] != item:
                    return False
            else:
                    return True

    
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

    def rehash(self,size): #take in new size
        """
        :pre: size is defined
        :post: a new hash table is returned
        :desc: rehash (resize)
        """
        if size < 1:
            raise ValueError("Size cannot less than 1")
        self.b = self.b
        copy = QuadProb(size,self.b)
        #print(self.array)
        for i in range(len(self.array)):
            if self.array[i] is not None:
                copy[self.array[i][0]]=self.array[i][1]
        self.table_size = size
        #self.resize += 1
        self.array = copy.array
        
    def delete(self,key):
        """
        :pre: key is defined
        :post: a new hash table is returned
        :desc: to delete key and its data
        """
        pos = self.hash(key)
        for i in range(self.table_size):
            if self.array[pos] is None:
                raise KeyError("Cannot delete None")
            elif self.array[pos][0] == key:
                item = self.array[pos]
                self.array = [i for i in self.array if i != item]
                #so that the delete item is what the previous collision happened
                #the key will placed at that spot
                #to rehash all the key
                #based on the concept of LN instead of swift things
                self.rehash(self.table_size)
                return
            else:
                pos = (pos+1)%self.table_size
        raise KeyError("The key is not exist!")
    
    def __iter__(self):
        """
        :pre: None
        :post: return iterator
        :desc: iterator function so that can access the key from hash table
        """
        return (item[0] for item in self.array if item is not None)
        

if __name__ == "__main__":
        a = QuadProb(20,1)
       
