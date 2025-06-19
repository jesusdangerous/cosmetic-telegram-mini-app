<template>
  <button v-if="!href">{{ text }}</button>
  <a v-else :href="href" class="button-link">
    {{ text }}
  </a>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  text: String,
  href: String
})
</script>

<style scoped>
button, .button-link {
  max-width: 100%;
  width: 100%;
  height: 52px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
  border: none;
  background-color: rgba(19, 19, 19, 1);
  border-radius: 12px;
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  color: rgba(251, 251, 251, 1);
  text-decoration: none;
  cursor: pointer;
}

button:disabled, .button-link:disabled {
  background-color: rgba(173, 173, 173, 1);
  border: 1px solid #4A4A4A;
}
</style>
