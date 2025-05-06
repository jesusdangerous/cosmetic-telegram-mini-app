<template>
  <div class="page-wrapper">
    <header>
      <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Справка и поддержка</h1>
    </header>
    <main>
      <h2>FAQ</h2>
      <article class="quetions">
        <div class="dropdown">
          <span>Как проверить состав косметического средства?</span>
          <div class="dropdown-content">
            <p>Много способов так-то</p>
          </div>
        </div>
        <div class="dropdown">
          <span>Что такое безопасность?</span>
          <div class="dropdown-content">
            <p>Неопасность</p>
          </div>
        </div>
        <div class="dropdown">
          <span>Как добавить косметическое средство в избранное</span>
          <div class="dropdown-content">
            <p>Просто на кнопку нажми</p>
          </div>
        </div>
      </article>
      <article>
        <div>
          <h3>Политика конфиденциальности</h3>
          <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
        </div>
        <div>
          <h3>Техподдержка</h3>
          <div>
            <p>С удовольствием поможем Вам с 8:00 до 18:00 (Мск)</p>
            <a href="#">Позвонить</a>
          </div>
        </div>
        <div>
          <h3>Остались вопросы?</h3>
          <div>
            <p>Если у вас возникли вопросы
              о работе нашего сервиса — напишите
              нам! Наша команда специалистов
              всегда рада помочь.</p>
            <h4>Как к вам обращаться?</h4>
            <Input placeholder="Имя"></Input>
            <Input type="phone" placeholder="+7 999 999 99 99"></Input>
          </div>
          <div>
            <h4>Ваш вопрос</h4>
            <textarea placeholder="Вопросы, комментарии, предложения"></textarea>
            <Button text="Отправить"></Button>
          </div>
        </div>
      </article>
    </main>
  </div>
</template>

<script setup>
  import Button from '@/components/UI/Button.vue';
  import Input from '@/components/UI/Input.vue';
  import IconButton from '@/components/UI/IconButton.vue';
</script>
