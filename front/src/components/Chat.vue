<template>
  <div class="chat">
    <div>
      <img  class="photo-expert" src="/images/expert-1.jpg">
      <p>Дмитрий</p>
    </div>
    <IconButton><img class="chat-button" src="/images/arrow-back.svg"></IconButton>
  </div>
</template>

<script setup>
import IconButton from './UI/IconButton.vue';
</script>

<style scoped>
.chat {
  padding: 12px;
  display: flex;
  justify-content: space-between;
  background-color: white;
  border-radius: 12px;
}

.chat div {
  display: flex;
  flex-direction: row;
  gap: 8px;
}

p {
  font-size: 1em;
  display: flex;
  align-items: center;
}

.photo-expert {
  width: 40px;
  height: 40px;
  object-fit: cover;
  border-radius: 50%;
}

.chat-button {
  transform: rotate(180deg);
}

</style>
