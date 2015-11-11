#!/usr/bin/python2                                                                                                                      
from sys import argv, exit

text = argv[1]
debug = int(argv[2]) //flag to debug

def  parsing_text(pos,k,text):
    
    sub_string = text[pos:k]

    counting = dict()

    counting[sub_string] = 0

    print count_sub_string(pos, k, sub_string, text,counting)

    return 

def count_sub_string(pos,k,sub_string, text, counting):
    
    len_sub_string = len(sub_string)

    if pos+len_sub_string == len(text)+1:
        if debug == 1:
            print "end"
        return counting

    if debug == 1:
        print "pos,k : ", pos,",",pos+k
        print "val: ",text[pos:pos+k]

    if sub_string == text[pos:pos+k]:
        counting[sub_string] += 1 

    return count_sub_string(pos+1,k,sub_string,text,counting)

parsing_text(0,1,text)
