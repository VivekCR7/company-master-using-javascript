# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

"""
Approach:

we needed to plot the Histogram of authorized cap, histogram is plotted based
on frequency and according to the question there were groups of the authorized
cap that is bins = [<=1L, 1L to 10L, 10L to 1Cr, 1Cr to 10Cr, >10Cr]

So, I planned to group the amount according to bins condition. I created helper
function in which I generated list of groups no. that is:
<=1L --> 1
1l to 10L --> 2
10L to 1Cr --> 3
1Cr to 10Cr --> 4
>10Cr --> 5

so my dataset looked like this: [1,1,1,2,2,2,2,2,2,3,3,3,4,4,4,5]
the occurence of the group no. is the frequency that this amount of time there
is a price of this price group.

Then I created one more function for plotting histogram. In which I used
matplotlib's plt.hist() function to plot histogram.


"""
import json
from transform import get

# get() function imported from transform.py file to get the dataset
dataset = get()


def get_the_grouped_data(arr):
    grouped_list = []

    for ele in arr:
        price = int(float(ele['AUTHORIZED_CAP']))
        # break
        if price <= 100000:
            grouped_list.append(1)
        elif 100000 <= price <= 1000000:
            grouped_list.append(2)
        elif 1000000 <= price <= 10000000:
            grouped_list.append(3)
        elif 10000000 <= price <= 100000000:
            grouped_list.append(4)
        elif price >= 100000000:
            grouped_list.append(5)

    return grouped_list


output = get_the_grouped_data(dataset)

with open('../json_data/histogram.json', 'w') as f:
    json.dump(output, f)
