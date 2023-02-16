<script setup>
import { reactive } from 'vue'
import axios from 'axios';

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
    <span>api version</span>
    <span class="tag">{{ state.apiVersion }}</span>
</template>

<style scoped>

</style>
