<template>
  <body>
    <div class="page-wrapper">
        <IconButton><img src="../assets/images/icon-cross.svg"></IconButton>
      <div>
        <h1>Внимание!</h1>
        <p>Удалить Belka mineral из избранного?</p>
        <div>
          <button><p>Удалить</p></button>
          <button><p>Отмена</p></button>
        </div>
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
    width: 70%;
    padding: 24px 16px 16px 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    border-radius: 12px;
    box-shadow: 0 0 5px rgba(122,122,122,0.5);
  }

  button{
    margin-left: 95%;
  }

  .page-wrapper p {
    width: 80%;
    margin: 0 auto;
  }

  .page-wrapper div div {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 55%;
    margin: 0 auto;
  }

  .page-wrapper div div button {
    width: 103px;
    border: none;
    background-color: #F3F2F8;

  }

  .page-wrapper div div button p {
    color: #A368F0;
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
