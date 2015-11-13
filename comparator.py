#!/usr/bin/python2

def compression_ratio(avg_cw_length, original_text_size=8):
    return original_text_size/avg_cw_length

def average_codeword_length(frequencies, code):
	return sum([len(code[x])*frequencies[x] for x in code])


# Testing
frequencies = {'x1': 0.25, 'x2': 0.25, 'x3': 0.2, 'x4': 0.15, 'x5': 0.15}

huffman_code = {'x1':'00', 'x2':'01', 'x3':'10', 'x4':'110', 'x5':'111'}
shannon_code = {'x1':'00', 'x2':'010', 'x3':'10', 'x4':'10110', 'x5':'110110'}
shannon_fano_code = {'x1':'00', 'x2':'01', 'x3':'10', 'x4':'110', 'x5':'111'}

# Get average codeword length
huffman_avg_cw_length = average_codeword_length(frequencies, huffman_code)
shannon_avg_cw_length = average_codeword_length(frequencies, shannon_code)
shannon_fano_avg_cw_length = average_codeword_length(frequencies, shannon_fano_code)

print "Huffman average codeword length", huffman_avg_cw_length
print "Shannon average codeword length", shannon_avg_cw_length
print "Shannon Fano average codeword length", shannon_fano_avg_cw_length

huffman_compression_ratio = compression_ratio(huffman_avg_cw_length)
shannon_compression_ratio = compression_ratio(shannon_avg_cw_length)
shannon_fano_compression_ratio = compression_ratio(shannon_fano_avg_cw_length)

print "Huffman compression ratio", huffman_compression_ratio
print "Shannon compression ratio", shannon_compression_ratio
print "Shannon Fano compression ratio", shannon_fano_compression_ratio