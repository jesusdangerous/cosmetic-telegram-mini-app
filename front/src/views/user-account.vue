<template>
  <body>
    <div class="page-wrapper">
    <header>
      <IconButton href="/main-page"><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Личный кабинет</h1>
    </header>
      <main>
        <article>
          <div class="data-user">
            <div>
              <img src="../assets/images/photo-user.svg">
              <div>
                <h2>Дарья</h2>
                <p>+7 982 912 87 35</p>
              </div>
            </div>
            <button>Изменить</button>
          </div>
          <div>
            <label class="message-input" for="messages">Уведомления</label>
            <label class="checkbox-message">
              <input name="messages" type="checkbox" checked>
              <span class="checkbox-message-switch"></span>
            </label>
          </div>
          <div>
            <p>Язык</p>
            <span>Русский</span>
          </div>
          <div>
            <p style="font-weight:bold;">История анализа</p>
            <IconButton><img class="arrow" src="../assets/images/arrow-back.svg"></IconButton>
          </div>
          <div>
            <p>Реакции<!--({reaction.lenght})-->:</p>
            <button>Редактировать</button>
          </div>
          <div>
            <p>Аллергены<!--({allerg.lenght})-->:</p>
            <button>Редактировать</button>
          </div>
          <div class="help">
            <p>Справка и поддержка</p>
            <IconButton href="/support"><img class="arrow" src="../assets/images/arrow-back.svg"></IconButton>
          </div>
          <div class="exit">
            <p>Выйти</p>
            <IconButton><img src="../assets/images/icon-exit.svg"></IconButton>
          </div>
        </article>
      </main>
      <Footer></Footer>
    </div>
  </body>
</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import Footer from '@/components/Footer.vue';
</script>

<style scoped>
  .exit {
    display: flex;
    width: 100%;
  }

  .arrow {
    transform: rotate(180deg);
  }
  .help p{
    font-weight: bold;
  }
  .checkbox-message {
    display: inline-block;
    height: 28px;
    line-height: 28px;
    margin-right: 10px;
    position: relative;
    vertical-align: middle;
    font-size: 14px;
    user-select: none;
    margin: 0;
  }

  .message-input {
    font-size: 16px;
    display: flex;
    align-items: center;
  }

  .checkbox-message .checkbox-message-switch {
    position: relative;
    display: inline-block;
    box-sizing: border-box;
    width: 56px;
    height: 28px;
    border: 1px solid rgba(0, 0, 0, .1);
    border-radius: 25%/50%;
    vertical-align: top;
    background: #eee;
    transition: .2s;
  }
  .checkbox-message .checkbox-message-switch:before {
    content: '';
    position: absolute;
    top: 1px;
    left: 1px;
    display: inline-block;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: white;
    box-shadow: 0 3px 5px rgba(0, 0, 0, .3);
    transition: .15s;
  }
  .checkbox-message input[type=checkbox] {
    display: block;
    width: 0;
    height: 0;
    position: absolute;
    z-index: -1;
    opacity: 0;
  }
  .checkbox-message input[type=checkbox]:not(:disabled):active + .checkbox-message-switch:before {
    box-shadow: inset 0 0 2px rgba(0, 0, 0, .3);
  }
  .checkbox-message input[type=checkbox]:checked + .checkbox-message-switch {
    background: rgba(163, 104, 240, 1);
  }
  .checkbox-message input[type=checkbox]:checked + .checkbox-message-switch:before {
    transform:translateX(28px);
  }

  /* Focus */
  .checkbox-message.focused .checkbox-message-switch:before {
    box-shadow: inset 0px 0px 4px #ff5623;
  }

  /* Disabled */
  .checkbox-message input[type=checkbox]:disabled + .checkbox-message-switch {
    filter: grayscale(70%);
    border-color: rgba(0, 0, 0, .1);
  }
  .checkbox-message input[type=checkbox]:disabled + .checkbox-message-switch:before {
    background: #eee;
  }

  .page-wrapper{
    display: flex;
    flex-direction: column;
    gap: 32px;
    width: 92%;
    margin: 0;

    padding: 20px 16px 114px 16px;
  }

  .data-user button {
    width: 29%;
    height: 36px;
    border-radius: 12px;
    border: 1px solid rgba(19, 19, 19, 1);
    background-color: transparent;
  }

  .data-user div {
    display: flex;
    gap: 12px;
  }

  article div {
    display: flex;
    justify-content: space-between;
  }


  article div button {
    border: none;
    font-weight: bold;
    background-color: transparent;
  }

  article div p {
    font-size: 16px;
  }

  .data-user div div {
    flex-direction: column;
    gap: 8px;
  }

  .data-user {
    display: flex;
    justify-content: space-between;
  }

  article {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  header {
    display: flex;
  }

  header button{
    width: 32px;
    padding: 8px !important;
  }

  header h1 {
    width: 87%;
    text-align: center;
  }

</style>
