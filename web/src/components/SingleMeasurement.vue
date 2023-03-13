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
  
  <div>
    Measurement taken at {{ state.measurement.timestamp }}
  </div>

  <div class="row">
    <div class="col-md-auto">
      <dl>
        <dt>Battery Voltage</dt>  
        <dd>{{ state.measurement.vbat }}</dd>

        <dt>Power Active</dt>
        <dd> {{ state.measurement.power }} </dd>

        <dt>Charging</dt>
        <dd>{{ state.measurement.charging }}</dd>
      </dl>
    </div>
    <div class="col-md-auto">
      <dl>
        <dt>Temperature 1</dt>
        <dd>{{ state.measurement.temp1 }}</dd>

        <dt>Temperature 2</dt>
        <dd>{{ state.measurement.temp2 }}</dd>

        <dt>Last Turn</dt>
        <dd>{{ state.measurement.last_turn || 'unknown' }}</dd>
      </dl>
    </div>
    <div class="col">
      <div class="alert alert-danger" role="alert" v-for="error in state.measurement.errors">
        {{ error }}
      </div>
      <!--uncomment to view example of error message format-->
      <div class="d-none">
        <div class="alert alert-danger" role="alert" >
          Repeated socket errors
        </div>
        <div class="alert alert-danger" role="alert" >
          Network Error 6
        </div>
      </div>
    </div>
  </div>
  
</template>


<style scoped>

</style>
