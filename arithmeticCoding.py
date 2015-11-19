#!/usr/bin/python2
from sys import argv
from collections import Counter, OrderedDict

def compute_ranges(probabilities):
	keys = probabilities.keys()
	print keys
	first_range = (keys[0], (0.0, probabilities[keys[0]]))
	ranges = list()
	ranges.append(first_range)
	accumulated = probabilities[keys[0]]
	internal_ranges = list()
	for i in range(len(keys))[1:-1]:
		internal_ranges.append((keys[i], (accumulated, accumulated+probabilities[keys[i]])))
		accumulated += probabilities[keys[i]]
	ranges.extend(internal_ranges)
	#ranges.extend([(keys[i], (probabilities[keys[i-1]], probabilities[keys[i]])) for i in range(len(keys))[1:-1]])
	last_range = (keys[-1], (accumulated, 1.0))
	ranges.append(last_range)
	print ranges
	return ranges

def arithmeticCoding(probabilities, word):
	encoded = ""
	high = 1.0
	low = 1.0
	ranges = compute_ranges(probabilities)
	#for s in word:
		#a = 
		#subinterval(a, b)
	return encoded

if __name__=='__main__':
	try:
		string = argv[1]
	except:
		#string = "no llores la muerte de tu cuerpo ni llores la muerte de tu alma."
		string = "alaladoaroloro"
	frequencies = Counter(string)
	probability = {s : float(frequencies[s]) / len(string) for s in frequencies}
	print probability
	word = 'ala' # Word to be encoded
	encoded = arithmeticCoding(probability, word)

