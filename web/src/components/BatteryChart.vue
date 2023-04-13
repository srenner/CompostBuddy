<script setup>
import { reactive } from 'vue'
import axios from 'axios';
import Chart from 'chart.js/auto';
import annotationPlugin from 'chartjs-plugin-annotation';
import trendlinePlugin from 'chartjs-plugin-trendline';

Chart.register(annotationPlugin);
Chart.register(trendlinePlugin);

const state = reactive({ apiVersion: 'unknown', events: [] });

axios.get('http://localhost:3000/api/event/latest?quantity=60')
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
            label: 'battery',
            data: state.events.map(row => row.vbat),
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            // trendlineLinear: {
            //     style: "rgb(75 ,192 ,192, 0.1)",
            //     lineStyle: "dotted",
            //     width: 1
            // },
        }
        ]
      },

      options: {
        plugins: {
            annotation: {
                drawTime: 'beforeDraw',
                annotations: [
                    {
                        id: 'batteryGreen',
                        type: 'box',
                        yMin: 3.6,
                        backgroundColor: 'rgba(40, 167, 69, 0.25)',
                        borderWidth: 0
                    },
                    {
                        id: 'batteryYellow',
                        type: 'box',
                        yMin: 3.4,
                        yMax: 3.6,
                        backgroundColor: 'rgba(255, 193, 7, 0.25)',
                        borderWidth: 0
                    },
                    {
                        id: 'batteryRed',
                        type: 'box',
                        yMin: 0.0,
                        yMax: 3.4,
                        backgroundColor: 'rgba(220, 53, 69, 0.25)',
                        borderWidth: 0
                    },
                ]
            }
        },
        scales: {
            y: {
                suggestedMax: 4.2,
                suggestedMin: 3.3
            },
            // x: {
            //     ticks: {
            //          callback: function(tick, index, array) {
            //             return tick;
            //              //return (index % 3) ? "" : tick;
            //          }
            //     }
            // }
        }
      },
      
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
