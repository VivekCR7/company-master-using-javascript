# Company Master

This project is more of a data project, data visualization. The main aim of the project is
to convert the raw open data plots, that tells a story on the state of Company registration.
One important thing in this project is, there is no use of built-in libraries for transforming
the data, libraries like pandas are not used in this project. We are going to write code for generating
data for plots then store it as a json file. we going to use that json data to display  plotting on website with the
help of [highcharts](https://www.highcharts.com/).



## Dataset

raw data which is .csv file, it's the real world data of company registration in the state of maharashtra.
below is the link you can download the data from there.

Two dataset has been used for this project:

| Dataset | Link |
| --- | --- |
| Company Master data of Maharashtra | https://tinyurl.com/3453m26x |
| District vs zip data | https://tinyurl.com/39tauusa |



## Run Locally

Clone the project

```bash
git clone git@gitlab.com:mountblue/cohort-17-python/vivek-dubey/company-master-javascript-version.git
```

Go to the project directory

```bash
~ cd company-master-javascript-version
```

Make a directory dataset and then move the downloaded data in that directory using terminal or from gui.

```bash
~ mkdir dataset
~ mv downloads/Maharashtra.csv ./dataset/
~ mv downloads/district_zip.csv ./dataset/
```

to run your program Locally type below command

```bash
~ python3 -m http.server
```
the default port is `8000` so open the browser then type `localhost:8000`.


### Official Website Link

* [Official website](https://company-master-vivek.herokuapp.com/)

## Authors

- [@Vivek Dubey]()



