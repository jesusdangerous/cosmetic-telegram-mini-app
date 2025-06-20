<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="/main-page">
        <img src="/images/arrow-back.svg" alt="Назад" />
      </IconButton>
      <h1>Избранное</h1>
    </header>
    <main>
      <InputSearch placeholder="Поиск по избранному" />
      <div v-if="favoritesStore.favorites.length > 0" class="products-container">
        <CardMini
          v-for="product in favoritesStore.favorites"
          :key="product.title"
          :image="product.image"
          :alt-text="product.altText"
          :title="product.title"
          :brand="product.brand"
          :description="product.description"
          :details-link="product.detailsLink"
        />
      </div>
      <div v-else class="empty-state">
        <p>В избранном пока ничего нет</p>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script setup>
import { useFavoritesStore } from '@/stores/favorites'
import IconButton from '@/components/UI/IconButton.vue'
import InputSearch from '@/components/InputSearch.vue'
import CardMini from '@/components/CardMini.vue'
import Footer from '@/components/Footer.vue'

const favoritesStore = useFavoritesStore()
</script>

<style scoped>
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
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
}

.empty-state {
  text-align: center;
  padding: 40px 0;
  color: #666;
}
</style>
