#!/usr/bin/python2
from sys import argv, exit

try:
    string = argv[1]
    k = int(argv[2])
except:
    exit("Usage: ./vic-k-mer.py string k")

string_length = len(string)

def get_kmers(string, k):
	kmers = list()
	for pos in xrange(0, string_length-1):
		kmers.append(string[pos:pos+k])
	return kmers

kmers = get_kmers(string, k)
frequencies = [string.count(kmer) for kmer in kmers]
print kmers, frequencies