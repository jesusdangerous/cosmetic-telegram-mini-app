<template>
  <div class="product-card">
    <div class="product-btn">
      <IconButton><img src='/images/icon-like.svg' alt="иконка сердечка"></IconButton>
    </div>
    <div class="product-image">
      <img :src="image" :alt="altText" />
    </div>
    <div class="product-info">
      <h3 class="product-title">{{ title }}</h3>
      <p class="product-brand">{{ brand }}</p>
      <p class="product-description">{{ description }}</p>
      <Button
        class="details-button"
        :text="buttonText"
        :href="detailsLink"
      />
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import IconButton from './UI/IconButton.vue';
import Button from './UI/Button.vue';

const props = defineProps({
  image: {
    type: String,
    required: true,
  },
  altText: {
    type: String,
    default: 'Product image',
  },
  title: {
    type: String,
    required: true,
  },
  brand: {
    type: String,
    default: '', // Сделаем необязательным
  },
  description: {
    type: String,
    default: '', // Сделаем необязательным
  },
  detailsLink: {
    type: String,
    required: true,
  },
  buttonText: {
    type: String,
    default: 'Подробнее'
  }
})
</script>

<style scoped>
.product-btn {
  display: flex;
  justify-content: flex-end;
}

.product-card {
  border: 1px solid #FBFBFB;
  background-color: #FBFBFB;
  border-radius: 8px;
  padding: 12px 12px 0;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
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
</style>
