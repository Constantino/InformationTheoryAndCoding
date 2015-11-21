import heapq
from collections import Counter

##################################################################
class Node():
    'Huffman tree nodes'

    def __init__(self, name, frequency):
        self._name = name
        self._frequency = frequency
        self._left = None
        self._right = None

    def setChildren(self, left_node, right_node):
        self._left = left_node
        self._right = right_node

    def getChildren(self):
        return self._left, self._right

    def get_values(self):
        return {self._symbol: self._frequency}

    def __cmp__(self, frequency):
        return cmp(self._frequency, frequency)

    def __repr__(self):
        return "(Key: %s, Value: %s)" % (self._name, self._frequency)
##################################################################

class HuffmanCode():
    'Create huffman code'

    def __init__(self, nodes):
        self._codes={}
        self._nodes = nodes

    def create_tree(self):
        heapq.heapify(self._nodes)
        while len(self._nodes)>1:
            left_node = heapq.heappop(self._nodes)
            right_node = heapq.heappop(self._nodes)
            new_node = Node(left_node._name+right_node._name, left_node._frequency+right_node._frequency)            
            new_node.setChildren(left_node, right_node)
            print new_node
            heapq.heappush(self._nodes, new_node)
        return self._nodes[0]

    def get_codes(self, node, code):
        if node is not None:
            if node._left is None and node._right is None:
                self._codes[node._name] = code
            self.get_codes(node._left, code + '0')
            self.get_codes(node._right, code + '1')

    def huffman_code(self):
        root = self.create_tree()
        self.get_codes(root, '')
        return root, self._codes

##################################################################

def encode(string):
    huffman_code = HuffmanCode(string)
    root, codes = huffman_code.huffman_code()
    encoded = ""
    for e in string:
        encoded += codes[e]
    new_binary = [encoded[i:i+8] for i in range(0, len(encoded), 8)]
    new_string = [chr(int(binary, 2)) for binary in new_binary]
    new_string = "".join(new_string)
    return new_string, root

def get_symbol(node, bits, index):
    if node._left is None and node._right is None:
        return node._name, index
    if bits[index] == '0':
        return get_symbol(node._left, bits, index+1)
    else:
        return get_symbol(node._right, bits, index+1)

def decode(encoded, root):
    decoded = ""
    binary = ''.join(["{0:b}".format(ord(c)).zfill(8) for c in encoded[:-1]])
    binary += "{0:b}".format(ord(encoded[-1])) # Add last character to binary string without padding with zeroes 
    index = 0
    while index < len(binary):
        symbol, index = get_symbol(root, binary, index)
        decoded += symbol
    return decoded
