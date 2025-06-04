<!-- Input.vue -->
<template>
  <input
    type="text"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
    :style="inputStyle"
  />
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: String,
  inputStyle: Object // принимаем стиль
})

const emit = defineEmits(['update:modelValue'])
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
  width: 100%; /* чтобы стиль ширины работал корректно */
}
</style>
