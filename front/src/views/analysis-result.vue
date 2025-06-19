<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="/analysis"><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Результаты анализа</h1>
    </header>
    <main>
      <div class="product">
        <div class="product-header">
          <div class="product-category">
            <p>Шампунь для волос</p>
            <IconButton><img src="../assets/images/icon-like.svg"></IconButton>
          </div>
          <div class="product-name">
            <h2>HUMAN BEAUTY EVOLUTION DAILY USE</h2>
          </div>
        </div>

        <div class="product-info">
          <img src="../assets/images/photo-product-result.svg">
          <div class="product-info-text">
            <p>Безопасность {{ analysisResult.safetyScore }}%</p>
            <div>
              <div>
                <p>Область применения:</p>
                <span>{{ analysisResult.usageRecommendations.join(', ') }}</span>
              </div>
              <div v-if="analysisResult.skinTypeRecommendations.length">
                <p>Тип волос:</p>
                <span>{{ analysisResult.skinTypeRecommendations.join(', ') }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="text">
          <p>Безопасность состоит из аллергичности, токсичности и экологичности компонентов. В случае, когда безопасность составляет меньше 60%, то косметическое средство не является безопасным.</p>
        </div>

        <div class="structure">
          <h2>Состав</h2>
          <p>{{ analysisResult.components.map(c => c.name).join(', ') }}</p>
        </div>

        <div class="components">
          <h2>Происхождение компонентов</h2>
          <div>
            <img src="../assets/images/diagramm-components.svg">
            <div class="legent">
              <div>
                <p class="legent-item legent-item__natural"></p>
                <p>Природное {{ analysisResult.naturalPercentage }}%</p>
              </div>
              <div>
                <span class="legent-item legent-item__chemical"></span>
                <p>Химическое {{ analysisResult.chemicalPercentage }}%</p>
              </div>
            </div>
          </div>
        </div>

        <div class="components-info">
          <h2>О компонентах (INCI)</h2>
          <div class="components-info-main" v-for="(component, index) in displayedComponents" :key="index">
            <span class="components-info-safety" :style="{backgroundColor: getSafetyColor(component.safety)}">
              {{ component.safety }}
            </span>
            <p>{{ component.name }} — {{ component.type }}</p>
            <p>{{ component.benefits.join(', ') }}</p>
            <div class="components-info-facts">
              <p v-for="(fact, i) in component.facts" :key="i">{{ fact }}</p>
            </div>
          </div>

          <div class="components-info-view" @click="showAllComponents = !showAllComponents">
            <p>{{ showAllComponents ? 'Скрыть' : 'Показать все' }} компоненты</p>
            <IconButton>
              <img src="../assets/images/arrow-back.svg" :style="{transform: showAllComponents ? 'rotate(90deg)' : 'rotate(270deg)'}">
            </IconButton>
          </div>
        </div>

        <div class="recommendation">
          <h2>Рекомендации по использованию</h2>
          <div class="recommendation-items">
            <p class="recommendation-items-ps">Подходит тем, кто нуждается в следующем:</p>
            <div>
              <p v-for="(recommendation, idx) in analysisResult.usageRecommendations" :key="idx">{{ recommendation }}</p>
            </div>
          </div>
        </div>

        <div class="reviews">
          <div class="reviews-header">
            <h2>Отзывы</h2>
            <IconButton href="/reviews"><img src="../assets/images/arrow-back.svg"></IconButton>
          </div>
          <div class="reviews-info">
            <div>
              <img src="../assets/images/reviews-star.svg">
              <p>4,3</p>
            </div>
            <span>14 оценок</span>
          </div>
        </div>

        <div class="similar">
          <h1>Аналогичные продукты</h1>
          <ul class="cards">
            <li v-for="(product, index) in products" :key="index">
              <CardMini
                :image="product.image"
                :alt="product.alt"
                :title="product.title"
                :brand="product.brand"
                :description="product.description"
              />
            </li>
          </ul>
        </div>

        <div class="buttons">
          <a href="/experts" class="buttons-item buttons__consult">Консультация у эксперта</a>
          <a href="/main-page" class="buttons-item buttons__main">На главную</a>
        </div>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Footer from '@/components/Footer.vue';
import IconButton from '@/components/UI/IconButton.vue';
import CardMini from '@/components/CardMini.vue';
import photoProduct from '../assets/images/photo-product.svg';

const router = useRouter();
const showAllComponents = ref(false);
const products = ref([
  {
    image: photoProduct,
    alt: 'Крем для рук и тела LABORATORIUM Вишневый пирог',
    title: 'Крем для рук и тела',
    brand: 'LABORATORIUM',
    description: 'Вишневый пирог',
  }
]);

const analysisResult = ref({
  safetyScore: 89,
  naturalPercentage: 60,
  chemicalPercentage: 40,
  allergens: [],
  skinTypeRecommendations: ['Для всех типов волос'],
  usageRecommendations: [
    'Очищение',
    'Увлажнение кожи',
    'Антисептическое действие',
    'Смягчение кожи',
    'Успокоение кожи',
    'Улучшение структуры волос',
    'Лечение повреждений',
    'Кондиционирование волос'
  ],
  components: [
    {
      name: 'Arginine',
      type: 'действующее вещество',
      safety: 'Безопасно',
      benefits: ['Разглаживает волос', 'Хорошо влияет на корни волос'],
      facts: ['Аминокислота', 'Заживляет', 'Очищает кожу', 'Укрепляет сосуды']
    },
    // Добавьте другие компоненты по аналогии
  ]
});

const displayedComponents = computed(() => {
  return showAllComponents.value
    ? analysisResult.value.components
    : analysisResult.value.components.slice(0, 3);
});

const getSafetyColor = (safety) => {
  if (safety === 'Безопасно') return '#D0F068';
  if (safety === 'Умеренно') return '#FBA70A';
  return '#FF6B6B';
};

onMounted(() => {
  if (router.currentRoute.value.state?.analysisResult) {
    analysisResult.value = router.currentRoute.value.state.analysisResult;
  } else if (router.currentRoute.value.state?.comparisonResult) {
    const comparison = router.currentRoute.value.state.comparisonResult;
    analysisResult.value = {
      ...analysisResult.value,
      safetyScore: comparison.firstCompositionSafety,
    };
  }
});
</script>

<style scoped>
.buttons {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.buttons-item {
  display: block;
  border-radius: 12px;
  padding: 16px 0;
  text-align: center;
}
.buttons__consult {
  background-color: #131313;
  color: #FBFBFB;
}
.buttons__main {
  background-color: transparent;
  border: 1px solid #131313;
}
.similar {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.similar ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
.similar li {
  width: 53%;
}
.reviews {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.reviews-header {
  display: flex;
  justify-content: space-between;
}
.reviews-info {
  display: flex;
  gap: 12px;
}
.reviews-info span {
  color: #545454;
  font-size: 14px;
  display: flex;
  align-items: end;
}
.reviews-info div {
  display: flex;
  gap: 5px;
}
.reviews-header img {
  transform: rotate(180deg);
}
.recommendation-items-ps {
  color: #545454;
}
.recommendation {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.recommendation-items {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.recommendation-items div {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.recommendation-items div p {
  background-color: #A368F0;
  color: #FBFBFB;
  padding: 4px 12px;
  border-radius: 12px;
}
.components-info {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.components-info-view {
  display: flex;
  width: 65%;
  margin: 0 auto;
  justify-content: space-between;
}
.components-info-view img{
  transform: rotate(270deg);
}
.components-info-facts {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.components-info-facts {
  width: 92%;
  margin: 0 auto;
}
.components-info-main p{
  margin: 0 12px;
}
.components-info-facts p{
  border: 1px solid #A368F0;
  color: #A368F0;
  border-radius: 12px;
  padding: 4px 12px;
  margin: 0;
}
.components-info-main {
  display: flex;
  flex-direction: column;
  gap: 14px;
  border: 4px solid #D0F068;
  border-radius: 12px;
  padding: 0 0 12px;
}
.components-info-safety {
  width: 27%;
  background-color: #D0F068;
  border-radius: 9px;
  text-align: center;
  padding: 4px 12px;
}
.components {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.components div {
  display: flex;
  gap: 12px;
}
.legent {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.legent div {
  display: flex;
  gap: 4px;
}
.legent-item {
  width: 12px;
  height: 12px;
  margin-top: 3%;

  border-radius: 50%;
}
.legent-item__chemical {
  background-color: #FBA70A;
}
.legent-item__natural {
  background-color: #A368F0;
}
.structure p {
  background-color: #FBFBFB;
  padding: 12px 16px;
  border-radius: 12px;
}
.structure {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.product-info {
  display: flex;
  flex-direction: row;
  gap: 12px;
}
.product-info-text {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.product-info-text div {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.product-info div div {
  display: flex;
  gap: 4px;
}
.product-info div div p {
  color: #545454;
  background-color: transparent;
  text-align: start;
  padding: 0;
}
.product-info-text p {
  background-color: #D0F068;
  border-radius: 12px;
  padding: 4px 16px;
  text-align: center;
}
.product-info img {
  width: 144px;
  height: 144px;
}
.product-category {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 10px 0;
}
.product-category h2 {
  font-size: 20px;
}

.product-category p {
  color: #545454;
}
.product-header {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.product {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
header {
  display: flex;
  justify-content: space-between;
}
header h1 {
  width: 87%;
}
.page-wrapper {
  width: 92%;
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin-bottom: 400px;
}
main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
</style>
