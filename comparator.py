#!/usr/bin/python2
from collections import OrderedDict

def compression_ratio(avg_cw_length, original_text_size=8):
    return original_text_size/avg_cw_length

def average_codeword_length(frequencies, code):
	return sum([len(code[x])*frequencies[x] for x in code])

def compare(frequencies, huffman_code, shannon_code, shannon_fano_code):
    # Get average codeword length
    huffman_avg_cw_length = average_codeword_length(frequencies, huffman_code)
    shannon_avg_cw_length = average_codeword_length(frequencies, shannon_code)
    shannon_fano_avg_cw_length = average_codeword_length(frequencies, shannon_fano_code)

    # Compute compression ratios
    huffman_compression_ratio = compression_ratio(huffman_avg_cw_length)
    shannon_compression_ratio = compression_ratio(shannon_avg_cw_length)
    shannon_fano_compression_ratio = compression_ratio(shannon_fano_avg_cw_length)

    ordered_frequencies = OrderedDict(sorted(frequencies.items()))

    print
    print "{:<6} {:<12} {:<10} {:<15} {:<10}".format('Symbol', 'Frequency', 'Shannon', 'Shannon Fano', 'Huffman')
    for x in ordered_frequencies:
        print "{:<6} {:<12} {:<10} {:<15} {:<10}".format(x, frequencies[x], shannon_code[x], shannon_fano_code[x], huffman_code[x])

    print
    print "{:<14} {:<20} {:<18}".format('Coding method', 'Avg codeword length', 'Compression Ratio')
    print "{:<14} {:<20} {:<.5f}".format('Huffman', huffman_avg_cw_length, huffman_compression_ratio)
    print "{:<14} {:<20} {:<.5f}".format('Shannon', shannon_avg_cw_length, shannon_compression_ratio)
    print "{:<14} {:<20} {:<.5f}".format('Shannon Fano', shannon_fano_avg_cw_length, shannon_fano_compression_ratio)
    print

if __name__=="__main__":
    # Testing
    frequencies = {'x1': 0.25, 'x2': 0.25, 'x3': 0.2, 'x4': 0.15, 'x5': 0.15}
    huffman_code = {'x1':'00', 'x2':'01', 'x3':'10', 'x4':'110', 'x5':'111'}
    shannon_code = {'x1':'00', 'x2':'010', 'x3':'10', 'x4':'10110', 'x5':'110110'}
    shannon_fano_code = {'x1':'00', 'x2':'01', 'x3':'10', 'x4':'110', 'x5':'111'}

    compare(frequencies, huffman_code, shannon_code, shannon_fano_code)