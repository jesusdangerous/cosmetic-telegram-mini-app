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

import photoL1 from '/images/l1.jpg';
import photoL2 from '/images/l2.jpg';

const products = ref([
  {
    image: photoL1,
    alt: '',
    title: 'L`ORÉAL PARIS Нюдовая помада для губ Color Riche Les Nus',
    brand: '',
    description: '',
    detailsLink: 'https://www.letu.ru/product/l-oreal-paris-nyudovaya-pomada-dlya-gub-color-riche/96700004?sort=default&open=volumeProduct~brand~productClass~gender~forWhom&hide=line'
  },
  {
    image: photoL2,
    alt: '',
    title: 'ЛЭТУАЛЬ Увлажняющая помада для губ Rouge Desir Drop',
    brand: '',
    description: '',
    detailsLink: 'https://www.letu.ru/product/l-etual-uvlazhnyayushchaya-pomada-dlya-gub-rouge-desir-drop/113500079?sort=default&open=volumeProduct~brand~productClass~gender~forWhom&hide=line'
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
