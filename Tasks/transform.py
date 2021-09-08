# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

"""
Approach:

I read the csv file with the help of DictReader from python csv library.
Intially the data contains of around 4 lakhs rows which was a lot. so I
tried to shortened my data and considered only last 21 years of data
from 2000 to 2021.

So, I just iterate over the my DictReader and look for the year.
if year was between 2000 to 2001 then I appended that row in my
list of dictionary.
"""

from csv import DictReader


def get():
    updated_dataset = []
    with open('../dataset/Maharashtra.csv',
              'r', encoding='utf-8') as csv_file:
        dataset = DictReader(csv_file)

        for data in dataset:
            if data['DATE_OF_REGISTRATION'] == 'NA':
                continue

            if 2000 <= int(data['DATE_OF_REGISTRATION'][0:4]) <= 2021:
                updated_dataset.append(data)
            else:
                continue

    return updated_dataset
