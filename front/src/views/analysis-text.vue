<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="/analysis"><img src='/images/arrow-back.svg'></IconButton>
      <h1>Анализ состава</h1>
    </header>
    <main>
      <div>
        <textarea placeholder="Состав косметического средства" name="" id=""></textarea>
      </div>
      <div>
        <h2>
          Для качественного анализа с помощью текста необходимо:
        </h2>
        <div class="instruction">
          <p>1. Ввести все компоненты без лишних пробелов, отделяя их запятыми;</p>
          <p>2. Избегать сокращений;</p>
          <p>3. Не пропустить ни одного компонента;</p>
          <p>4. Проверить введенный текст на наличие ошибок.</p>
        </div>
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
</style>
