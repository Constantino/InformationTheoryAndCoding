#!/usr/bin/python2                                                                                                                      
from sys import argv, exit

text = argv[1]
ks = int(argv[2])

len_text = len(text)
counting = dict()

def  parsing_text(pos,k,text):
    
    sub_string = text[pos:pos+k]

    len_sub_string = len(sub_string)

    if pos+len_sub_string > len_text or len_sub_string < k:
        return

    if sub_string not in counting:

        counting[sub_string] = 0

        count_sub_string(pos, k, sub_string, len_sub_string, text,counting)

    return parsing_text(pos+1,k,text)

def count_sub_string(pos,k,sub_string,len_sub_string, text, counting):

    if pos+len_sub_string > len_text:
        return

    if sub_string == text[pos:pos+k]:
        counting[sub_string] += 1 

    return count_sub_string(pos+1,k,sub_string, len_sub_string,text,counting)


for k in range(1,len_text+1):
    print "k: ",k
    parsing_text(0,k,text)
    print counting


print "dict counting: ", counting
