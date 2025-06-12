<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="/main-page"><img src='../assets/images/arrow-back.svg'></IconButton>
      <h1>Анализ состава</h1>
    </header>
    <main>
      <div>
        <a href="/analysis-scan">
          <p>Загрузить фото состава</p>
          <img src="../assets/images/icon-scan-white.svg" alt="иконка скана">
        </a>
        <p>Загрузить фото состава косметического средства из галереи или сделать новое фото через камеру</p>
      </div>
      <div>
        <a href="/analysis-text">
          <p>Ввести состав текстом</p>
          <img src="../assets/images/icon-text-white.svg" alt="иконка текста">
        </a>
        <p>Ввести состав косметического средства вручную</p>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import Footer from '@/components/Footer.vue';
</script>

<style scoped>
  .page-wrapper {
    width: 92%;
    padding: 20px 0;
    display: flex;
    gap: 192px;
    flex-direction: column;
  }

  header {
    display: flex;
    flex-direction: row;
  }

  h1 {
    width: 87%;
    text-align: center;
  }

  main {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  div {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  div p {
    color: #545454;
  }

  div a {
    display: flex;
    background-color: #131313;
    justify-content: space-between;
    padding: 16px 12px;
    border-radius: 12px;
  }

  div a p {
    color: #FBFBFB;
  }


</style>
