import json

from Methods import read_image_percentage


def get_max_percentage(percentages):
    temp_max = {
        'alphabet': '',
        'value': 0
    }
    for percentage in percentages:
        if percentage['value'] > temp_max['value']:
            temp_max = percentage
    return temp_max['alphabet'], temp_max['value']

def compare_percentage(image_path):
    percentage = read_image_percentage(image_path)
    input_sum = sum(percentage)

    with open('alphabets.json', 'r') as f:
        alphabets = json.load(f)

    percents = []
    for alphabet in alphabets:

        percent = []
        for image in alphabets[alphabet]:
            master_sum = sum(image)
            dev = master_sum - input_sum
            percent.append(round(((master_sum - abs(dev)) / master_sum) * 100))

        percents.append({
            "alphabet": alphabet,
            "value": max(percent),
        })

    max_alphabet, max_percentage = get_max_percentage(percents)

    return max_alphabet, max_percentage, percents
