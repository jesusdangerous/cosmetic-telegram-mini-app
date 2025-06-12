<template>
  <div class="page-wrapper">
    <header>
      <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Эксперт</h1>
    </header>
    <main>
      <div class="expert-info">
        <img src="../assets/images/expert-1.jpg">
        <div>
          <p>Дмитрий</p>
          <span>Врач-дерматолог</span>
        </div>
      </div>
      <div class="expert-education">
        <h2>Образование</h2>
        <div class="expert-document">
          <div>
            <p>Документы</p>
            <span>Проверены</span>
          </div>
          <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
        </div>
      </div>
      <div class="expert-job">
        <h2>Стаж работы</h2>
        <p>23 года</p>
      </div>
      <div class="expert-facts">
        <h2>Интересные факты</h2>
        <ul>
          <li>
            Разработал уникальную методику терапии экземы, которая продемонстрировала 85% эффективность у пациентов;
          </li>
          <li>
            Опубликовал более 20 статей в международных медицинских журналах;
          </li>
          <li>
            Внедрил новую программу для пациентов с псориазом, которая помогла 200 людям достичь ремиссии.
          </li>
        </ul>
      </div>
      <div class="expert-consult">
        <Button text="Получить консультацию"></Button>
      </div>
      <div class="expert-other">
        <p>Найти другого специалиста</p>
        <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
      </div>
    </main>
    <Footer></Footer>
  </div>

</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import Button from '@/components/UI/Button.vue';
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
    width: 100%;
  }

  header h1 {
    width: 87%;
    text-align: center;
  }

  .expert-info {
    display: flex;
    width: 100%;
    gap: 12px;
  }

  .expert-info img {
    width: 54px;
    height: 54px;
    border-radius: 100%;
    object-fit: cover;
  }

  .expert-info div {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .expert-info div p{
    font-size: 20px;
  }

  .expert-info div span{
    font-size: 14px;
    color: #545454;
  }

  main {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  .expert-education {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .expert-education h2 {
    font-size: 20px;
  }

  .expert-document {
    display: flex;
    justify-content: space-between;
  }

  .expert-document div {
    display: flex;
    gap: 12px;
  }

  .expert-document div span{
    display: block;
    font-size: 14px;
    background-color: #D0F068;
    border-radius: 12px;
    padding: 4px 12px;
  }

  .expert-document div p {
    display: flex;
    align-items: center;
  }

  .expert-document img {
    transform: rotate(180deg);
  }

  .expert-job {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .expert-facts {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .expert-facts ul {
    padding: 0;
    margin: 0;
    margin-left: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .expert-consult button{
    padding: 16px 83px;
  }

  .expert-other {
    display: flex;
    justify-content: space-between;
    display: none;
  }

  .expert-other img {
    transform: rotate(180deg);
  }

</style>
