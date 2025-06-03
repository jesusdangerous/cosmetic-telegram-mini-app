<template>
  <body>
    <header>
        <div class="welcome">
          <div class="welcome_user"><img src="../assets/images/photo-user.svg"></div>
          <div class="welcome_hi">
            <h2>Привет, Дарья! <!--{name}--></h2>
            <h3>С любовью к деталям</h3>
          </div>
        </div>
        <InputSearch />
    </header>
      <main>
        <h1>Позаботься о своей коже уже сегодня!</h1>
        <article class="actions">
          <div class="action_check-product">
            <p>Проверить средство</p>
            <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
          </div>
          <div class="action_other">
            <div class="action_other-compare">
              <p>Сравнить составы</p>
              <div>
                <IconButton><img src="../assets/images/arrow-right.svg" alt="иконка стрелочки"></IconButton>
              </div>
            </div>
            <div class="action_other-group">
              <div class="action_other-card">
                <p>Консультация у эксперта</p>
                <div>
                  <IconButton><img src="../assets/images/arrow-right.svg" alt="иконка стрелочки"></IconButton>
                </div>
             </div>
              <div class="action_other-card">
                <p>Избранное</p>
                <div>
                  <IconButton><img src="../assets/images/arrow-right.svg" alt="иконка стрелочки"></IconButton>
                </div>
              </div>
            </div>
          </div>
        </article>
        <article class="experts">
          <div class="block_header">
            <h2>Наши эксперты</h2>
            <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
          </div>
          <ul>
              <li>
                <div class="experts_photo">
                  <p>Врач-дерматолог</p>
                </div>
                <div class="experts_info">
                  <p>Дмитрий<!--{experts.name}--></p>
                  <span>Стаж работы: 23 года<!--{exsperts.record}--></span>
                </div>

              </li>
          </ul>
        </article>
        <article class="safety">
          <div class="block_header">
            <h2>Безопасная косметика</h2>
            <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
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
            <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
          </div>
          <ul>
            <li>
              <IconButton>
                <img src="../assets/images/icon-like.svg"
                alt="иконка лайка">
              </IconButton>
              <div class="cosmetics-info">
                <div class="cosmetics-info_photo"></div>
                <div class="cosmetics-info_text">
                  <span>Крем для лица</span>
                  <p>The Act с витамином C</p>
                  <div class="cosmetics-info_safety">
                    <p>Безопасность: 89%</p>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </article>
      </main>
      <Footer></Footer>
    </body>
</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import InputSearch from '@/components/InputSearch.vue';
  import Footer from '@/components/Footer.vue';
</script>

<style scoped>

  .page-wrapper {
    width: 92%;
  }
  .memory {
    display: flex;
    gap: 16px;
    flex-direction: column;
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
    width: 87%;
    font-size: 16px;
  }

  .memory ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .cosmetics-info {
    display: flex;
    flex-direction: column;
    gap: 31px;
  }

  .cosmetics-info_safety {
    border: 1px solid rgba(163, 104, 240, 1);
    padding: 4px 12px;
    border-radius: 12px;
    width: 85%;
  }

  .cosmetics-info_safety p {
    font-size: 14px;
    color: rgba(163, 104, 240, 1);
  }

  .cosmetics-info_photo {
    background-image: url("../assets/images/photo-product.png");
    width: 116px;
    height: 128px;
    background-size: cover;
    background-repeat: no-repeat;
    margin: 0 auto;

  }

  .memory ul li {
    border-radius: 12px;
    width: 53%;
    padding: 12px;
    background-color: rgba(251, 251, 251, 1);
  }

  .memory li button {
    display: flex;
    justify-content: end;
    width: 100%
  }

  .safety {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .safety-cosmetic a{
    color: rgba(19, 19, 19, 1);
    background-color: rgba(251, 251, 251, 1);
    text-decoration: none;
    display: inline-block;
    border-radius: 12px;
    padding: 8px 12px;
    margin-right: 16px;
    margin-bottom: 16px;
  }

  .safety-cosmetic a:last-child {
    margin: 0;
  }

  .safety-cosmetic a:nth-child(9n) {
    margin-bottom: 0;
  }

  .experts {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 16px;
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
  }

  .experts_info span {
    color: rgba(84, 84, 84, 1);
    font-size: 14px;
  }

  .block_header {
    display: flex;
    justify-content: space-between;
    flex-direction: row;
  }

  .block_header h2 {
    font-size: 20px;
  }

  .block_header img {
    transform: rotate(180deg);
  }

  .experts_photo {
    background-image: url("../assets/images/expert-1.jpg");
    width: 100%;
    height:174px;
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    align-items: end;
    border-radius: 12px;
  }

  .experts_photo p {
    display: flex;
    justify-content: center;
    background-color: rgba(163, 104, 240, 1);
    width: 53%;
    border-radius: 12px;
    padding: 4px 0;
    font-size: 14px;
    color: rgba(251, 251, 251, 1);
  }

  .experts ul{
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .experts ul li {
    background-color: rgba(251, 251, 251, 1);
    border-radius: 12px;
    width: 67%;
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding-bottom: 12px;
  }

  .action_other-group {
    display: flex;
    flex-direction: column;
    gap: 16px;
    width: 64%;
  }

  .action_other-card p {
    width: 50%;
  }

  .action_other-card div{
    display: flex;
    justify-content: end;
  }

  .action_other-card button {
    background-color: rgba(251, 251, 251, 1);
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: flex;
  }

  .action_other-card{
    background-color: rgba(251, 251, 251, 0.24);
    border-radius: 12px;
    padding: 12px;
    display: flex;
    flex-direction: column;
  }

  .action_other {
    display: flex;
    gap: 16px;
  }

  .action_other-compare {
    background-color: rgba(251, 251, 251, 0.24);
    border-radius: 12px;
    width: 32%;
    padding: 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

  }

  .action_other-compare div{
    display: flex;
    justify-content: end;
  }

  .action_other-compare button {
    background-color: rgba(251, 251, 251, 1);
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: flex;
  }

  .action_other-compare p {
    font-size: 16px;
    margin: 0;
  }

  .actions {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .action_check-product {
    display: flex;
    border-radius: 16px;
    justify-content: space-between;
    background-color: rgba(251, 251, 251, 1);
  }

  .action_check-product p {
    padding: 15px;
    font-size: 1em;
    font-weight: 500;
  }

  .action_check-product button{
    padding-left: 15px;
    transform: rotate(180deg);
  }

  main {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  main h1 {
    color: rgba(251, 251, 251, 1);
    margin: 0;
    padding: 0;
    font-size: 50px;
  }

  body {
    max-width: 100%;
    background-position: center;
    padding: 20px 15px 160px;
    display: flex;
    flex-direction: column;
    gap: 32px;
    background-image: url("../assets/images/background-main.png");
    background-size: 100% 100%;
  }

  header {
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  .welcome {
    width: 100%;
    display: flex;
    min-height: 54px;
    gap: 8px;
    max-height: 54px;
  }

  .welcome_user img{
    width: 54px;
  }

  .welcome_hi {
    color: rgba(19, 19, 19, 1);
    display: flex;
    justify-content: space-between;
    flex-direction: column;
  }

  .welcome_hi h2 {
    font-size: 20px;
    padding: 0;
    margin: 0;
  }

  .welcome_hi h3 {
    font-size: 14px;
    color: rgba(84, 84, 84, 1);
    padding: 0;
    margin: 0;
  }

  .search {
    display: flex;
    width: 100%;
    justify-content: space-between;

  }

  .search label {
    display: flex;
    width: 88%;
    justify-content: space-between;
    border-radius: 16px;
    background-color: rgba(251, 251, 251, 1);
    padding-left: 16px;
  }

  .search label img {
    width: 16px;
  }
</style>
