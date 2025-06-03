<template>
  <div>
    <label>
      <img class="icon-search" src="../assets/images/icon-search.svg"
      alt="иконка лупы">
      <Input placeholder="Поиск"></Input>
    </label>
    <IconButton><img src="../assets/images/icon-parameters.svg"></IconButton>
  </div>
</template>

<script setup>
  import Input from './UI/Input.vue';
  import IconButton from './UI/IconButton.vue';
</script>

<style scoped>
  div {
    display: flex;
    justify-content: space-between;
  }

  input {
    padding: 0;
  }

  label {
    min-width: 89%;
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
