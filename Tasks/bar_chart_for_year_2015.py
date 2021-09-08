# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

"""
Approach:

For this task we need to plot the bar plot for the number of registration
vs district.

So, first I manually created the zipcode vs district .csv file, then created
a function in which I converted that .csv file into a simple dictionary with
the pincode as keys and its corresponding district as values
eg: {'pincode': 'district'}

then I created one more helper funciton to short my large data cause we only
need to work for the year 2015. I just iterated over my list of dictionary
and created a dictionary for counting and looked for the year=2015 and the
address pincode and counted the matching district.
eg: {'district_for_year_2015': count}

then I used one more function to plot the barplot using the
"""
from csv import DictReader as d
import json
from transform import get

dataset = get()


def get_zip_district_dic():
    zip_district_arr = []
    with open('../dataset/district_zip.csv',
              'r', encoding="UTF-8") as csv_file:
        csv_reader = d(csv_file)
        for data in csv_reader:
            zip_district_arr.append(data)

    zip_district_dictionary = {}

    for data in zip_district_arr:
        if data['Pin Code'] not in zip_district_dictionary:
            zip_district_dictionary[data['Pin Code']] = data['District']

    return zip_district_dictionary


# get_zip_distric_dic()

def get_the_district_count(arr):
    zip_district = get_zip_district_dic()

    district_count = {}
    for data in arr:
        if int(data['DATE_OF_REGISTRATION'][0:4]) != 2015:
            continue

        address = data['Registered_Office_Address']
        zipcode = address[len(address)-6:]

        if zipcode in zip_district:
            if zip_district[zipcode] not in district_count:
                district_count[zip_district[zipcode]] = 1
            else:
                district_count[zip_district[zipcode]] += 1

    return district_count


output = get_the_district_count(dataset)

with open('../json_data/bar_chart_2015.json', 'w') as f:
    json.dump(output, f, indent=2)
