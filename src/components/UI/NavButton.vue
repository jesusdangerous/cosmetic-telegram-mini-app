<template>
  <button>{{ text }}</button>
</template>

<script setup>
  import { defineProps } from 'vue';
  defineProps({
    text: String,
  })
</script>

<style scoped>
  button {
    border: none;
    background-color: transparent;
    font-size: 16px;
    padding: 0;
  }
</style>
