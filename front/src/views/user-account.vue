<template>
  <div class="page-wrapper">
    <header>
      <IconButton @click="goBack"><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Личный кабинет</h1>
    </header>
    <main>
      <article>
        <div class="data-user">
          <div>
            <img src="../assets/images/photo-user.svg">
            <div>
              <h2 v-if="!editMode">{{ userName }}</h2>
              <input v-else v-model="tempName" type="text" class="name-input">
              <p>+7 977 324 8982</p>
            </div>
          </div>
          <button @click="toggleEditMode">
            {{ editMode ? 'Сохранить' : 'Изменить' }}
          </button>
        </div>

        <div>
          <label class="message-input">Уведомления</label>
          <label class="checkbox-message">
            <input v-model="notificationsEnabled" type="checkbox">
            <span class="checkbox-message-switch"></span>
          </label>
        </div>

        <div>
          <p>Язык</p>
          <span>Русский</span>
        </div>

        <div @click="goToHistoryAnalysis" class="clickable-section">
          <p style="font-weight:bold;">История анализа</p>
          <IconButton><img class="arrow" src="../assets/images/arrow-back.svg"></IconButton>
        </div>

        <div>
          <p>Реакции: <span v-for="(reaction, index) in reactions" :key="'reaction-'+index">
            {{ reaction }}{{ index < reactions.length - 1 ? ', ' : '' }}
          </span></p>
          <button @click="showReactionsModal = true">Редактировать</button>
        </div>

        <div>
          <p>Аллергены: <span v-for="(allergen, index) in allergens" :key="'allergen-'+index">
            {{ allergen }}{{ index < allergens.length - 1 ? ', ' : '' }}
          </span></p>
          <button @click="showAllergensModal = true">Редактировать</button>
        </div>

        <div class="help clickable-section" @click="goToSupport">
          <p>Справка и поддержка</p>
          <IconButton><img class="arrow" src="../assets/images/arrow-back.svg"></IconButton>
        </div>

        <div class="exit clickable-section" @click="logout">
          <p>Выйти</p>
          <IconButton><img src="../assets/images/icon-exit.svg"></IconButton>
        </div>
      </article>
    </main>
    <Footer></Footer>

    <div v-if="showReactionsModal" class="modal">
      <div class="modal-content">
        <h3>Мои реакции</h3>
        <div class="input-group">
          <input v-model="newReaction" type="text" placeholder="Добавить реакцию" @keyup.enter="addReaction">
          <button @click="addReaction">+</button>
        </div>
        <ul>
          <li v-for="(reaction, index) in reactions" :key="index">
            {{ reaction }}
            <button @click="removeReaction(index)" class="remove-btn">×</button>
          </li>
        </ul>
        <div class="modal-buttons">
          <button @click="saveReactions" class="save-btn">Сохранить</button>
          <button @click="cancelReactions" class="cancel-btn">Отмена</button>
        </div>
      </div>
    </div>

    <div v-if="showAllergensModal" class="modal">
      <div class="modal-content">
        <h3>Мои аллергены</h3>
        <div class="input-group">
          <input v-model="newAllergen" type="text" placeholder="Добавить аллерген" @keyup.enter="addAllergen">
          <button @click="addAllergen">+</button>
        </div>
        <ul>
          <li v-for="(allergen, index) in allergens" :key="index">
            {{ allergen }}
            <button @click="removeAllergen(index)" class="remove-btn">×</button>
          </li>
        </ul>
        <div class="modal-buttons">
          <button @click="saveAllergens" class="save-btn">Сохранить</button>
          <button @click="cancelAllergens" class="cancel-btn">Отмена</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import IconButton from '@/components/UI/IconButton.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()
const userStore = useUserStore()

// Состояние пользователя
const userName = computed(() => userStore.name || 'Пользователь')
const tempName = ref('')
const editMode = ref(false)
const notificationsEnabled = ref(true)

// Реакции и аллергены
const reactions = ref([])
const allergens = ref([])
const showReactionsModal = ref(false)
const showAllergensModal = ref(false)
const newReaction = ref('')
const newAllergen = ref('')
const tempReactions = ref([])
const tempAllergens = ref([])

// Загрузка данных при монтировании
onMounted(() => {
  loadUserData()
})

const loadUserData = () => {
  // Загружаем реакции
  const savedReactions = localStorage.getItem('userReactions')
  if (savedReactions) reactions.value = JSON.parse(savedReactions)

  // Загружаем аллергены
  const savedAllergens = localStorage.getItem('userAllergens')
  if (savedAllergens) allergens.value = JSON.parse(savedAllergens)

  // Инициализируем временные данные
  tempReactions.value = [...reactions.value]
  tempAllergens.value = [...allergens.value]
}

const toggleEditMode = () => {
  if (editMode.value) {
    userStore.updateUser({ name: tempName.value })
  } else {
    tempName.value = userStore.name
  }
  editMode.value = !editMode.value
}

const goBack = () => {
  router.go(-1)
}

const goToSupport = () => {
  router.push('/support')
}

const goToHistoryAnalysis = () => {
  router.push('/history-analysis')
}

const logout = () => {
  userStore.clearUser()
  router.push('/login')
}

// Функции для работы с реакциями
const addReaction = () => {
  if (newReaction.value.trim()) {
    tempReactions.value.push(newReaction.value.trim())
    newReaction.value = ''
  }
}

const removeReaction = (index) => {
  tempReactions.value.splice(index, 1)
}

const saveReactions = () => {
  reactions.value = [...tempReactions.value]
  localStorage.setItem('userReactions', JSON.stringify(reactions.value))
  showReactionsModal.value = false
}

const cancelReactions = () => {
  tempReactions.value = [...reactions.value]
  showReactionsModal.value = false
}

// Функции для работы с аллергенами
const addAllergen = () => {
  if (newAllergen.value.trim()) {
    tempAllergens.value.push(newAllergen.value.trim())
    newAllergen.value = ''
  }
}

const removeAllergen = (index) => {
  tempAllergens.value.splice(index, 1)
}

const saveAllergens = () => {
  allergens.value = [...tempAllergens.value]
  localStorage.setItem('userAllergens', JSON.stringify(allergens.value))
  showAllergensModal.value = false
}

const cancelAllergens = () => {
  tempAllergens.value = [...allergens.value]
  showAllergensModal.value = false
}
</script>

<style scoped>
.exit {
  display: flex;
  width: 100%;
}

.arrow {
  transform: rotate(180deg);
}
.help p{
  font-weight: bold;
}
.checkbox-message {
  display: inline-block;
  height: 28px;
  line-height: 28px;
  margin-right: 10px;
  position: relative;
  vertical-align: middle;
  font-size: 14px;
  user-select: none;
  margin: 0;
}

.message-input {
  font-size: 16px;
  display: flex;
  align-items: center;
}

.checkbox-message .checkbox-message-switch {
  position: relative;
  display: inline-block;
  box-sizing: border-box;
  width: 56px;
  height: 28px;
  border: 1px solid rgba(0, 0, 0, .1);
  border-radius: 25%/50%;
  vertical-align: top;
  background: #eee;
  transition: .2s;
}
.checkbox-message .checkbox-message-switch:before {
  content: '';
  position: absolute;
  top: 1px;
  left: 1px;
  display: inline-block;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: white;
  box-shadow: 0 3px 5px rgba(0, 0, 0, .3);
  transition: .15s;
}
.checkbox-message input[type=checkbox] {
  display: block;
  width: 0;
  height: 0;
  position: absolute;
  z-index: -1;
  opacity: 0;
}
.checkbox-message input[type=checkbox]:not(:disabled):active + .checkbox-message-switch:before {
  box-shadow: inset 0 0 2px rgba(0, 0, 0, .3);
}
.checkbox-message input[type=checkbox]:checked + .checkbox-message-switch {
  background: rgba(163, 104, 240, 1);
}
.checkbox-message input[type=checkbox]:checked + .checkbox-message-switch:before {
  transform:translateX(28px);
}

/* Focus */
.checkbox-message.focused .checkbox-message-switch:before {
  box-shadow: inset 0px 0px 4px #ff5623;
}

/* Disabled */
.checkbox-message input[type=checkbox]:disabled + .checkbox-message-switch {
  filter: grayscale(70%);
  border-color: rgba(0, 0, 0, .1);
}
.checkbox-message input[type=checkbox]:disabled + .checkbox-message-switch:before {
  background: #eee;
}

.page-wrapper{
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 92%;
  margin: 0;
  padding: 20px 16px 114px 16px;
}

.data-user button {
  width: 29%;
  height: 36px;
  border-radius: 12px;
  border: 1px solid rgba(19, 19, 19, 1);
  background-color: transparent;
}

.data-user div {
  display: flex;
  gap: 12px;
}

article div {
  display: flex;
  justify-content: space-between;
}

article div button {
  border: none;
  font-weight: bold;
  background-color: transparent;
}

article div p {
  font-size: 16px;
}

.data-user div div {
  flex-direction: column;
  gap: 8px;
}

.data-user {
  display: flex;
  justify-content: space-between;
}

article {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

header {
  display: flex;
}

header button{
  width: 32px;
  padding: 8px !important;
}

header h1 {
  width: 87%;
  text-align: center;
}

.clickable-section {
  cursor: pointer;
}

.name-input {
  border: 1px solid #ccc;
  padding: 5px;
  border-radius: 4px;
  width: 100%;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 80%;
  max-width: 500px;
}

.modal-content ul {
  list-style: none;
  padding: 0;
  margin: 15px 0;
}

.modal-content li {
  display: flex;
  justify-content: space-between;
  padding: 5px 0;
  border-bottom: 1px solid #eee;
}

.modal-content button {
  margin: 5px;
  padding: 5px 10px;
}

div > p > span {
  font-weight: normal;
}

/* Стили для модальных окон */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 12px;
  width: 90%;
  max-width: 400px;
  max-height: 80vh;
  overflow-y: auto;
}

.input-group {
  display: flex;
  margin-bottom: 15px;
}

.input-group input {
  flex-grow: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 8px 0 0 8px;
}

.input-group button {
  padding: 8px 15px;
  background-color: #a368f0;
  color: white;
  border: none;
  border-radius: 0 8px 8px 0;
  cursor: pointer;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0 0 20px 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.remove-btn {
  background: none;
  border: none;
  color: #ff4444;
  font-size: 1.2em;
  cursor: pointer;
}

.modal-buttons {
  display: flex;
  gap: 10px;
}

.save-btn {
  flex-grow: 1;
  padding: 10px;
  background-color: #a368f0;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.cancel-btn {
  flex-grow: 1;
  padding: 10px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
</style>
