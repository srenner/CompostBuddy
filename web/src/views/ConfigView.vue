<script setup>
import ViewHeader from "../components/ViewHeader.vue";
import ApiInfo from "../components/ApiInfo.vue";
import Shutdown from "../components/Shutdown.vue";
</script>

<template>
  <main class="container">    
    <ViewHeader title="Configuration" icon="fa-solid fa-gears" />

    <div class="mb-4">
        <ApiInfo />
    </div>
    <div class="mb-4">
        <Shutdown />
    </div>

    
    

  </main>
</template>
