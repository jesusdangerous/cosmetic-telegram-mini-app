<template>
  <div class="page-wrapper">
    <nav>
      <div>
        <IconButton><img src='../assets/images/arrow-back.svg'></IconButton>
        <NavButton text="Назад"></NavButton>
      </div>
      <NavButton text="Пропустить"></NavButton>
    </nav>
    <div class="check-number">
      <header>
        <h1>Еще немного!</h1>
        <h2>Введите код из смс</h2>
      </header>
      <label>
        <Input placeholder="_ _ _ _"></Input>
      </label>
      <div class="buttons">
        <Button text="Завершить регистрацию"></Button>
        <Button text="Отправить код повторно"></Button>
      </div>
    </div>
  </div>

</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import NavButton from '@/components/UI/NavButton.vue';
  import Input from '@/components/UI/Input.vue';
  import Button from '@/components/UI/Button.vue';
</script>

<style scoped>
  .page-wrapper {
    width: 100%;
    min-height: 486px;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding-top: 32px;
    justify-content: space-between;
  }

  nav {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }

  nav div {
    display: flex;
    gap: 8px;
    align-items: center;
  }

  .check-number {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  header {
    display: flex;
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }

  .buttons {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }


</style>
