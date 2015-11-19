#!/usr/bin/python2
from sys import argv
from collections import Counter, OrderedDict

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
    for symbol in word:
        rang = high - low
        high = low + rang*ranges[symbol][1]
        low = low + rang*ranges[symbol][0]
    return (high+low)/2

if __name__=='__main__':
    try:
        string = argv[1]
    except:
        #string = "no llores la muerte de tu cuerpo ni llores la muerte de tu alma."
        string = "alaladoaroloro" # String for testing purposes

    frequencies = Counter(string)
    probability = {s : float(frequencies[s]) / len(string) for s in frequencies}

    word = 'al' # Word to be encoded for testing
    encoded = arithmeticCoding(probability, word)
    print word + " =", encoded