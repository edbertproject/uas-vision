import os
import json
from Methods import read_image_percentage

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabets = ['a', 'b']

dicts = {}
for alphabet in alphabets:
    all_files = os.listdir("alphabets/" + alphabet)

    percentages = []
    for all_file in all_files:
        percentages.append(read_image_percentage("alphabets/" + alphabet + "/" + all_file))

    dicts[alphabet] = percentages

with open('alphabets.json', 'w') as fp:
    json.dump(dicts, fp)