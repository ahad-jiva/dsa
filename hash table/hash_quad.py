
class HashTable:

    def __init__(self, table_size):  # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will 
            be used, if 11 is passed, 11 will be used.)'''
        self.table_size = self.next_prime(table_size)
        self.table = [[None, None]] * self.table_size
        self.num_items = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value can be anything (Object, None, list, etc.).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        hash_value = self.horner_hash(key) % self.table_size
        if self.table[hash_value] == [None, None]:
            self.table[hash_value] = [key, value]
            self.num_items += 1
        elif self.table[hash_value][0] == key:
            self.table[hash_value][1] = value
        else:
            for i in range(1, self.table_size):
                index_offset = i ** 2
                if self.table[(hash_value + index_offset) % self.table_size] == [None, None]:
                    self.table[(hash_value + index_offset) % self.table_size] = [key, value]
                    self.num_items += 1
                    break
                elif self.table[(hash_value + index_offset) % self.table_size][0] == key:
                    self.table[(hash_value + index_offset) % self.table_size][1] = value
                    break
        if self.get_load_factor() > 0.5:
            self.rehash()

    def rehash(self):
        old_table_size = self.table_size
        old_table = self.table
        self.table_size = self.next_prime(2 * self.table_size)
        self.table = [[None, None]] * self.table_size
        self.num_items = 0
        for i in range(old_table_size):
            if old_table[i] != [None, None]:
                self.insert((old_table[i][0]), old_table[i][1])

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        n = min(len(key), 8)
        hash_value = 0
        for i in range(0, n):
            hash_value += ((ord(key[i])) * (31 ** (n - 1 - i)))
        return hash_value

    def is_prime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def next_prime(self, n):
        ''' Find the next prime number that is > n.'''
        if n <= 1:
            return 2
        if self.is_prime(n) is True:
            return n
        prime = n
        found = False
        while found is not True:
            prime = prime + 1
            if self.is_prime(prime) is True:
                found = True
        return prime

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        index = self.horner_hash(key) % self.table_size
        if self.table[index][0] == key:
            return True
        else:
            i = 0
            while self.table[(index + (i ** 2)) % self.table_size][0] != key:
                i += 1
                if self.table[(index + (i ** 2)) % self.table_size][0] == key:
                    return True
                elif self.table[(index + (i ** 2)) % self.table_size] == [None, None]:
                    return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        index = self.horner_hash(key) % self.table_size
        if self.table[index][0] == key:
            return index
        else:
            i = 0
            while self.table[(index + (i ** 2)) % self.table_size][0] != key:
                i += 1
                if self.table[(index + (i ** 2)) % self.table_size] == [None, None]:
                    return None
                elif self.table[(index + (i ** 2)) % self.table_size][0] == key:
                    return (index + (i ** 2)) % self.table_size

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        list_of_keys = []
        for i in range(self.table_size):
            if self.table[i][0] is not None:
                list_of_keys.append(self.table[i][0])
        return list_of_keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.horner_hash(key) % self.table_size
        if self.table[index][0] == key:
            return self.table[index][1]
        else:
            i = 0
            while self.table[(index + (i ** 2)) % self.table_size][0] != key:
                i += 1
                if self.table[(index + (i ** 2)) % self.table_size] == [None, None]:
                    return None
                elif self.table[(index + (i ** 2)) % self.table_size][0] == key:
                    return self.table[(index + (i ** 2)) % self.table_size][1]

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size
