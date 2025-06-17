<template>
  <div class="page-wrapper">
    <NavButton text="Пропустить"></NavButton>
    <div class="main">
      <header>
        <h1>Добро пожаловать!</h1>
        <h2>Введите свои данные для регистрации</h2>
      </header>
      <div class="data-user">
          <form ref="userForm" method="post" @submit="handleSubmit">
            <label>
              <Input placeholder="Имя"></Input>
            </label>
            <label>
              <Input type="email" placeholder="Почта"></Input>
            </label>
          <div class="checkbox">
            <div>
              <input type="checkbox" id="true-data">
              <label for="true-data">Даю согласие на обработку данных</label>
            </div>
            <Button router-link='/check-number' text="Получить код"></Button>
          </div>
        </form>
      </div>
    </div>
    <footer>
      <p>Или войти через</p>
      <div>
        <IconButton><img src="../assets/images/icon-google.svg"></IconButton>
        <IconButton><img src="../assets/images/icon-apple.svg"></IconButton>
        <IconButton><img src="../assets/images/icon-wk.svg"></IconButton>
      </div>
    </footer>
  </div>
</template>

<script setup>
  import Input from '@/components/UI/Input.vue';
  import Button from '@/components/UI/Button.vue';
  import IconButton from '@/components/UI/IconButton.vue';
  import NavButton from '@/components/UI/NavButton.vue';

</script>

<style scoped>
  .page-wrapper {
    min-height: 600px;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding-top: 32px;
    justify-content: space-between;
  }

  .skip-button {
    border: none;
    background-color: transparent;
  }

  .main {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  button {
    margin-left: auto;
  }

  header {
    display: flex;
    flex-direction: column;
    color: rgba(19, 19, 19, 1);
    text-align: center;
    gap: 12px;
  }

  h1 {
    margin: 0;
    font-size: 32px;
  }

  h2 {
    font-size: 16px;
    margin: 0;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  .data-user {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .checkbox {
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  footer {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  footer p {
    margin: 0;
    text-align: center;
  }

  footer div {
    display: flex;
    gap: 16px;
  }
</style>
