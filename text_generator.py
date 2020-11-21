# Input a txt or CSV containing text and this programme will
# generate a new text based on Markov Analysis

from __future__ import print_function, division
 
import string
import bisect
import random
import sys

class markov_prediction:

    def __init__(self):
            self.suffixes = {} 
            self.prefix = ()

    def prep_file(self, text, order = 2):
    # This function accepts the txt or CSV file you wish to 
    # generate new texts from. Order refers to the number 
    # of words the programme will use to base its prediction on

    # The purpose of this function is to prepare the text i.e.
    # remove supperflious punction and spacing so that the 
    # programme creates tuples of words rather than tuples
    # of punctuation or text and punctuation

        res = open(text)

        for line in res:
            for word in line.rstrip().split():
                self.prep_words(word, order)

    def prep_words(self, word, order = 2):
    # This function goes through the prepared text word by word
    # to generate tuples of the size specified in order
    # This is achived first by first adding the word as a 
    # prefix to the tuple and shifting the text by one word and
    # adding subsequent words to the tuple until it equals the 
    # size specified in order.

    # Once this is achieved the word is added to the suffix dict
    # with the word being a key and suffix its value.

        if len(self.prefix) < order:
            self.prefix += (word,)
            return
            
        try:
            self.suffixes[self.prefix].append(word)
            
        except KeyError:
            self.suffixes[self.prefix] = [word]

        self.prefix = shift(self.prefix, word)               

    def make_text(self, n = 100):
    # This function will generate a random text. It dose this
    # by first choosing a random word in the text.

    # The programme then iterates n times i.e. the number of 
    # words desired in the final text. In this process the
    # programme is called recursively adding suffixes until
    # n is zero at which point the text is printed

        start = random.choice(list(self.suffixes.keys()))

        for i in range(n):
            suffixes_item = self.suffixes.get(start, None)
            if suffixes_item == None:
                self.make_text(n-1)
                return

            word = random.choice(suffixes_item)
            print(word, end=' ')
            start = shift(start, word)

def shift(t, word): 
    # generates new tuple by removing top word and moving
    # it to back

    return t[1:] + (word,)
    
    
def main(script, filename='gpu_texts.csv', n=100, order=2):
        
    try: 
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
        
    else:
        markov = markov_prediction()
        markov.prep_file(filename,order)
        markov.make_text(n)

if __name__ == '__main__':
    main(*sys.argv)