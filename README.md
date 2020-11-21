# Programme to generate text

## Overview

This programme is based on an exercise from Allen Downey's [Think Python](https://greenteapress.com/wp/think-python/). It generates text based on Markov Analysis.

The texts generated are based on the assumption that words tend to cluster together i.e. an author will have a particular idiom meaning she will put particular words together more frequently than others. Therefore we can make predictions about which words are likely to follow one another based on probability.

A randomising module in Python is implemented initially to chose a single word used by the author and then to generate subsequent words, based on the probability of one word following another.

## A word on application

The texts I have included here are short descriptions from Amazon on Nvidia GPUs. My reasons for exploring this use case are outlined in my study blog.

Of course you are free to use any text you wish so long as it is a txt or csv file.
