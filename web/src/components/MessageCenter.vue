<script setup>
import { reactive } from 'vue'
import axios from 'axios';

const state = reactive({ 
    info: [],
    warnings: [],
    errors: []
});

axios.get('http://localhost:3000/api/compost/latest')
  .then(function (response) {
    state.info = response.data.info;
    state.warnings = response.data.warnings;
    state.errors = response.data.errors;
  })
  .catch(function (error) {
    console.log(error);
  })
  .finally(function () {
    // 
  });
</script>

<template>
    <div class="small">
      <div class="alert alert-info" role="alert" v-for="info in state.info">
        {{ info }}
      </div>

      <div class="alert alert-warning" role="alert" v-for="warning in state.warnings">
        {{ warning }}
      </div>

      <div class="alert alert-danger" role="alert" v-for="error in state.errors">
        {{ error }}
      </div>
    </div>
    
</template>

<style scoped>

</style>
