<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="/experts"><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Эксперт</h1>
    </header>
    <main>
      <div class="expert-info">
        <img src="../assets/images/expert-4.jpg">
        <div>
          <p>Елена</p>
          <span>Профессиональный визажист</span>
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
        <h2>Опыт в индустрии</h2>
        <p>8 лет</p>
      </div>
      <div class="expert-facts">
        <h2>Специализация</h2>
        <ul>
          <li>Создание идеального wedding-образа с учетом индивидуальных особенностей</li>
          <li>Коррекция черт лица с помощью контуринга и современных техник макияжа</li>
          <li>Эксперт по макияжу для фотосессий, видеосъемок и special events</li>
          <li>Работала с 200+ невестами, создавая долговременные стойкие образы</li>
          <li>Разработала авторский курс "Макияж для себя" с пожизненным доступом</li>
        </ul>
      </div>
      <div class="expert-consult">
        <a href="https://t.me/whqsfasagd" target="_blank" class="consult">Получить консультацию</a>
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
.consult {
  background-color: black;
  color: white;
  padding: 16px 82px;
  display: flex;
  border-radius: 12px;
}
.page-wrapper {
  width: 92%;
  padding: 20px 0 400px;
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
  width: 100%;
}

.expert-other img {
  transform: rotate(180deg);
}

</style>
