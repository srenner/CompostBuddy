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
    <div>
        <span class="badge text-bg-primary ms-1 me-1">{{ state.apiVersion }}</span>
    </div>
    
</template>

<style scoped>

</style>
