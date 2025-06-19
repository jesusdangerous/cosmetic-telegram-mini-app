<template>
  <div class="review-card">
    <div class="review-info">
      <div class="user-info">
        <div class="avatar-wrapper">
          <img :src="review.userPhoto" :alt="review.userName" class="avatar-img" />
        </div>
        <div class="review-name">
          <div class="font-weight-medium">{{ review.userName }}</div>
          <div class="text-caption text-grey">{{ formattedDate }}</div>
        </div>
      </div>

      <div class="stars">
        <img
          v-for="n in 5"
          :key="n"
          :src="n <= review.rating ? filledStar : emptyStar"
          alt="star"
          class="star"
        />
      </div>
    </div>

    <div class="review-text mt-2">
      <div v-if="review.pros">
        <span>Достоинства:</span>
        <p>{{ review.pros }}</p>
      </div>
      <div v-if="review.cons" class="mt-2">
        <span>Недостатки:</span>
        <p>{{ review.cons }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import filledStar from '/images/reviews-star.svg'
import emptyStar from '/images/reviews-star-empty.svg'

const props = defineProps({
  review: Object,
})

const formattedDate = computed(() => {
  return new Date(props.review.date).toLocaleString('ru-RU', {
    day: '2-digit',
    month: 'long',
    hour: '2-digit',
    minute: '2-digit',
  })
})
</script>

<style scoped>
.review-card {
  background-color: #FBFBFB;
  padding: 12px;
  border-radius: 12px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.review-info {
  display: flex;
  justify-content: space-between;
}

.user-info {
  display: flex;
  gap: 12px;
}

.avatar-wrapper {
  overflow: hidden;
  flex-shrink: 0;
}

.avatar-img {
  width: 40px;
  height: 40px;
  object-fit: contain;
  border-radius: 99px;
}

.review-name {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.font-weight-medium {
  font-weight: 500;
  font-size: 16px;
  color: #222;
}

.text-caption {
  font-size: 12px;
  color: #888;
}

.text-grey {
  color: #888;
}

.stars {
  display: flex;
  align-items: flex-start;
  gap: 4px;
}

.star {
  width: 15px;
  height: 16px;
}


.review-text span {
  color: #545454;
  font-size: 14px;
}

.review-text p {
  font-size: 14px;
}
.review-text {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>
