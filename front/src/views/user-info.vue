<template>
  <div class="page-wrapper">
    <!-- Навигация и заголовок из второго компонента -->
    <nav v-if="showNavigation">
      <a href="/main-page">Пропустить</a>
    </nav>

    <header v-if="showHeader">
      <h1>{{ headerTitle }}</h1>
      <p>{{ headerSubtitle }}</p>
    </header>

    <div class="user-info-container">
      <!-- Основной контент -->
      <h1 v-if="!showHeader">Настройки профиля</h1>

      <div class="user-form-section">
        <h2>Контактная информация</h2>
        <form @submit.prevent="saveUserInfo">
          <div class="form-group">
            <label for="name">Имя:</label>
            <input type="text" id="name" v-model="name" required>
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required>
          </div>
          <div class="form-group">
            <label for="phone">Телефон:</label>
            <input type="tel" id="phone" v-model="phone">
          </div>
          <div class="form-group" v-if="showBirthInput">
            <label>Дата рождения:</label>
            <Input placeholder="__.__.____" v-model="birthDate"/>
          </div>
          <button type="submit" class="save-btn">Сохранить</button>
        </form>
      </div>

      <div class="skin-conditions-section">
        <h2>Состояния кожи</h2>
        <FormSkin @open-allergy-modal="isAllergyModalOpen = true"/>
      </div>

      <div v-if="showPurposeForm">
        <FormPurpose />
      </div>



      <a v-if="showSaveButton" href="/meet" class="save-link">
        <Button text="Сохранить"></Button>
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import FormSkin from '@/components/FormSkin.vue'
import FormPurpose from '@/components/FormPurpose.vue'
import Input from '@/components/UI/Input.vue'
import Button from '@/components/UI/Button.vue'
import IconButton from '@/components/UI/IconButton.vue'

const userStore = useUserStore()

// Данные пользователя
const name = ref('')
const email = ref('')
const phone = ref('')
const birthDate = ref('')
const isAllergyModalOpen = ref(false)



// Параметры отображения
const showNavigation = ref(true)
const showHeader = ref(true)
const showBirthInput = ref(true)
const showPurposeForm = ref(true)
const showBrandsSection = ref(true)
const showSaveButton = ref(true)

const headerTitle = ref('Расскажите нам немного о себе')
const headerSubtitle = ref('Это сделает нашу совместную работу более эффективной')

onMounted(() => {
  // Загрузка данных пользователя
  name.value = userStore.name
  email.value = userStore.email
  phone.value = userStore.phone
})

const saveUserInfo = () => {
  userStore.setUser({
    name: name.value,
    email: email.value,
    phone: phone.value
  })
}

const toggleDropdown = (index) => {
  faqItems.value[index].isOpen = !faqItems.value[index].isOpen
}

// Вычисляемые свойства для реакций
const userReactions = computed(() => userStore.reactions)
</script>

<style scoped>
.page-wrapper {
  width: 92%;
  max-width: 1200px;
  padding: 20px 0;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.user-info-container {
  background: #fff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

nav {
  display: flex;
  justify-content: flex-end;
}

header {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

h1 {
  text-align: center;
  font-size: 24px;
  margin-bottom: 30px;
  color: #333;
}

header p {
  color: #545454;
  text-align: center;
}

.user-form-section, .skin-conditions-section {
  margin-bottom: 40px;
}

.user-form-section {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

label {
  display: block;
}

input {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
}

.save-btn {
  background: #333;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
}

.save-btn:hover {
  background: #555;
}

.save-link {
  display: block;
  margin-top: 20px;
}

/* Стили для брендов */
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

main {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
</style>
