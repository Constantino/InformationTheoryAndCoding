#!/usr/bin/python2                                                                                                                      
from sys import argv, exit

text = argv[1]

len_text = len(text)
counting = dict()

frequencies = []
buffer_last_values = dict()
def  parsing_text(pos,k,text):
    
    sub_string = text[pos:pos+k]

    len_sub_string = len(sub_string)

    if pos+len_sub_string > len_text or len_sub_string < k:
        return

    if sub_string not in counting:

        counting[sub_string] = 0

        count_sub_string(pos, k, sub_string, len_sub_string, text,counting)

        buffer_last_values[sub_string] = counting[sub_string]
        frequencies.append(counting[sub_string])

    return parsing_text(pos+1,k,text)

def count_sub_string(pos,k,sub_string,len_sub_string, text, counting):

    if pos+len_sub_string > len_text:
        return

    if sub_string == text[pos:pos+k]:
        counting[sub_string] += 1 

    return count_sub_string(pos+1,k,sub_string, len_sub_string,text,counting)

k_mer = dict()
k_mer_most_freq = {"e": 0, "value":0}
def find_kmer_most_frequent():
    for e in counting:
        k_mer[e] = len(e)*counting[e]
        if k_mer[e] > k_mer_most_freq["value"]:
            k_mer_most_freq["e"] = e
            k_mer_most_freq["value"] = k_mer[e]

    print "k_mer_most_freq: ",k_mer_most_freq

still_continue = True
k = 1
while (still_continue and k < len_text):
    
    frequencies = []
    buffer_last_values = {}
    parsing_text(0,k,text)
    
    still_continue = False
    for e in frequencies: #Continue while at least one of the frequencies is greater than 1
        if e > 1:
            still_continue = True

    if still_continue == False: #if all frequencies == 1 then remove those keys from the dictionary
        for e in buffer_last_values:
            del counting[e]

    k += 1
    
#print "dict counting: ", counting

find_kmer_most_frequent()



