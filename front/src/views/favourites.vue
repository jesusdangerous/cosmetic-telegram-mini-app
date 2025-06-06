<template>
  <div class="page-wrapper">
    <header>
      <IconButton>
        <img src="@/assets/images/arrow-back.svg" alt="Назад" />
      </IconButton>
      <h1>Избранное</h1>
    </header>
    <main>
      <InputSearch placeholder="Поиск по избранному" />
      <div class="products-container">
        <CardMax
          v-for="product in products"
          :key="product.name"
          :product="product"
        />
      </div>
    </main>
  </div>
  <Footer></Footer>
</template>

<script setup>
import IconButton from '@/components/UI/IconButton.vue';
import InputSearch from '@/components/InputSearch.vue';
import CardMax from '@/components/CardMax.vue';
import Footer from '@/components/Footer.vue'
// Импорт картинок
import photoProduct from '../assets/images/photo-product.png';
import photoProduct2 from '../assets/images/photo-product-2.png'
const products = [
  {
    name: 'Крем для лица',
    brand: 'The Act с витамином C',
    safety: 89,
    ingredients:
      'Аgua (Water), Caprylic/Capric Triglyceride, Cetearyl Olivate, Sorbitan Olivate, Coco-Caprylate/Caprate, Glyc...',
    imageUrl: photoProduct,
    imageAlt: 'Крем для лица The Act'
  },
  {
    name: 'Рассыпчатые румяна для лица',
    brand: 'Belka mineral',
    safety: 100,
    ingredients:
      'Mica, Boron Nitride, Magnesium Stearate, [+/- Iron Oxides (77492, 77491), Manganese Violet (77742), Tit...',
    imageUrl: photoProduct2,
    imageAlt: 'Румяна Belka mineral'
  }
];
</script>

<style scoped>

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
.page-wrapper {
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 92%;
  padding: 20px 0;
}

header {
  display: flex;
  align-items: center;
}

h1 {
  margin: 0 auto;
}

.products-container {
  display: flex;
  flex-direction: column;
}
</style>
