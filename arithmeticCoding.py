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

def get_word_intervals(word, probabilities):

    first_ranges = compute_ranges(probabilities)

    first_character_ranges = ranges[word[0]]



    return intervals

def process_word_ranges(ranges, alphabet, character):

    interval = ranges[character]
    print " ... interval: ",interval
    new_ranges = dict()

    for c in alphabet:
        if c == alphabet[0]:
            new_ranges[c] = [interval[0],interval[0]+ranges[c][1]*interval[1]]
        elif c == alphabet[-1]:
            new_ranges[c] = [ranges[c][0]*interval[1],interval[1]]
        else:
            new_ranges[c] = [ranges[c][0]*interval[1],ranges[c][1]*interval[1]]

    #print new_ranges

    return new_ranges

def get_ranges(probabilities,alphabet):

    ranges = dict()
    freq_ac = 0
    for e in alphabet:
        ranges[e] = [freq_ac,probabilities[e]+freq_ac]
        freq_ac = probabilities[e]+freq_ac

    return ranges

def arithmeticCoding(probabilities, word,alphabet):

    #ranges = compute_ranges(probabilities)
    ranges = get_ranges(probabilities,alphabet)

    
    for symbol in word:
        print "symbol: ", symbol, " __ ",ranges[symbol]
    

    print "****"

    my_ranges = ranges
    for c in word[:-1]:
        print "character: ",c
        my_ranges = process_word_ranges(my_ranges, alphabet, c)

        print "my_new_ranges: ",my_ranges
    print "****"

    #Testing
    l = my_ranges['l'][1] - my_ranges['l'][0]
    t = find_t(l)
    print "t: ",t
    x = find_x(my_ranges['l'][0],my_ranges['l'][1],t)
    print "x: ",x
    r = find_r(x,t)
    print "r: ",r
    
    return r

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
    print "alfa: ",alfa," -- beta: ",beta
    integers = []

    for e in range(int(ceil(alfa)),int(ceil(beta))):
        integers.append(e)

    if len(integers) > 1:
        for e in integers:
            if e%2 == 0:
                return e
    return integers[0]

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
        string = "nolloreslamuertedetucuerponilloreslamuertedetualma"
        #string = "alaladoaroloro" # String for testing purposes

    print "string len: ",len(string)
    frequencies = Counter(string)
    frequencies = sorted(frequencies.items())
    print "frequencies_s: ",frequencies

    alphabet = []
    for key,value in frequencies:
        #print key,value
        alphabet.append(key)
    probability = {key : float(value) / len(string) for key,value in frequencies}

    #print "my ranges: ",get_ranges(probability,alphabet)

    print "probability: ", probability

    #word = 'alo' # Word to be encoded for testing
    words = ['no', 'llores', 'la', 'muerte', 'de', 'tu', 'cuerpo', 'ni', 'llores', 'la', 'muerte', 'de', 'tu', 'alma']
    coding = dict()
    for word in words:
        #word = "llores"
        encoded = arithmeticCoding(probability, word,alphabet)
        print word + " =", encoded
        #print binary_expansion(encoded, '')
        coding[word] = binary_expansion(encoded, '')

    print "**** CODING: ",coding



