from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = HashTable(191)  # hash table for stop words
        self.concordance_table = HashTable(191)  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            input_text = open(filename, 'r')
            stop_table = input_text.readlines()
            input_text.close()
        except FileNotFoundError:
            raise FileNotFoundError
        for i in range(len(stop_table)):
            stop_table[i] = stop_table[i].replace("\n", '')
        for word in stop_table:
            self.stop_table.insert(word)

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        input_text = open(filename, 'r')
        word_table = input_text.readlines()
        input_text.close()
        for i, line in enumerate(word_table):
            line = line.replace("'", '')
            no_punc = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
            lowercase = no_punc.lower()
            line_list = lowercase.split()
            single_words = []
            for word in line_list:
                if word.isalpha():
                    single_words.append(word)
            line_keys = dict.fromkeys(single_words)
            for word in line_keys:
                if not self.stop_table.in_table(word) and not self.concordance_table.in_table(word):
                    self.concordance_table.insert(word, i + 1)
                elif (not self.stop_table.in_table(word)) and (self.concordance_table.in_table(word)):
                    value = self.concordance_table.get_value(word)
                    self.concordance_table.insert(word, f'{value} {i + 1}')

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        output = open(filename, 'w')
        keys = self.concordance_table.get_all_keys()
        keys.sort()
        for key in keys:
            output.write(f'{key}: {self.concordance_table.get_value(key)} \n')
        output.close()
