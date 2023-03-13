<script setup>
import { reactive } from 'vue'
import axios from 'axios';
import Chart from 'chart.js/auto';

const state = reactive({ apiVersion: 'unknown', events: [] });

axios.get('http://localhost:3000/api/events?start=2023-03-08&end=2023-03-18')
  .then(function (response) {
    state.events = response.data.slice(-60);

    new Chart(
    document.getElementById('batteryChart'),
    {
      type: 'line',
      data: {
        labels: state.events.map(row => row.timestamp),
        datasets: [
        {
          label: 'batt',
          data: state.events.map(row => row.vbat)
        }
        // {
        //   label: 'batt',
        //   data: state.events.map(row => row.vbat)
        // }
        ]
      }
    });

  })
  .catch(function (error) {
    console.log(error);
  })
  .finally(function () {
    // 
  });

  
</script>

<template>
    <div style="width: 800px;"><canvas id="batteryChart"></canvas></div>
    <div class="d-none">{{ state.events }}</div>
</template>

<style scoped>

</style>
