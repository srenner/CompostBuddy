<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
  <header class="container">
    <div class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-light text-decoration-none">
        <font-awesome-icon icon="fa-solid fa-recycle" class="fa-xl me-2"  />
        <span class="fs-4">CompostBuddy</span>
      </a>

      <ul class="nav nav-pills">
        <!-- <li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Active Example</a></li> -->
        <li class="nav-item"><RouterLink class="nav-link" to="/"><font-awesome-icon icon="fa-solid fa-line-chart" class="fa-xl" /></RouterLink></li>
        <li class="nav-item"><RouterLink class="nav-link" to="/config"><font-awesome-icon icon="fa-solid fa-gears" class="fa-xl" /></RouterLink></li>
      </ul>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
