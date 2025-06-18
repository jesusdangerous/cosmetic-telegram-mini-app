<template>
  <body>
  <div class="page-wrapper">
    <IconButton><img src="../assets/images/icon-cross.svg"></IconButton>
    <div>
      <h1>Внимание!</h1>
      <p>Для достоверного результата
        необходимо указать реакции в 
        личном кабинете</p>
      <Button text="Перейти в личный кабинет"></Button>
    </div>
  </div>
  </body>
</template>

<script setup>
import Button from '@/components/UI/Button.vue';
import IconButton from '@/components/UI/IconButton.vue';
</script>

<style scoped>
.page-wrapper {
  width: 84%;
  padding: 24px 16px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  border-radius: 12px;
  box-shadow: 0 0 5px rgba(122,122,122,0.5);
}

a{
  margin-left: 95%;
}

.page-wrapper div {
  display: flex;
  flex-direction: column;
  gap: 14px;
  text-align: center;
}

h1 {
  font-size: 20px;
}

p {
  font-size: 16px;
}

.page-wrapper div button {
  width: 100%;
  height: 36px;
  font-size: 16px;
  font-weight: normal;
  margin: 0;
}
</style>
