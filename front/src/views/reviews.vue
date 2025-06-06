<template>
  <header>
    <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
    <h1>Отзывы</h1>
  </header>
  <main>
    <div class="reviews-info">
      <div>
        <img src="../assets/images/reviews-star.svg">
        <p>4,3</p>
      </div>
      <span>14 оценок</span>
    </div>
    <div class="reviews-parametrs">
      <button>
        <img src="../assets/images/icon-arrow-up-down.svg">
        <p>Новые</p>
      </button>
      <a>
        <p>Оставить отзыв</p>
      </a>
    </div>
  </main>
</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
</script>

<style scoped>
header {
  display: flex;
}
h1 {
  width: 87%;
}
.page-wrapper {
  width: 92%;
  display: flex;
  flex-direction: column;
  gap: 32px;
  padding: 20px 0;
}
.reviews-info {
  display: flex;
  gap: 12px;
}
.reviews-info span {
  color: #545454;
  font-size: 14px;
  display: flex;
  align-items: end;
}
.reviews-info div {
  display: flex;
  gap: 5px;
}
</style>
