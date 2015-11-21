from collections import Counter
from HuffmanCoding import *

if __name__ == '__main__':
    
    frequencies = Counter()
    nodes = {}
    
    while raw_input('Enter new word? [y/n] ') == 'y':
        word = raw_input('Enter word: ')

        for symbol in word:
            frequencies[symbol] += 1

        for e, f in frequencies.items():
            if e not in nodes:
                nodes[e] = Node(e, f)
            else:
                nodes[e]._frequency = f

        print nodes
        
        huffman_code = HuffmanCode(nodes.values())
        root, codes = huffman_code.huffman_code()

        print codes

