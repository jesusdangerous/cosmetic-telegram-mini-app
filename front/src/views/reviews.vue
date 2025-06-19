<template>
  <div class="page-wrapper">
    <teleport to="body">
      <div v-if="showSortModal" class="modal-overlay" @click.self="closeSortModal">
        <SortReviews @sort-changed="handleSortChanged" />
      </div>
      <div v-if="showReviewModal" class="modal-overlay" @click.self="closeReviewModal">
        <NewReviewModal @submit-review="handleNewReview" @cancel="closeReviewModal" />
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
          <p>{{ averageRating.toFixed(1) }}</p>
        </div>
        <span>{{ reviews.length }} {{ reviewCountText }}</span>
      </div>

      <div class="reviews-parametrs">
        <button @click="openSortModal">
          <img src="../assets/images/icon-arrow-up-down.svg">
          <p>{{ sortOption === 'newest' ? 'Новые' : 'Старые' }}</p>
        </button>
        <button
          @click="openReviewModal"
          class="leave-review-btn"
          :disabled="isSubmitting"
        >
          <span v-if="!isSubmitting">Оставить отзыв</span>
          <span v-else>Отправка...</span>
        </button>
      </div>

      <div class="reviews">
        <Review
          v-for="review in sortedReviews"
          :key="review.id"
          :review="review"
        />
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCookies } from 'vue3-cookies'
import IconButton from '@/components/UI/IconButton.vue'
import Review from '@/components/Review.vue'
import SortReviews from './sort-reviews.vue'
import NewReviewModal from './NewReviewModal.vue'
import photoUser from '@/assets/images/photo-user-1.svg'

const { cookies } = useCookies()
const COOKIE_NAME = 'product_reviews_v3'

// Состояние
const reviews = ref([])
const showSortModal = ref(false)
const showReviewModal = ref(false)
const sortOption = ref('newest')
const isSubmitting = ref(false)

// Вычисляемые свойства (остаются без изменений)
const averageRating = computed(() => {
  if (!reviews.value.length) return 0
  const sum = reviews.value.reduce((acc, review) => acc + review.rating, 0)
  return sum / reviews.value.length
})

const reviewCountText = computed(() => {
  const count = reviews.value.length
  const lastDigit = count % 10
  const lastTwoDigits = count % 100

  if (lastTwoDigits >= 11 && lastTwoDigits <= 19) return 'оценок'
  if (lastDigit === 1) return 'оценка'
  if (lastDigit >= 2 && lastDigit <= 4) return 'оценки'
  return 'оценок'
})

const sortedReviews = computed(() => {
  return [...reviews.value].sort((a, b) => {
    return sortOption.value === 'newest'
      ? new Date(b.date) - new Date(a.date)
      : new Date(a.date) - new Date(b.date)
  })
})

// Методы
const getDefaultReviews = () => [
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
  }
]

const loadReviews = () => {
  try {
    const savedReviews = cookies.get(COOKIE_NAME);

    // Добавляем более строгую проверку
    if (Array.isArray(savedReviews)) {
      // Фильтруем некорректные записи
      return savedReviews.filter(review =>
        review?.id &&
        review?.userName &&
        typeof review?.rating === 'number'
      );
    }

    // Возвращаем дефолтные отзывы, если нет сохранённых или они некорректны
    return getDefaultReviews();
  } catch (e) {
    console.error('Ошибка загрузки отзывов:', e);
    return getDefaultReviews();
  }
};


const saveReviews = () => {
  try {
    // Добавляем проверку перед сохранением
    if (!Array.isArray(reviews.value)) {
      console.error('Отзывы не являются массивом');
      return;
    }

    // Ограничиваем размер сохраняемых данных
    const reviewsToSave = reviews.value.slice(0, 50);

    cookies.set(COOKIE_NAME, reviewsToSave, {
      expires: '30d',
      secure: true,
      sameSite: 'Strict',
      path: '/'
    });

    // Логируем успешное сохранение
    console.log('Отзывы успешно сохранены');
  } catch (e) {
    console.error('Ошибка сохранения отзывов:', e);

    // Дополнительная обработка ошибки
    if (e.message.includes('exceeded')) {
      alert('Слишком много отзывов для сохранения. Некоторые отзывы не будут сохранены.');
    }
  }
};

const handleNewReview = (newReview) => {
  isSubmitting.value = true
  try {
    const review = {
      ...newReview,
      id: Date.now().toString(),
      date: new Date().toISOString(),
      userPhoto: 'https://randomuser.me/api/portraits/lego/5.jpg',
      rating: Number(newReview.rating) || 5
    }

    reviews.value = [review, ...reviews.value]
    saveReviews()
    closeReviewModal()
  } catch (error) {
    console.error('Ошибка при добавлении отзыва:', error)
    alert('Ошибка при сохранении отзыва: ' + error.message)
  } finally {
    isSubmitting.value = false
  }
}

// Остальные методы остаются без изменений
const openSortModal = () => {
  showSortModal.value = true
}

const closeSortModal = () => {
  showSortModal.value = false
}

const openReviewModal = () => {
  showReviewModal.value = true
}

const closeReviewModal = () => {
  showReviewModal.value = false
}

const handleSortChanged = (option) => {
  sortOption.value = option
  closeSortModal()
}

// Инициализация
onMounted(() => {
  reviews.value = loadReviews()
})
</script>

<style scoped>
.page-wrapper {
  width: 92%;
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

header {
  display: flex;
  gap: 5%;
  align-items: center;
}

h1 {
  width: 87%;
  text-align: center;
  margin: 0;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.reviews-info {
  display: flex;
  gap: 12px;
  align-items: center;
}

.reviews-info div {
  display: flex;
  gap: 5px;
  align-items: center;
}

.reviews-info span {
  color: #545454;
  font-size: 14px;
}

.reviews-parametrs {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.reviews-parametrs button {
  background-color: #FBFBFB;
  border: none;
  border-radius: 12px;
  padding: 10px 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.leave-review-btn {
  background: none;
  border: none;
  color: #007BFF;
  cursor: pointer;
  padding: 0;
  font-size: inherit;
  transition: opacity 0.3s;
}

.leave-review-btn:hover:not(:disabled) {
  text-decoration: underline;
  opacity: 0.8;
}

.leave-review-btn:disabled {
  color: #cccccc;
  cursor: not-allowed;
}

.reviews {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.modal-overlay {
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
</style>
