"""
    Print "Fan-Far-Naque" occurrences in order
"""

import sys
import json


print("'Fan-Far-Naque' occurrences in order.json")

with open('order.json') as f:
    data = json.load(f)
    order = data["order"]

sample = ["i", "v", "x"] # words are roman based
current_index = 0

for word, number in order:
    if(word == sample[current_index]):
        # the word is expected, go to next one
        current_index+=1
        if(current_index==len(sample)):
            # we just reached last word, print it and start again
            print(number)
            current_index=0
    else:
        # the word isn't expected, start again
        current_index=0
