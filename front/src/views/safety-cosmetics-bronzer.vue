<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="main-page">
        <img src="/images/arrow-back.svg" />
      </IconButton>
      <h1>Безопасная косметика</h1>
    </header>
    <main>
      <InputSearch width="100%" />
      <div class="search">
        <p>Найдено {{ products.length }} косметических средств</p>
      </div>
      <div class="cards">
        <CardMini
          v-for="(product, index) in products"
          :key="index"
          :image="product.image"
          :alt-text="product.alt || product.title"
          :title="product.title"
          :brand="product.brand"
          :description="product.description"
          :details-link="product.detailsLink"
        />
      </div>
    </main>
  </div>
</template>

<script setup>
import InputSearch from '@/components/InputSearch.vue'
import IconButton from '@/components/UI/IconButton.vue'
import CardMini from '@/components/CardMini.vue'
import { ref } from 'vue'

import photoB1 from '/images/b1.jpg';
import photoB2 from '/images/b2.jpg';

const products = ref([
  {
    image: photoB1,
    alt: '',
    title: 'DOLCE&GABBANA Стойкий бронзер и тени для век Face&eyes match',
    brand: '',
    description: '',
    detailsLink: 'https://www.letu.ru/product/dolce-gabbana-stoikii-bronzer-i-teni-dlya-vek-face-eyes-match/161000596'
  },
  {
    image: photoB2,
    alt: '',
    title: 'LUXVISAGE Бронзер MULTI Color',
    brand: '',
    description: '',
    detailsLink: 'https://www.letu.ru/product/luxvisage-bronzer-multi-color/147600903'
  },
])
</script>

<style scoped>
.page-wrapper {
  width: 92%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 32px;
  flex-direction: column;
  padding: 20px 0;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

header {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 16px;
}

header h1 {
  flex: 1;
  text-align: center;
  margin: 0;
  font-size: 1.5rem;
}

.search p {
  margin: 0;
  color: #666;
  font-size: 0.9rem;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

@media (max-width: 768px) {
  .page-wrapper {
    width: 90%;
    gap: 24px;
  }

  .cards {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
  }
}

@media (max-width: 480px) {
  header h1 {
    font-size: 1.2rem;
  }

  .cards {
    grid-template-columns: 1fr;
  }
}
</style>
