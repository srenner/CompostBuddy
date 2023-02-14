<script setup>
import TheWelcome from "../components/TheWelcome.vue";
import HelloWorld from "../components/HelloWorld.vue";
</script>

<template>
  <main class="container">
    <TheWelcome />
    <HelloWorld msg="Hello World" />
    <div>This page is like a home</div>
    <div>Look at these icons</div>
    <font-awesome-icon icon="fa-solid fa-recycle" class="fa-xl"  />
    <font-awesome-icon icon="fa-solid fa-gears" class="fa-xl"  />
    <font-awesome-icon icon="fa-solid fa-house" class="fa-xl"  />
    <font-awesome-icon icon="fa-solid fa-chart-line" class="fa-xl"  />
    <font-awesome-icon icon="fa-solid fa-signal" class="fa-xl"  />
  </main>
</template>
