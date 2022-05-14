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

def is_exit_ignore_letter(word: str, ignore_letters: List[str]) -> bool:
     return len([l for l in list(word) if l in ignore_letters]) > 0

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-r', '--random', action='store_true', dest='show_random', default=False)
    parser.add_option('-f', '--file', dest='fnm_word_list', default='./word.list')
    parser.add_option('-i', '--ignore', dest='ignore_letters', default='')
    parser.parse_args()
    options, args = parser.parse_args()

    ignore_letters = [l for l in options.ignore_letters.split(',') if l != '']

    words = get_five_letter_words(options.fnm_word_list)
    if len(words) > 0 and len(ignore_letters) > 0:
        words = [w for w in words if not is_exit_ignore_letter(w, ignore_letters)]
    if options.show_random:
        print(words[randint(1, len(words))])
    else:
        for w in words:
            print(w)
        
