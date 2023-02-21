<script setup>
//import { reactive } from 'vue'

defineProps({
  measurement: {},
});


</script>

<template>

  {{ measurement }}


  <div class="small">
    <div class="alert alert-info" role="alert" v-for="info in measurement.info">
      {{ info }}
    </div>
    <div class="alert alert-warning" role="alert" v-for="warning in measurement.warnings">
      {{ warning }}
    </div>
    <div class="alert alert-danger" role="alert" v-for="error in measurement.errors">
      {{ error }}
    </div>
  </div>
    
</template>

<style scoped>

</style>
