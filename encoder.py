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

def encode(letter, key):
    
    c_text = ""

    if letter not in l_caps and letter not in l_small:
        c_text += letter

    elif letter in l_caps:
        i = (l_caps.index(letter) - key) % 26
        c_text += l_caps[i]
    
    else:
        i = (l_small.index(letter) - key) % 26
        c_text += l_small[i]
    
    return c_text


plain_text = sys.argv[1]
key = sys.argv[2]       # Key by which letter will shift backward
cipher_text = ""

plain_text = plain_text.split() 

for word in plain_text:
    for i in range(len(word)):
        cipher_text += encode(word[i], int(key))
    cipher_text += " "

print cipher_text

