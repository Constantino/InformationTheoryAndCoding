#!/usr/bin/python2
from sys import argv
from collections import Counter, OrderedDict
from math import pow,ceil

def compute_ranges(probabilities):
    keys = probabilities.keys()
    ranges = dict()
    ranges[keys[0]] = (0.0, probabilities[keys[0]])
    accumulated = probabilities[keys[0]]
    for i in range(len(keys))[1:-1]:
        ranges[keys[i]] = (accumulated, accumulated+probabilities[keys[i]])
        accumulated += probabilities[keys[i]]
    ranges[keys[-1]] = (accumulated, 1.0)
    print "Ranges", ranges
    return ranges   

def arithmeticCoding(probabilities, word):
    high = 1.0
    low = 0.0
    ranges = compute_ranges(probabilities)

    #Testing
    t = find_t(.0612)
    x = find_x(0.1020,0.1632,t)
    r = find_r(x,t)
    
    print "t: ",t
    print "x: ",x
    print "r: ",r
    
    return r
    
    """
    for symbol in word:
        rang = high - low
        high = low + rang*ranges[symbol][1]
        low = low + rang*ranges[symbol][0]
    return (high+low)/2
    """

#Method 1
def find_t(l):
    t = 0
    while (1.0/pow(2,t) > l):
        t += 1

    return t

def find_x(alfa, beta, t):
    den = pow(2,t)
    alfa *= den
    beta *= den

    integers = []

    for e in range(int(ceil(alfa)),int(ceil(beta))):
        integers.append(e)

    for e in integers:
        if e%2 == 0:
            return e
    return 

def find_r(x,t):
    return x/pow(2,t)

def binary_expansion(word, binary):
    word = word*2
    if word > 1:
        return binary_expansion(word - 1, binary + '1')
    elif word < 1:
        return binary_expansion(word, binary + '0')
    else:
        binary += '1'
        return binary


if __name__=='__main__':
    try:
        string = argv[1]
    except:
        #string = "no llores la muerte de tu cuerpo ni llores la muerte de tu alma."
        string = "alaladoaroloro" # String for testing purposes

    frequencies = Counter(string)
    for f in frequencies:
        print f, frequencies[f]
    probability = {s : float(frequencies[s]) / len(string) for s in frequencies}

    word = 'al' # Word to be encoded for testing
    encoded = arithmeticCoding(probability, word)
    print word + " =", encoded
    print binary_expansion(encoded, '')