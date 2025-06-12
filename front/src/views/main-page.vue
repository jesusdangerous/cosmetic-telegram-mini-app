<template>
  <div class="page-wrapper">
    <header>
      <div class="welcome">
        <div class="welcome_user">
          <img src="../assets/images/photo-user.svg" alt="Фото пользователя" />
        </div>
        <div class="welcome_hi">
          <h2>Привет, Алина!</h2>
          <h3>С любовью к деталям</h3>
        </div>
      </div>

      <div class="search">
        <InputSearch />
        <IconButton>
          <img src="../assets/images/icon-parameters.svg" alt="Параметры" />
        </IconButton>
      </div>
    </header>

    <main>
      <h1>Позаботься о своей коже уже сегодня!</h1>
      <article class="actions">
        <div class="action_check-product">
          <p>Проверить средство</p>
          <IconButton href="/analysis" class="icon-arrow">
            <img src="../assets/images/arrow-back.svg" alt="Иконка стрелочки" />
          </IconButton>
        </div>

        <div class="action_other">
          <div class="action_other-compare">
            <p>Сравнить составы</p>
            <IconButton href="/analysis-compare" class="icon-arrow">
              <img src="../assets/images/arrow-right.svg" alt="Иконка стрелочки" />
            </IconButton>
          </div>

          <div class="action_other-group">
            <div class="action_other-card">
              <p>Консультация у эксперта</p>
              <IconButton href="/chats" class="icon-arrow">
                <img src="../assets/images/arrow-right.svg" alt="Иконка стрелочки" />
              </IconButton>
            </div>

            <div class="action_other-card">
              <p>Избранное</p>
              <IconButton href="/favourites" class="icon-arrow">  <!--страницы очень похожи-->
                <img src="../assets/images/arrow-right.svg" alt="Иконка стрелочки" />
              </IconButton>
            </div>
          </div>
        </div>
      </article>

      <article class="experts">
        <div class="block_header">
          <h2>Наши эксперты</h2>
          <IconButton href="/experts">
            <img src="../assets/images/arrow-back.svg" alt="Иконка стрелочки" />
          </IconButton>
        </div>
        <ul>
          <li>
            <div class="experts_photo">
              <p>Врач-дерматолог</p>
            </div>
            <div class="experts_info">
              <p>Дмитрий</p>
              <span>Стаж работы: 23 года</span>
            </div>
          </li>
        </ul>
      </article>

      <article class="safety">
        <div class="block_header">
          <h2>Безопасная косметика</h2>
          <IconButton href="/safety-cosmetics">
            <img src="../assets/images/arrow-back.svg" alt="Иконка стрелочки" />
          </IconButton>
        </div>
        <div class="safety-cosmetic">
          <a href="#">Тональные крема</a>
          <a href="#">Шампуни</a>
          <a href="#">Хайлайтеры</a>
          <a href="#">Крема</a>
          <a href="#">Подводки</a>
          <a href="#">Помады</a>
          <a href="#">Глиттеры</a>
          <a href="#">Бронзеры</a>
          <a href="#">Пудры</a>
          <a href="#">Румяна</a>
        </div>
      </article>

      <article class="memory">
        <div class="block_header">
          <h2>Вы проверяли</h2>
          <IconButton href="/favourites">  <!--страницы очень похожи-->
            <img src="../assets/images/arrow-back.svg" alt="Иконка стрелочки" />
          </IconButton>
        </div>
        <ul>
          <li v-for="(product, index) in products" :key="index">
            <CardMini
              :image="product.image"
              :alt="product.alt"
              :title="product.title"
              :brand="product.brand"
              :description="product.description"
            />
          </li>
        </ul>
      </article>
    </main>
    <Footer></Footer>
  </div>
</template>

<script setup>
import IconButton from '@/components/UI/IconButton.vue';
import InputSearch from '@/components/InputSearch.vue';
import Footer from '@/components/Footer.vue';
import CardMini from '@/components/CardMini.vue';
import photoProduct from '@/assets/images/photo-product.svg'
import { ref } from 'vue'
const products = ref([
  {
    image: photoProduct,
    alt: 'Крем для рук и тела LABORATORIUM Вишневый пирог',
    title: 'Крем для рук и тела',
    brand: 'LABORATORIUM',
    description: 'Вишневый пирог',
  },
])
</script>

<style scoped>
.page-wrapper {
  width: 92%;
  padding: 20px 15px 160px;
  background-image: url("../assets/images/background-main.png");
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  gap: 32px;
  color: rgba(19, 19, 19, 1);
}

header {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.welcome {
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 54px;
}

.welcome_user img {
  width: 54px;
  height: 54px;
  object-fit: cover;
  border-radius: 50%;
}

.welcome_hi {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.welcome_hi h2 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
}

.welcome_hi h3 {
  margin: 0;
  font-size: 14px;
  color: rgba(84, 84, 84, 1);
}

.search {
  display: flex;
  gap: 4px;
  align-items: center;
  width: 100%;
}

main {
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 100%;
}

main h1 {
  font-size: 50px;
  margin: 0;
  color: white;
}

.actions {
  width: 92%;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.action_check-product img {
  background-color: white;
  transform: rotate(180deg);
}
.action_check-product {
  background-color: rgba(251, 251, 251, 1);
  border-radius: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 8px;
}

.action_check-product p {
  margin: 0;
  font-weight: 500;
  font-size: 1em;
}

.action_check-product button {
  transform: rotate(180deg);
  background: none;
  border: none;
}

.action_other {
  display: flex;
  gap: 16px;
}

.action_other img {
  background-color: white;
  padding: 9px 13px;
  border-radius: 50%;
}

.icon-button {
  display: flex;
  align-items: flex-end;
}

.action_other-compare,
.action_other-card {
  background-color: rgba(251, 251, 251, 0.24);
  border-radius: 12px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 32%;
}

.action_other-group {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 64%;
}

.action_other-card {
  width: 100%;
  padding: 12px;
  background-color: rgba(251, 251, 251, 0.24);
  border-radius: 12px;
}

.action_other-card p {
  margin: 0;
  width: 50%;
}

.action_other-card button,
.action_other-compare button {
  background-color: rgba(251, 251, 251, 1);
  border-radius: 50%;
  width: 32px;
  height: 32px;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.action_other-compare p {
  font-size: 16px;
  margin: 0 0 12px 0;
}

.experts {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.block_header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.block_header h2 {
  font-size: 20px;
  margin: 0;
}

.block_header img {
  transform: rotate(180deg);
  cursor: pointer;
}

.experts ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.experts ul li {
  background-color: rgba(251, 251, 251, 1);
  border-radius: 12px;
  width: 60%;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-bottom: 12px;

}

.experts_photo {
  background-image: url("../assets/images/expert-1.jpg");
  height: 174px;
  background-repeat: no-repeat;
  background-size: contain;
  border-radius: 12px;
  display: flex;
  margin: 0;
  align-items: flex-end;
  padding: 8px;
}

.experts_photo p {
  background-color: rgba(163, 104, 240, 1);
  border-radius: 12px;
  color: white;
  font-size: 14px;
  padding: 4px 0;

  text-align: center;
  width: 55%;
  margin: 0;
}

.experts_info {
  display: flex;
  flex-direction: column;
  gap: 4px;
  width: 90%;
  margin: 0 auto;
}

.experts_info p {
  font-size: 16px;
  margin: 0;
}

.experts_info span {
  font-size: 14px;
  color: rgba(84, 84, 84, 1);
  margin: 0;
}

.safety {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.safety-cosmetic a {
  color: rgba(19, 19, 19, 1);
  background-color: rgba(251, 251, 251, 1);
  border-radius: 12px;
  padding: 8px 12px;
  text-decoration: none;
  margin-right: 16px;
  margin-bottom: 16px;
  display: inline-block;
}

.safety-cosmetic a:last-child {
  margin-right: 0;
  margin-bottom: 0;
}

.memory {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.memory ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.memory ul li {
  border-radius: 12px;
  padding: 12px;
  display: flex;
  gap: 16px;
  align-items: center;
  box-sizing: border-box;
  width: 53% !important;
}

.cosmetics-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cosmetics-info_photo {
  background-image: url("../assets/images/photo-product.png");
  width: 116px;
  height: 128px;
  background-size: cover;
  background-repeat: no-repeat;
  border-radius: 12px;
  margin: 0 auto;
}

.cosmetics-info_text {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.cosmetics-info_text span {
  font-size: 14px;
  color: rgba(84, 84, 84, 1);
}

.cosmetics-info_text p {
  font-size: 16px;
  margin: 0;
  width: 87%;
}

.cosmetics-info_safety {
  border: 1px solid rgba(163, 104, 240, 1);
  border-radius: 12px;
  padding: 4px 12px;
  width: 85%;
}

.cosmetics-info_safety p {
  font-size: 14px;
  color: rgba(163, 104, 240, 1);
  margin: 0;
}
</style>
