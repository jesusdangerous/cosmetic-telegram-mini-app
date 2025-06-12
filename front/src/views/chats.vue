<template>
  <div class="page-wrapper">
    <header>
      <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Чаты</h1>
    </header>
    <main>
      <InputSearch></InputSearch>
      <div class="chats">
        <Chat></Chat>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import InputSearch from '@/components/InputSearch.vue';
  import Chat from '@/components/Chat.vue';
  import Footer from '@/components/Footer.vue';
</script>

<style scoped>
.page-wrapper {
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 92%;
  padding: 20px 0;
}

header {
  display: flex;
  justify-content: space-between;
}

h1 {
  width: 95%;
  text-align: center;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.chats {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
