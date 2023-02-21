<script setup>
import { reactive } from 'vue'
import axios from 'axios';
import Chart from 'chart.js/auto';

const state = reactive({ apiVersion: 'unknown', events: [] });

const minutesInDay = 1440; // should be pretty close to records per day

axios.get('http://localhost:3000/api/events?start=2023-02-16&end=2023-02-18')
  .then(function (response) {
    state.events = response.data;


    new Chart(
    document.getElementById('activity1'),
    {
      type: 'line',
      data: {
        labels: state.events.map(row => row.timestamp),
        datasets: [
        {
          label: 'temp1',
          data: state.events.map(row => row.bin1.temp)
        },
        {
          label: 'temp2',
          data: state.events.map(row => row.bin2.temp)
        },
        {
          label: 'batt',
          data: state.events.map(row => row.batt)
        }
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
    <div>chart goes here</div>
    <div style="width: 800px;"><canvas id="activity1"></canvas></div>
    <div class="d-none">{{ state.events }}</div>
</template>

<style scoped>

</style>
