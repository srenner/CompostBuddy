<script setup>
import { reactive } from 'vue'
import axios from 'axios';
import Chart from 'chart.js/auto';
import annotationPlugin from 'chartjs-plugin-annotation';

Chart.register(annotationPlugin);

const state = reactive({ apiVersion: 'unknown', events: [] });

axios.get('http://localhost:3000/api/event/latest?quantity=60')
  .then(function (response) {
    state.events = response.data.slice(-60);

    new Chart(
    document.getElementById('activityChart'),
    {
      type: 'line',
      data: {
        labels: state.events.map(row => row.timestamp),
        datasets: [
        {
          label: 'temp1',
          data: state.events.map(row => Math.round(row.temp1 * 10.0) / 10.0)
        },
        {
          label: 'temp2',
          data: state.events.map(row => Math.round(row.temp2 * 10.0) / 10.0)
        },
        ]
      },
      options: {
        plugins: {
            annotation: {
                drawTime: 'beforeDraw',
                annotations: [
                    {
                        id: 'idealRange',
                        type: 'box',
                        yMin: 55,
                        yMax: 72,
                        backgroundColor: 'rgba(40, 167, 69, 0.25)',
                        borderWidth: 0
                    },
                    {
                        id: 'heatTarget',
                        type: 'box',
                        yMin: 65,
                        yMax: 72,
                        backgroundColor: 'rgba(40, 167, 69, 0.25)',
                        borderWidth: 0
                    },
                    
                ]
            }
        },
        scales: {
            y: {
                max: 75,
                suggestedMin: 20
            }
        }
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
    <div style="width: 800px;"><canvas id="activityChart"></canvas></div>
</template>

<style scoped>

</style>
