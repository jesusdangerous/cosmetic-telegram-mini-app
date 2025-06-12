<template>
  <div class="category-selector">
    <button
      v-for="category in categories"
      :key="category.name"
      :class="['category-btn', { active: category.name === selected }]"
      @click="selectCategory(category.name)"
    >
      <img :src="category.img" :alt="category.alt" />
      <span>{{ category.name }}</span>
    </button>
  </div>
</template>

<script setup>
import { ref, watch, defineProps, defineEmits } from 'vue'

const props = defineProps({
  categories: {
    type: Array,
    required: true,
  },
  modelValue: {
    type: String,
    default: null,
  },
})

const emit = defineEmits(['update:modelValue'])

const selected = ref(props.modelValue)

watch(() => props.modelValue, (newVal) => {
  selected.value = newVal
})

function selectCategory(name) {
  selected.value = name
  emit('update:modelValue', name)
}
</script>

<style scoped>
.category-selector {
  display: flex;
  gap: 4px;
}

.category-btn {
  border: 1px solid #99BC2B;
  border-radius: 24px;
  background: white;
  cursor: pointer;
  display: flex;
  gap: 8px;
  align-items: center;
  transition: background-color 0.3s;

  width: 33%;
  min-height: 50px;
}

.category-btn span {
  color: #99BC2B;
}

.category-btn.active {
  background-color: #D0F068;
  border: none;
}

.category-btn.active span {
  color: #131313;
}

.category-btn img {
  max-width: 50px;
  max-height: 50px;
  margin-bottom: 4px;
}
</style>
