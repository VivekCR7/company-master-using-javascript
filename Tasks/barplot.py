# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

"""
Approach:

For this task we just need to plot the bar plot of the company
registrations vs year so, I just created a function get_the_dictionary(),
and iterate over my dataset and retrieved the no.of company registered
respective to the year, where year is key and the count is the values
eg: {"year":count"}

after getting the dictionary I created one more function for plotting
graph in which I used matplotlib's plt.bar() to plot the bar plot.

"""

import json
from transform import get

dataset = get()


def get_the_dictionary(data):
    registration_dictionary = {}
    for ele in data:
        date = int(ele['DATE_OF_REGISTRATION'][0:4])
        if date not in registration_dictionary:
            registration_dictionary[date] = 1
        else:
            registration_dictionary[date] += 1

    return registration_dictionary


output = get_the_dictionary(dataset)

with open('../json_data/barplot.json', 'w') as f:
    json.dump(output, f, indent=2)
