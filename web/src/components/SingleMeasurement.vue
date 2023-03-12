<script setup>
import { reactive } from 'vue';
import axios from 'axios';

// defineProps({
//   measurement: {},
// });

const state = reactive({ measurement: {} });

axios.get('http://localhost:3000/api/event/latest')
  .then(function (response) {
    state.measurement = response.data;
  })
  .catch(function (error) {
    console.log(error);
  })
  .finally(function () {
    // 
  });

</script>

<template>

  <div class="d-none">
    {{ state.measurement }}
  </div>
  

  <h3 class="d-none">Power Status</h3>
  <dl>
    <dt>Battery Voltage</dt>  
    <dd>{{ state.measurement.vbat }}</dd>

    <dt>Power Active</dt>
    <dd> {{ state.measurement.power }} </dd>

    <dt>Charging</dt>
    <dd>{{ state.measurement.charging }}</dd>
  </dl>

  <dl>
    <dt>Temperature 1</dt>
    <dd>{{ state.measurement.temp1 }}</dd>

    <dt>Temperature 2</dt>
    <dd>{{ state.measurement.temp2 }}</dd>

    <dt>Last Turn</dt>
    <dd>{{ state.measurement.last_turn || 'unknown' }}</dd>
  </dl>


  <div class="small">
    <div class="alert alert-danger" role="alert" v-for="error in state.measurement.errors">
      {{ error }}
    </div>
  </div>
    
</template>

<style scoped>

</style>
