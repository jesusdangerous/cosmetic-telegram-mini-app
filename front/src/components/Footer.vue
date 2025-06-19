<template>
  <footer>
    <nav>
      <a href="/main-page"><img src="/images/icon-home.svg"></a>
      <a href="/experts"><img src="/images/icon-comment.svg"></a>
      <a href="/analysis"><img src="/images/icon-scan.svg"></a>
      <a href="/favourites"><img src="/images/icon-like.svg"></a>
      <a href="/user-account"><img src="/images/icon-profile.svg"></a>
    </nav>
  </footer>
</template>

<script setup>
</script>

<style scoped>
  footer {
  width: 93vw;
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
