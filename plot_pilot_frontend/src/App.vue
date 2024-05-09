<template>
  <div id="app">
    <header class="header">
      <h2>Welcome to Plot Pilot</h2>
    </header>
    <main class="content">
      <h3>Create Graphs for your data in seconds.</h3>
      <p>Tell us what you want to say with this graph, then highlight the data and press the generate button.</p>
      <textarea v-model="intention" class="input" placeholder="What should the chart say about your data?" />
      <button class="button" @click="createChart">
        <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
          <path fill-rule="evenodd" d="M20.599 1.5c-.376 0-.743.111-1.055.32l-5.08 3.385a18.747 18.747 0 0 0-3.471 2.987 10.04 10.04 0 0 1 4.815 4.815 18.748 18.748 0 0 0 2.987-3.472l3.386-5.079A1.902 1.902 0 0 0 20.599 1.5Zm-8.3 14.025a18.76 18.76 0 0 0 1.896-1.207 8.026 8.026 0 0 0-4.513-4.513A18.75 18.75 0 0 0 8.475 11.7l-.278.5a5.26 5.26 0 0 1 3.601 3.602l.502-.278ZM6.75 13.5A3.75 3.75 0 0 0 3 17.25a1.5 1.5 0 0 1-1.601 1.497.75.75 0 0 0-.7 1.123 5.25 5.25 0 0 0 9.8-2.62 3.75 3.75 0 0 0-3.75-3.75Z" clip-rule="evenodd" />
        </svg>
        <div>Generate Graph</div>
      </button>
    </main>
  </div>
</template>


<script setup>
import { ref } from 'vue';
const teaGreen = ref('rgba(196, 241, 190, 1)');
const paynesGray = ref('rgba(82, 91, 118, 1)');
const spaceCadet = ref('rgba(32, 30, 80, 1)');
const intention = ref('');

let chartData = {
  chart_type : "Line",
  title : 'Sales Data',
  x_axis_label : 'Month',
  y_axis_label : 'Sales',
  has_trendline : true,
}

const fetchData = async (data) => {
  const requestParams = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ intention: intention.value, data: data}),
  };
  await fetch('http://localhost:8000/graph-data', requestParams)
  .then(response => response.json())
  .then(data => chartData = data);
}

const createChart = async() => {
  window.Excel.run(async context => {
    const range = context.workbook.getSelectedRange();

    
    range.load("valuesAsJsonLocal");
    await context.sync();
    const data_input = range.valuesAsJsonLocal.map(item => item.map(subItem => subItem.basicValue));
    await fetchData(data_input);


    const sheet = context.workbook.worksheets.getActiveWorksheet();
    const chart = sheet.charts.add(chartData.chart_type, range, "Auto");
    chart.title.text = chartData["title"];
    chart.legend.format.fill.setSolidColor("white");
    chart.dataLabels.format.font.size = 15;
    chart.dataLabels.format.font.color = "black";
    switch (chartData.chart_type) {
      case "Line":
        chart.axes.valueAxis.title.text = chartData["y_axis_label"];
        chart.axes.categoryAxis.title.text = chartData["x_axis_label"];
        if (chartData.has_trendline) {
          let seriesCollection = chart.series;
          seriesCollection.getItemAt(0).trendlines.add("Linear");
        }
        break;
    }
    await context.sync();
  });
};
</script>

<style>

html, body {
  background-color: rgba(162, 195, 164, 1);
}

.header {
  background-color: v-bind("spaceCadet");
  color: v-bind("teaGreen");
  text-align: center;
  padding: 10px;
  font-size: 20px;
}

.content {
  padding: 20px;
  color: v-bind("spaceCadet");
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
}

.button {
  background-color: v-bind("paynesGray");
  color: v-bind("teaGreen");
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
  display: inline-flex;
  align-items: center;
  border-radius: 10px;
}

.icon {
  margin-right: 10px;
  width: 24px;
  height: 24px;
}

.input {
  border-radius: 5px;
  padding: 5px;
}
</style>
