<template>
  <div class="product-card">
    <div class="product-btn">
      <button
        class="favorite-btn"
        @click.stop="toggleFavorite"
        aria-label="Добавить в избранное"
      >
        <img
          :src="isFavorite ? '/images/trashcan.svg' : '/images/icon-like.svg'"
          :alt="isFavorite ? 'Удалить из избранного' : 'Добавить в избранное'"
          class="favorite-icon"
        >
      </button>
    </div>
    <div class="product-image">
      <img :src="image" :alt="altText" class="product-img">
    </div>
    <div class="product-info">
      <h3 class="product-title">{{ title }}</h3>
      <p v-if="brand" class="product-brand">{{ brand }}</p>
      <p v-if="description" class="product-description">{{ description }}</p>
      <a
        v-if="detailsLink"
        :href="detailsLink"
        class="details-button"
        target="_blank"
        rel="noopener noreferrer"
        @click.stop
      >
        {{ buttonText }}
      </a>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useFavoritesStore } from '@/stores/favorites'

const props = defineProps({
  image: {
    type: String,
    required: true
  },
  altText: {
    type: String,
    default: 'Product image'
  },
  title: {
    type: String,
    required: true
  },
  brand: {
    type: String,
    default: ''
  },
  description: {
    type: String,
    default: ''
  },
  detailsLink: {
    type: String,
    default: ''
  },
  buttonText: {
    type: String,
    default: 'Подробнее'
  }
})

const favoritesStore = useFavoritesStore()

const currentProduct = computed(() => ({
  title: props.title,
  image: props.image,
  altText: props.altText,
  brand: props.brand,
  description: props.description,
  detailsLink: props.detailsLink
}))

const isFavorite = computed(() => favoritesStore.isFavorite(props.title))

const toggleFavorite = () => {
  favoritesStore.toggleFavorite(currentProduct.value)
}
</script>

<style scoped>
.product-card {
  position: relative;
  border: 1px solid #FBFBFB;
  background-color: #FBFBFB;
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.product-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 2;
}

.favorite-btn {
  background: none;
  border: none;
  padding: 8px;
  cursor: pointer;
}

.favorite-icon {
  width: 24px;
  height: 24px;
}

.product-image img {
  width: 67%;
  display: block;
  margin: 0 auto;
}

.product-info {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding-bottom: 12px;
}

.product-title {
  font-size: 0.9em;
  color: #545454;
  margin: 0;
}

.product-brand {
  font-size: 1em;
  margin: 0;
  color: #333;
}

.product-description {
  font-size: 1em;
  margin: 0;
  color: #666;
}

.details-button {
  display: inline-block;
  margin-top: 8px;
  padding: 6px 12px;
  background-color: #6200ee;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 0.8em;
  text-align: center;
}
</style>
