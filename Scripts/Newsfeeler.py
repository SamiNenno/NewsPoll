import os
import pandas as pd

baerbock_sentences = []
with open("baerbock_sentences.txt") as file:
    for line in file:
        baerbock_sentences.append(line.rstrip())

print(baerbock_sentences[0])
