<script setup>
defineProps({
    title: {
        type: String,
        required: true,
    },
    icon: {
        type: String,
        required: true,
    }
});
</script>

<template>
    <h1>
        <font-awesome-icon :icon="icon" />
        <span class="ms-3">{{ title }}</span>
    </h1>

</template>

<style scoped>

</style>
