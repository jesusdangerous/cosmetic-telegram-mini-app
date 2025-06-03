<template>
  <input
  type="text"
  :value="modelValue"
  @input="$emit('update:modelValue', $event.target.value)">
</template>

<script setup>
defineProps(['modelValue'])
defineEmits(['update:modelValue'])
</script>

<style scoped>
input {
  box-sizing: border-box;
  border-radius: 12px;
  height: 44px;
  padding: 5px 20px;
  font-size: 20px;
  outline: none;
  border: none;
}
</style>
