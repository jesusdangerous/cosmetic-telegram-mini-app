<template>
  <div class="page-wrapper">
    <header>
      <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Поиск</h1>
    </header>
    <main>
      <div class="search">
        <InputSearch width="100%" placeholder="Поиск"></InputSearch>
        <IconButton><img src="../assets/images/icon-parameters.svg" alt="Иконка параметров"></IconButton>
      </div>
      <div class="ps">
        <p>
          Чтобы получить консультацию впервые, необходимо выбрать эксперта
        </p>
      </div>
      <div>
          <ExpertCard
            :expert="selectedExpert"
          />
      </div>
    </main>
  </div>
</template>

<script setup>
import IconButton from '@/components/UI/IconButton.vue';
import InputSearch from '@/components/InputSearch.vue';
import { ref } from 'vue'
import ExpertCard from '@/components/ExpertCard.vue'
import photoExpert from '@/assets/images/expert-1.jpg'

const selectedExpert = ref({
  name: 'Дмитрий',
  position: 'Врач-дерматолог',
  experience: '23 года',
  imageUrl: photoExpert,
  bioItems: [
    'Разработал уникальную методику терапии экземы, которая продемонстрировала 85% эффект',
  ]
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

.ps {
  width: 80%;
  margin: 0 auto;
}

.ps p{
  text-align: center;
  color: #545454;
}

header {
  display: flex;
  justify-content: space-between;
}

h1 {
  width: 87%;
  text-align: center;
}

.search {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
</style>
