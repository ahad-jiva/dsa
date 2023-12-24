from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the freqency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if isinstance(other, HuffmanNode):
            return (self.char == other.char) and (self.freq == other.freq)
        return False

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if isinstance(other, HuffmanNode):
            if self.freq < other.freq:
                return True
            elif self.freq == other.freq:
                if self.char < other.char:
                    return True
                return False
            return False


def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    freq_list = [0] * 256
    f = open(filename, 'r')
    text = f.read()
    f.close()
    for char in text:
        freq_list[ord(char)] += 1
    return freq_list


def create_huff_tree(list_of_freqs):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    huff_node_list = OrderedList()
    for i in range(len(list_of_freqs) - 1):
        if list_of_freqs[i] != 0:
            huff_node = HuffmanNode(i, list_of_freqs[i])
            huff_node_list.add(huff_node)
    if huff_node_list.size() != 0:
        while huff_node_list.size() != 1:
            first = huff_node_list.pop(0)
            second = huff_node_list.pop(0)
            huff_parent = HuffmanNode(min(first.char, second.char), first.freq + second.freq)
            huff_parent.left = first
            huff_parent.right = second
            huff_node_list.add(huff_parent)
        return huff_node_list.pop(0)


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    huff_codes = [''] * 256
    if node:
        create_code_helper(node, huff_codes, '')
    return huff_codes


def create_code_helper(huff_node, list_of_codes, code):
    if huff_node.left:
        create_code_helper(huff_node.left, list_of_codes, code + '0')
    if huff_node.right:
        create_code_helper(huff_node.right, list_of_codes, code + '1')
    if not huff_node.left and not huff_node.right:
        list_of_codes[huff_node.char] += code


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    header = ''
    for i in range(len(freqs) - 1):
        if freqs[i] != 0:
            header = header + str(i) + " " + str(freqs[i]) + " "
    return header.strip()


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    freq_list = cnt_freq(in_file)
    hufftree = create_huff_tree(freq_list)
    huff_codes = create_code(hufftree)
    input_file = open(in_file, 'r')
    input_text = input_file.read()
    input_file.close()
    if input_text != '':
        output = open(out_file, 'w')
        output.write(create_header(freq_list))
        output.write('\n')
        huff_text = ''
        for char in input_text:
            huff_text += huff_codes[ord(char)]
        output.write(huff_text)
        output.close()
        out_file = out_file.replace('.txt', '_compressed.txt')
        compressed = HuffmanBitWriter(out_file)
        compressed.write_str(create_header(freq_list))
        compressed.write_str('\n')
        compressed.write_code(huff_text)
        compressed.close()
    else:
        output = open(out_file, 'w')
        output.close()
        cfilename = out_file.replace('.txt', '_compressed.txt')
        compressed_output = open(cfilename, 'w')
        compressed_output.close()


def huffman_decode(encode_file, decode_file):
    encoded = HuffmanBitReader(encode_file)
    decoded = open(decode_file, 'w')
    header = encoded.read_str()
    if len(header.split()) == 2:
        header_list = header.split()
        decoded.write(chr(int(header_list[0])) * int(header_list[1]))
    bits = []
    reading_bits = True
    while reading_bits is True:
        try:
            bits.append(encoded.read_bit())
        except:
            reading_bits = False
    encoded.close()
    list_of_freqs = parse_header(header)
    total_chars = 0
    for num in list_of_freqs:
        total_chars += num
    huff_tree = create_huff_tree(list_of_freqs)
    current = huff_tree
    chars_written = 0
    bit_index = 0
    while bit_index <= len(bits) - 1 and chars_written != total_chars:
        if not current.left and not current.right:
            decoded.write(chr(current.char))
            current = huff_tree
            chars_written += 1
        elif bits[bit_index] is False:
            current = current.left
            bit_index += 1
        elif bits[bit_index] is True:
            current = current.right
            bit_index += 1
    decoded.close()


def parse_header(header_string):
    split_header = header_string.split()
    ascii_vals = split_header[::2]
    freq_vals = split_header[1::2]
    list_of_freqs = [0] * 256
    for i in range(len(ascii_vals)):
        list_of_freqs[int(ascii_vals[i])] = int(freq_vals[i])
    return list_of_freqs
