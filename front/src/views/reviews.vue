<template>
  <div class="page-wrapper">
    <teleport to="body">
        <div v-if="showSortModal" class="modal-overlay" @click.self="closeSortModal">
          <SortReviews @sort-changed="handleSortChanged" />
        </div>
      </teleport>
    <header>
      <IconButton href="/analysis-result"><img src="../assets/images/arrow-back.svg"></IconButton>
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
        <button @click="openSortModal">
          <img src="../assets/images/icon-arrow-up-down.svg">
          <p>Новые</p>
        </button>
        <a>
          <p>Оставить отзыв</p>
        </a>
      </div>
      <div class="reviews">
          <Review
            v-for="review in reviews"
            :key="review.id"
            :review="review"
          />
      </div>
    </main>


  </div>

</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import Review from '@/components/Review.vue';
  import photoUser from '@/assets/images/photo-user-1.svg'

const reviews = [
  {
    id: '1',
    userPhoto: photoUser,
    userName: 'Иван Иванов',
    date: '2025-06-06T14:22:00',
    rating: 4,
    pros: 'Быстрая доставка, отличное качество.',
    cons: 'Нет инструкции в комплекте.',
  },
  {
    id: '2',
    userPhoto: 'https://randomuser.me/api/portraits/women/45.jpg',
    userName: 'Анна Смирнова',
    date: '2025-06-05T09:10:00',
    rating: 5,
    pros: 'Очень довольна покупкой!',
    cons: 'Нет',
  },
]

import { ref } from 'vue'

// другие импорты...
import sortReviews from './sort-reviews.vue' // импорт модалки
import SortReviews from './sort-reviews.vue';

const showSortModal = ref(false)

const openSortModal = () => {
  showSortModal.value = true
}

const closeSortModal = () => {
  showSortModal.value = false
}

const handleSortChanged = (value) => {
  // здесь можно применить сортировку
  console.log('Сортировка:', value)
  closeSortModal()
}

</script>

<style scoped>
:deep(.modal-overlay) {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
}
.reviews {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.reviews-parametrs {
  display: flex;
  justify-content: space-between;
}
.reviews-parametrs button {
  background-color: #FBFBFB;
  justify-content: center;
  border: none;
  border-radius: 12px;
  display: flex;
  justify-content: space-between;
  width: 28%;
  padding: 10px 12px;
}
.reviews-parametrs a {
  display: flex;
  align-items: center;
}
main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
header {
  display: flex;
  gap: 5%;
}
h1 {
  width: 87%;
  text-align: center;
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
.page-wrapper {
  width: 92%;
  padding: 20px 0;
}
</style>
