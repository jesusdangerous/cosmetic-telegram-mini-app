<!-- InputSearch.vue -->
<template>
  <div>
    <label>
      <img class="icon-search" src="../assets/images/icon-search.svg" alt="иконка лупы" />
      <Input
        :placeholder="placeholder"
        :inputStyle="{ width: width }"
        v-model="searchValue"
      />
    </label>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import Input from './UI/Input.vue'

const props = defineProps({
  placeholder: {
    type: String,
    default: 'Поиск'
  },
  width: {
    type: String,
    default: '93%'
  }
})

const searchValue = ref('')

</script>

<style scoped>
div {
  display: flex;
  justify-content: space-between;
}

label {
  max-width: 100%;
  display: flex;
  background-color: #FBFBFB;
  border-radius: 12px;
}

.icon-search {
  background-color: #FBFBFB;
  padding: 14px;
  border-radius: 12px;
}
</style>
