<template>
  <a :href="href" class="icon-button">
    <slot></slot>
  </a>
</template>

<script setup>
const props = defineProps({
  href: {
    type: String,
    default: '#',
  },
})
</script>

<style scoped>
.icon-button {
  padding: 0px;
  width: max-content;
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  background-color: transparent;
}

.icon-button img {
  width: 48px;
  height: 48px;
}
</style>
