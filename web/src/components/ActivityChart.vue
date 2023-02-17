<script setup>
import { reactive } from 'vue'
import axios from 'axios';
import Chart from 'chart.js/auto';

const state = reactive({ apiVersion: 'unknown' })

axios.get('http://localhost:3000/api/version')
  .then(function (response) {
    state.apiVersion = response.data;
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
    <div style="width: 800px;"><canvas id="activity"></canvas></div>
</template>

<style scoped>

</style>
