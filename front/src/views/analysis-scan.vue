<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="/analysis"><img src='../assets/images/arrow-back.svg'></IconButton>
      <h1>Анализ состава</h1>
    </header>
    <main>
      <div>
        <h2>
          Для качественного анализа с помощью фото необходимо:
        </h2>
        <div class="instruction">
          <p>1. Выбрать хорошо освещенное место;</p>
          <p>2. Убедиться, что этикетка хорошо видна и находится в фокусе;</p>
          <p>3. На фото отсутствуют блики и отражения;</p>
          <p>4. Фон нейтральный.</p>
        </div>
      </div>
      <div  class="buttons">
        <button>
          <p>Из галереи</p>
          <IconButton><img src="../assets/images/icon-clip.svg"></IconButton>
        </button>
        <button>
          <p>Открыть камеру</p>
          <IconButton><img src="../assets/images/icon-scan-black.svg"></IconButton>
        </button>
      </div>
      <div>
        <a href="/analysis-result">
          <p>Анализ состава</p>
        </a>
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
    flex-direction: column;
    gap: 32px;
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

  textarea {
    width: 90%;
    resize: none;
    min-height: 15vh;
    border: none;
    border-radius: 12px;
    padding: 12px 16px;
  }

  h2 {
    font-size: 20px;
  }

  div {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  div div {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .instruction p {
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
    width: 100%;
    color: #FBFBFB;
    text-align: center;
  }

  .buttons {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }

  .buttons button {
    width: 47%;
    display: flex;
    padding: 8px 12px;
    justify-content: space-between;
    background-color: #FBFBFB;
    border: 1px solid #131313;
    border-radius: 12px;
    background: transparent;
  }
</style>
