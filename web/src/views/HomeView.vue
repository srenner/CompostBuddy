<script setup>
import PageHeader from "../components/PageHeader.vue";
import ActivityChart from "../components/ActivityChart.vue";
import MessageCenter from "../components/MessageCenter.vue";
import SingleMeasurement from "../components/SingleMeasurement.vue";
import BatteryChart from "../components/BatteryChart.vue";

</script>

<template>
  <main class="container">
    <PageHeader title="Activity" icon="fa-solid fa-chart-line" />
    <ActivityChart />
    <BatteryChart />
    <SingleMeasurement />
    <!-- <MessageCenter /> -->
  </main>
</template>
