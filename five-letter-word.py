#!/usr/bin/env python3

from optparse import OptionParser
from random import randint
from typing import List

def get_five_letter_words(fn: str) -> List[str]:
    try:
        words = open(fn, "r")
        return [w.strip() for w in words.readlines() if len(w) == 5+1] 
    except:
        return []

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-r', '--random', action='store_true', dest='show_random', default=False)
    parser.add_option('-f', '--file', dest='fnm_word_list', default='./word.list')
    parser.parse_args()
    options, args = parser.parse_args()

    words = get_five_letter_words(options.fnm_word_list)
    if options.show_random:
        len_words = len(words)
        print(words[randint(1, len(words))])
    else:
        for w in words:
            print(w)
        
