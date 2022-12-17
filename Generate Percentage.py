import os
import json
from Methods import read_image_percentage

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dicts = {}
for number in numbers:
    all_files = os.listdir("numbers/" + number)

    percentages = []
    for all_file in all_files:
        percentages.append(read_image_percentage("numbers/" + number + "/" + all_file))

    dicts[number] = percentages

with open('numbers.json', 'w') as fp:
    json.dump(dicts, fp)