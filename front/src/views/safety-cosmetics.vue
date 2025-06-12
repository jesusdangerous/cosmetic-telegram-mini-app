<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="main-page">
        <img src="../assets/images/arrow-back.svg" />
      </IconButton>
      <h1>Безопасная косметика</h1>
    </header>
    <main>
      <InputSearch width="100%" />
      <div class="category">
        <ButtonCategory :categories="categories" v-model="selectedCategory" />
      </div>
      <div class="search">
        <p>Найдено 2 косметических средства</p>
      </div>
      <div class="cards">
          <CardMini
            v-for="(product, index) in products"
            :key="index"
            :image="product.image"
            :alt="product.alt"
            :title="product.title"
            :brand="product.brand"
            :description="product.description"
          />

      </div>
    </main>
  </div>
</template>

<script setup>
import InputSearch from '@/components/InputSearch.vue'
import IconButton from '@/components/UI/IconButton.vue'
import ButtonCategory from '@/components/UI/ButtonCategory.vue'
import CardMini from '@/components/CardMini.vue'
import { ref } from 'vue'

import photoCream from '@/assets/images/cream.svg'
import photoShampoo from '@/assets/images/shampoo.svg'
import photoLip from '@/assets/images/lip.svg'

import photoProduct from '@/assets/images/photo-product.svg';
import photoProduct3 from '@/assets/images/photo-product-3.svg';
const categories = [
  { name: 'Крема', img: photoCream, alt: 'Крем' },
  { name: 'Шампуни', img: photoShampoo, alt: 'Шампунь' },
  { name: 'Помады', img: photoLip, alt: 'Помада' },
]

const selectedCategory = ref(null)

const products = ref([
  {
    image: photoProduct,
    alt: 'Крем для рук и тела LABORATORIUM Вишневый пирог',
    title: 'Крем для рук и тела',
    brand: 'LABORATORIUM',
    description: 'Вишневый пирог',
  },
  {
    image: photoProduct3,
    alt: 'Крем для лица The Act с витамином C',
    title: 'Крем для лица',
    brand: 'The Act',
    description: 'с витамином C',
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
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

main input{
  width: 100% !important;
}


header {
  width: 100%;
  display: flex;

}

header h1 {
  width: 87%;
  text-align: center;
}

.cards {
  display: flex;
  gap: 12px;
}

</style>
