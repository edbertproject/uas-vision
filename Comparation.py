import json

from Methods import read_image_percentage


def get_max_percentage(percentages):
    temp_max = {
        'number': '',
        'value': 0
    }
    for percentage in percentages:
        if percentage['value'] > temp_max['value']:
            temp_max = percentage
    return temp_max['number'], temp_max['value']

def compare_percentage(image_path):
    percentage = read_image_percentage(image_path)
    input_sum = sum(percentage)

    with open('numbers.json', 'r') as f:
        numbers = json.load(f)

    percents = []
    for number in numbers:

        percent = []
        for image in numbers[number]:
            master_sum = sum(image)
            dev = master_sum - input_sum
            percent.append(round(((master_sum - abs(dev)) / master_sum) * 100))

        percents.append({
            "number": number,
            "value": max(percent),
        })

    print(percents)

    max_number, max_percentage = get_max_percentage(percents)

    return max_number, max_percentage, percents
