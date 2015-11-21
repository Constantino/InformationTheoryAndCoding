from collections import Counter

class Node():

    def __init__(self, symbol, frequency):
        self._symbol = symbol
        self._frequency = frequency
        self._left = None
        self._right = None

    def setChildren(self, left_node, right_node):
        self._left = left_node
        self._right = right_node

    def getChildren(self):
        return self._left, self._right

    def __cmp__(self, frequency):
        return cmp(self._frequency, frequency)

    def __repr__(self):
        return "Key: %s Value: %s" % (self._symbol, self._frequency)

    def get_values(self):
        return {self._symbol: self._frequency}


if __name__ == '__main__':
    
    frequencies = Counter()
    nodes = {}
    
    while raw_input('Enter new word? [y/n] ') == 'y':
        word = raw_input('Enter word: ')

        for symbol in word:
            frequencies[symbol] += 1
        print frequencies

        for e, f in frequencies.items():
            if e not in nodes:
                nodes[e] = Node(e, f)
            else:
                nodes[e]._frequency = f

        print nodes
