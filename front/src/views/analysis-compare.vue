<template>
  <div class="page-wrapper">
    <header>
      <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Сравнение составов</h1>
    </header>
    <main>
      <div class="ps">
        <p>Загрузите фото состава косметического средства или вставьте его текстом.</p>
      </div>
      <div class="compare">
          <h2>1 косметическое средство</h2>
          <div>
            <a href="/analysis-scan" class="button button__ready">
              <p>Фото состава</p>
              <img src="../assets/images/icon-check.svg" alt="икнока галочки">
            </a>
            <a href="/analysis-text" class="button button__unready">
              <p>Текст состава</p>
              <img src="../assets/images/icon-text.svg" alt="икнока текста">
            </a>
          </div>

          <h2>1 косметическое средство</h2>
          <div>
              <a href="/analysis-scan" class="button button__unready">
                <p>Фото состава</p>
                <img src="../assets/images/icon-parameters.svg" alt="икнока параметров">
              </a>
              <a href="/analysis-text" class="button button__ready">
                <p>Текст состава</p>
                <img src="../assets/images/icon-check.svg" alt="икнока галочки">
              </a>
          </div>
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

  .compare {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .compare div {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  .button {
    width: 40%;
    display: flex;
    justify-content: space-between;
    border-radius: 12px;
    padding: 8px 12px;
  }
  .button__ready {
    border: 1px solid #131313;
  }
  .button__unready {
    border: 1px solid #ADADAD;
  }
  .button__unready p {
    color: #545454;
  }
  h2 {
    font-size: 20px;
  }
  h1 {
    width: 87%;
  }
  .page-wrapper {
    width: 92%;
    padding: 20px 0;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  main {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  header {
    display: flex;
    justify-content: space-between;
  }
</style>
