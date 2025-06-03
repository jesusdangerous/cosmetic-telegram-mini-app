<template>
  <div>
    <label>
      <img class="icon-search" src="../assets/images/icon-search.svg" alt="иконка лупы">
      <Input :placeholder="placeholder"></Input>
    </label>
  </div>
</template>

<script setup>
import Input from './UI/Input.vue';
import IconButton from './UI/IconButton.vue';

const props = defineProps({
  placeholder: {
    type: String,
    default: "Поиск" // Значение по умолчанию, если не передано
  }
});
</script>

<style scoped>
  div {
    display: flex;
    justify-content: space-between;
  }

  input {
    padding: 0;
    min-width: 93%;
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

  button {
    margin: 0;
  }

</style>
