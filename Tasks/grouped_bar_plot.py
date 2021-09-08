# # pylint: disable=missing-function-docstring
# # pylint: disable=missing-module-docstring
"""
Approach:

For this task we needed to group plot the aggregating registered
counts over year and principal activities for that I first counted
the companies registration from year and from principal activity but
for grouping them the array was uneven.

so, I created a function to combined the counts of companies and
the principal activity that is by creating a dictionary of dictionary
with keys as years and the values as a dictionary with total counts and
the principal activity counts respective to that year.

for eg: {'year': {'Total':count,'principal_activity_1':count,
        'principal_activity_2':count}}
and so on for rest of the years.

but the principal_activities were repeating so I manually selected
Total,Other,Manufacture,Construciton as the constant dictionaries keys
for every year.

with the help of the grouped_bar_plot() function I plotted the graph for
[other,manufacture] group to look clean, we can add other parameters
and group them as well.

"""
import json
from transform import get

dataset = get()


def get_the_combined_dictionary(arr):
    dictionary = {}

    for ele in arr:
        year = int(ele['DATE_OF_REGISTRATION'][0:4])
        principal = ele['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']

        extracted_manufacturer_from_principal = principal[:11]
        extracted_construction_from_principal = principal[:12]

        if year not in dictionary:
            dictionary[year] = {'Total': 0, 'Other': 0,
                                'Manufacture': 0, 'Construction': 0}

        if extracted_manufacturer_from_principal in dictionary[year]:
            dictionary[year][extracted_manufacturer_from_principal] += 1
        elif extracted_construction_from_principal in dictionary[year]:
            dictionary[year][extracted_construction_from_principal] += 1
        else:
            dictionary[year]['Other'] += 1

        dictionary[year]['Total'] += 1

    return dictionary


output = get_the_combined_dictionary(dataset)

with open('../json_data/grouped_barplot.json', 'w') as f:
    json.dump(output, f, indent=2)
