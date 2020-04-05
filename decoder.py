#!/usr/bin/env python

import sys

l_caps = ["A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X",
        "Y", "Z"]

l_small = ["a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x",
        "y", "z"]

def decode(letter, key):
    
    p_text = ""

    if letter not in l_caps and letter not in l_small:
        p_text += letter

    elif letter in l_caps:
        i = (l_caps.index(letter) + key) % 26
        p_text += l_caps[i]
    
    else:
        i = (l_small.index(letter) + key) % 26
        p_text += l_small[i]
    
    return p_text


cipher_text = sys.argv[1]
key = sys.argv[2]       # Key by whic letter will shioft forward
plain_text = ""

cipher_text = cipher_text.split() 

for word in cipher_text:
    for i in range(len(word)):
        plain_text += decode(word[i], int(key))
    plain_text += " "

print plain_text

