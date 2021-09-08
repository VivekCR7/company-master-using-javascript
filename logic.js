//Collect the json data using fetch api and plot the graph

// Histogram

function get_the_json_data_for_histogram() {
  fetch("./json_data/histogram.json")
    .then((data) => data.json())
    .then(histogram);
}

get_the_json_data_for_histogram();

function histogram(data) {
  const dic = {};
  for (d of data) {
    if (!(d in dic)) {
      dic[d] = 1;
    } else {
      dic[d] += 1;
    }
  }

  const arr = [];

  for (key in dic) {
    arr.push(dic[key]);
  }

  Highcharts.chart("histogram", {
    chart: {
      type: "column",
    },
    title: {
      text: "Histogram of Authorized Cap",
    },
    xAxis: {
      categories: ["<=1L", "1L to 10L", "10L to 1Cr", "1Cr to 10Cr", ">10Cr"],
      crosshair: true,
    },
    yAxis: {
      min: 0,
      title: {
        text: "No. of Companies",
      },
    },
    plotOptions: {
      column: {
        pointPadding: 0,
        borderWidth: 0,
        groupPadding: 0,
        shadow: false,
      },
    },
    series: [
      {
        name: "Authorized Cap",
        data: arr,
      },
    ],
  });
}

// Barplot

function get_the_json_data_for_barplot() {
  fetch("./json_data/barplot.json")
    .then((data) => data.json())
    .then(barplot);
}

get_the_json_data_for_barplot();

function barplot(data) {
  const arr = [];
  for (let year in data) {
    arr.push([year, data[year]]);
  }

  Highcharts.chart("barplot", {
    chart: {
      type: "column",
    },
    title: {
      text: "Number of Company registration vs Years",
    },
    xAxis: {
      type: "category",
    },
    yAxis: {
      min: 0,
      title: {
        text: "No. of companies",
      },
    },
    series: [
      {
        name: "Years",
        data: arr,
      },
    ],
  });
}

// Barchart for the year 2015

function get_the_json_data_for_barchart_2015() {
  fetch("./json_data/bar_chart_2015.json")
    .then((data) => data.json())
    .then(bar_chart_2015);
}

get_the_json_data_for_barchart_2015();

function bar_chart_2015(data) {
  const arr = [];
  for (let city in data) {
    arr.push([city, data[city]]);
  }

  Highcharts.chart("barchart_2015", {
    chart: {
      type: "column",
    },
    title: {
      text: "Number of Company registration vs Years",
    },
    xAxis: {
      type: "category",
      labels: {
        rotation: -90,
      },
    },
    yAxis: {
      min: 0,
      title: {
        text: "No. of companies",
      },
    },
    series: [
      {
        name: "districts",
        data: arr,
      },
    ],
  });
}

// Grouped plot

function get_the_json_data_for_grouped_plot() {
  fetch("./json_data/grouped_barplot.json")
    .then((data) => data.json())
    .then(grouped_barplot);
}

get_the_json_data_for_grouped_plot();

function grouped_barplot(data) {
  const other_arr = [];
  const manufacture_arr = [];
  for (key in data) {
    other_arr.push(data[key]["Other"]);
    manufacture_arr.push(data[key]["Manufacture"]);
  }

  Highcharts.chart("grouped_plot", {
    chart: {
      type: "column",
    },
    title: {
      text: "Grouped plot",
    },

    xAxis: {
      categories: [
        "2000",
        "2001",
        "2002",
        "2003",
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
        "2018",
        "2019",
        "2020",
        "2021",
      ],
      labels: {
        rotation: -45,
      },
    },
    yAxis: {
      min: 0,
      title: {
        text: "no. of companies",
      },
    },

    plotOptions: {
      column: {
        pointPadding: 0,
        borderWidth: 0,
      },
    },
    series: [
      {
        name: "Other",
        data: other_arr,
      },
      {
        name: "Manufacture",
        data: manufacture_arr,
      },
    ],
  });
}
