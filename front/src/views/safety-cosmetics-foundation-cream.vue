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
          :alt-text="product.alt"
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
import photoTon1 from '/images/ton1.png';
import photoTon2 from '/images/ton2.png';

const products = ref([
  {
    image: photoTon1,
    alt: 'Тональный флюид для сияния кожи OnColour',
    title: 'Тональный флюид для сияния кожи OnColour',
    brand: '',
    description: '',
    detailsLink: 'https://www.oriflame.ru/products/product?code=39292&store=RU-business_oriflame'
  },
  {
    image: photoTon2,
    alt: '',
    title: 'Lic Soft Velvet Foundation Mini version NEW',
    brand: '',
    description: '',
    detailsLink: 'https://goldapple.ru/19000167172-soft-velvet-foundation-mini-version-new'
  },
])
</script>

<style scoped>
.page-wrapper {
  width: 92%;
  display: flex;
  gap: 32px;
  flex-direction: column;
  padding-top: 20px;
  margin: 0 auto;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

main input {
  width: 100%;
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
}

.search p {
  margin: 0;
  color: #666;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
}
</style>
