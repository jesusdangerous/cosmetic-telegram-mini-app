<template>
  <div class="page-wrapper">
    <nav>
      <a href="/main-page">Пропустить</a>
    </nav>
    <header>
      <h1>Познакомимся поближе</h1>
      <p>Нам можно доверять</p>
    </header>
    <main>
      <FormAllergy />
      <div class="other">
        <h2>Другое:</h2>
        <textarea placeholder="Аллергены, которых нет в нашем списке"></textarea>
      </div>
      <div class="button-wrapper">
        <a href="/main-page"><Button text="Сохранить"></Button></a>
      </div>
    </main>
  </div>
</template>

<script setup>
import FormAllergy from '@/components/FormAllergy.vue';
import Button from '@/components/UI/Button.vue';
</script>

<style scoped>
.page-wrapper {
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 92%;
  padding: 20px 0 372px;
  margin: 0 auto;
}

nav {
  display: flex;
  justify-content: flex-end;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.other h2 {
  font-size: 20px;
}

textarea {
  padding: 12px 16px;
  border: none;
  border-radius: 12px;
  height: 100px;
  width: 100%;
  box-sizing: border-box;
}

.other {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.button-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 16px;
}

header {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

h1 {
  text-align: center;
  margin: 0;
}

header p {
  text-align: center;
  color: #545454;
  margin: 0;
}
</style>
