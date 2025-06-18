<template>
  <div class="page-wrapper">
    <header>
      <IconButton @click="goBack">
        <img src="@/assets/images/arrow-back.svg" alt="Назад">
      </IconButton>
      <h1>Поиск</h1>
    </header>
    <main>
      <div class="search">
        <InputSearch width="100%" placeholder="Поиск" />
        <IconButton>
          <img src="@/assets/images/icon-parameters.svg" alt="Параметры">
        </IconButton>
      </div>
      <div class="ps">
        <p>Чтобы получить консультацию впервые, необходимо выбрать эксперта</p>
      </div>
      <div class="experts-container">
        <ExpertCard
          v-for="expert in experts"
          :key="expert.id"
          :expert="expert"
        />
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import IconButton from '@/components/UI/IconButton.vue'
import InputSearch from '@/components/InputSearch.vue'
import ExpertCard from '@/components/ExpertCard.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()

const experts = ref([
  {
    id: 1,
    name: 'Дмитрий',
    position: 'Врач-дерматолог',
    experience: '23 года',
    telegram: 'Z1nn4',
    imageUrl: new URL('@/assets/images/expert-1.jpg', import.meta.url).href,
    bioItems: [
      'Разработал уникальную методику терапии экземы',
      '85% успешных случаев лечения',
      'Специалист по сложным кожным заболеваниям'
    ]
  },
  {
    id: 2,
    name: 'Анна',
    position: 'Косметолог-эстетист',
    experience: '15 лет',
    telegram: 'veatmanz',
    imageUrl: new URL('@/assets/images/expert-2.jpg', import.meta.url).href,
    bioItems: [
      'Специалист по anti-age программам',
      'Эксперт по аппаратной косметологии',
      'Авторские методики омоложения'
    ]
  },
  {
    id: 3,
    name: 'Сергей',
    position: 'Трихолог',
    experience: '12 лет',
    telegram: 'ljopy',
    imageUrl: new URL('@/assets/images/expert-3.jpg', import.meta.url).href,
    bioItems: [
      'Эксперт по лечению выпадения волос',
      'Специалист по проблемам кожи головы',
      'Разработал 10+ эффективных протоколов'
    ]
  },
  {
    id: 4,
    name: 'Елена',
    position: 'Визажист',
    experience: '8 лет',
    telegram: 'whqsfasagd',
    imageUrl: new URL('@/assets/images/expert-4.jpg', import.meta.url).href,
    bioItems: [
      'Профессиональный макияж для любых случаев',
      'Коррекция черт лица',
      'Эксперт по wedding-образам'
    ]
  },
  {
    id: 5,
    name: 'Ольга',
    position: 'Эстетист',
    experience: '10 лет',
    telegram: 'LeB4uK',
    imageUrl: new URL('@/assets/images/expert-5.jpg', import.meta.url).href,
    bioItems: [
      'Специалист по уходу за проблемной кожей',
      'Эксперт по химическим пилингам',
      'Автор курсов по домашнему уходу'
    ]
  }
])

const goBack = () => {
  router.go(-1)
}
</script>

<style scoped>
.page-wrapper {
  width: 92%;
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin: 0 auto;
}

.ps {
  width: 80%;
  margin: 0 auto;
}

.ps p {
  text-align: center;
  color: #545454;
  font-size: 14px;
}

header {
  display: flex;
  align-items: center;
  gap: 16px;
}

h1 {
  flex-grow: 1;
  text-align: center;
  margin: 0;
  font-size: 20px;
}

.search {
  display: flex;
  gap: 8px;
  align-items: center;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.experts-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
