<template>
  <div class="page-wrapper">
    <nav>
      <a href="/main-page">Пропустить</a>
    </nav>
    <header>
      <h1>Расскажите нам немного о себе</h1>
      <p>Это сделает нашу совместную работу более эффективной </p>
    </header>
    <main>
      <div class="birth">
        <h2>Дата рождения</h2>
        <Input placeholder="__.__.____"/>
      </div>
      <div>
        <FormPurpose />
      </div>
      <div>
        <FormSkin @open-allergy-modal="isAllergyModalOpen = true"/>
      </div>
      <div class="brend">
        <h2>На какие бренды косметики уже была выявлена реакция?</h2>
        <div v-for="(item, index) in faqItems" :key="index" class="dropdown">
          <div class="question" @click="toggleDropdown(index)">
            <p>{{ item.question }}</p>
            <IconButton class="dropdown-button">
              <img
                src="../assets/images/arrow-back.svg"
                alt="иконка стрелочки"
                :style="{ transform: item.isOpen ? 'rotate(90deg)' : 'rotate(270deg)' }"
              >
            </IconButton>
          </div>
          <div class="dropdown-content" v-show="item.isOpen">
            <p>{{ item.answer }}</p>
          </div>
        </div>
      </div>
      <Button text="Сохранить"></Button>
    </main>
  </div>
</template>

<script setup>
import FormSkin from '@/components/FormSkin.vue';
import { ref } from 'vue';
import Input from '@/components/UI/Input.vue';
import Button from '@/components/UI/Button.vue';
import FormPurpose from '@/components/FormPurpose.vue';
import meet from './meet.vue';
const faqItems = ref([
  {
    question: 'Список брендов',
    answer: 'Здесь выпадающая информация!',
    isOpen: false
  }
]);

const toggleDropdown = (index) => {
  faqItems.value[index].isOpen = !faqItems.value[index].isOpen;
};

</script>

<style scoped>
.brend {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.question {
  display: flex;
  height: 40px;
  border-radius: 12px;
  align-items: center;
  justify-content: space-between;
  padding: 0 12px;
  cursor: pointer;
  padding: 8px;
}

.dropdown {
  position: relative;
  margin-bottom: 12px;
  border-radius: 12px;
  background-color: #FBFBFB;
}

.dropdown-button {
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

.dropdown p {
  width: 86%;
}

.dropdown-button img {
  width: 16px;
  height: 16px;
  transition: transform 0.3s ease;
  transform: rotate(270deg);
}

.dropdown-content {
  background-color: #f9f9f9;
  padding: 12px;
  border-radius: 0 0 12px 12px;
  margin-top: 4px;
}

.dropdown-content p {
  margin: 0;
}

.birth {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.birth h2 {
  font-size: 20px;
  font-weight: normal;
}
.page-wrapper {
  width: 92%;
  padding: 20px 0 372px;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

nav{
  display: flex;
  justify-content: flex-end;
}

header {
  display: flex;
  flex-direction: column;
  gap: 12px
}

h1 {
  text-align: center;
}

header p {
  color: #545454;
  text-align: center;
}

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
</style>
