<template>
  <footer>
    <nav>
      <IconButton><img src="../assets/images/icon-home.svg"></IconButton>
      <IconButton><img src="../assets/images/icon-comment.svg"></IconButton>
      <IconButton><img src="../assets/images/icon-scan.svg"></IconButton>
      <IconButton><img src="../assets/images/icon-like.svg"></IconButton>
      <IconButton><img src="../assets/images/icon-profile.svg"></IconButton>
    </nav>
  </footer>
</template>

<script setup>
import IconButton from './UI/IconButton.vue';
</script>

<style scoped>
  footer {
  width: 93%;
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  padding: 0;
}


  nav {
    display: flex;
    justify-content: space-between;
    border-radius:32px;
    background-color: rgba(251, 251, 251, 0.64);
  }

  nav img {
    width: 16px;
    padding: 12px;
  }
</style>
