<template>
  <div class="page-wrapper">
    <header>
      <div>
        <div class="user"><img src="../assets/images/photo-user.svg"></div>
          <div class="welcome">
          <h2>Привет, Дарья! <!--{name}--></h2>
          <h3>С любовью к деталям</h3>
        </div>
        <div class="search">
          <Input />
          <IconButton><img src="../assets/images/icon-parameters.svg"></IconButton>
        </div>
      </div>
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
              <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
            </div>
            <div class="action_other-group">
              <div>
                <p>Консультация у эксперта</p>
                <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
              </div>
              <div>
                <p>Избранное</p>
                <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
              </div>
            </div>
          </div>
        </article>
        <article class="experts">
          <div class="experts_header">
            <h2>Наши эксперты</h2>
            <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
          </div>
          <ul>
              <li>
                <div class="experts_photo">
                  <img src="" alt="Фото эксперта">
                  <p>Врач-дерматолог</p>
                </div>
                <p>Дмитрий<!--{experts.name}--></p>
                <span>Стаж работы: 23 года<!--{exsperts.record}--></span>
              </li>
          </ul>
        </article>
        <article class="safety">
          <div class="safety_header">
            <h2>Безопасная косметика</h2>
            <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
          </div>
          <div class="safety-cosmetic">
            <p>Тональные крема</p>
            <p>Шампуни</p>
            <p>Хайлайтеры</p>
            <p>Крема</p>
            <p>Подводки</p>
            <p>Помады</p>
            <p>Глиттеры</p>
            <p>Бронзеры</p>
            <p>Пудры</p>
            <p>Румяна</p>
          </div>
        </article>
        <article class="memory">
          <div class="memory_header">
            <h2>Вы проверяли</h2>
            <IconButton><img src="../assets/images/arrow-back.svg" alt="иконка стрелочки"></IconButton>
          </div>
          <ul>
            <li>
              <IconButton>
                <img src="../assets/images/icon-like.svg"
                alt="иконка лайка">
              </IconButton>
              <div>
                <img src="">
                <span>Крем для лица</span>
                <p>The Act с витамином C</p>
                <div>
                  <p>Безопасность: 89%</p>
                </div>
              </div>
            </li>
          </ul>
        </article>
      </main>
    </header>

  </div>
</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import Input from '@/components/UI/Input.vue';
</script>
