<script setup>
import { reactive } from 'vue'
import axios from 'axios';

</script>

<template>
    <span>shut down device</span>
    <button class="btn btn-sm btn-link btn-danger ms-1"><font-awesome-icon icon="fa-solid fa-power-off" class="fa-xl" /></button>
    <span class="small d-none">sent shutdown command</span>
</template>

<style scoped>

</style>
