<!-- components/SortModal.vue -->
<template>
  <div class="sorting-container">
    <h1>Показать сначала</h1>
    <ul>
      <li
        v-for="option in sortOptions"
        :key="option.value"
        @click="selectOption(option.value)"
        :class="{ active: selectedOption === option.value }"
      >
        {{ option.label }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['sort-changed'])

const selectedOption = ref('new')
const sortOptions = [
  { value: 'new', label: 'Новые' },
  { value: 'old', label: 'Старые' },
  { value: 'high-rated', label: 'С высокой оценкой' },
  { value: 'low-rated', label: 'С низкой оценкой' }
]

const selectOption = (option) => {
  selectedOption.value = option
  emit('sort-changed', option)
}
</script>

<style scoped>
.sorting-container {
  background-color: white;
  border-radius: 12px;
  padding: 24px;
  max-width: 320px;
  width: 100%;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
li {
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
}
li:hover {
  background-color: #f5f5f5;
}
li.active {
  background-color: #e0e0e0;
  font-weight: bold;
}
</style>
