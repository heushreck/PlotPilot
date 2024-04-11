<template>
  <div id="app">
    <header class="header">
      <h2>Welcome to Plot Pilot</h2>
    </header>
    <main class="content">
      <h3>Create Graphs for your data in seconds.</h3>
      <p>Tell us what you want to say with this graph, then highlight the data and press the generate button.</p>
      <textarea v-model="intention" class="input" placeholder="Enter What chart should say" />
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


  const available_data_types = ["Line", "Doughnut", "ColumnClustered", "Waterfall", "XYScatter"]
  const chart_data = {
    chartType : available_data_types[1],
    title : 'Sales Data',
    
  }

  const createChart = async() => {
    window.Excel.run(async context => {
      const range = context.workbook.getSelectedRange();
      range.load("values");
      await context.sync();
      // Call the API that gives us the chart data
      // convert the range to a JSON object
      console.log(range.values);
      console.log(intention.value);
      // ...
      // Create the chart in Excel
      const sheet = context.workbook.worksheets.getActiveWorksheet();
      const chart = sheet.charts.add(chart_data["chartType"], range, "Auto");
      chart.title.text = chart_data["title"];
      chart.legend.format.fill.setSolidColor("white");
      chart.dataLabels.format.font.size = 15;
      chart.dataLabels.format.font.color = "black";
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
