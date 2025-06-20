<template>
  <div class="page-wrapper">
    <header>
      <IconButton @click="goBack"><img src="/images/arrow-back.svg"></IconButton>
      <h1>Личный кабинет</h1>
    </header>
    <main>
      <article>
        <div class="data-user">
          <div>
            <img src="/images/photo-user.svg">
            <div>
              <h2 v-if="!editMode">{{ userName || 'Пользователь' }}</h2>
              <input v-else v-model="tempName" type="text" class="name-input">
              <p><strong>Email:</strong> {{ userEmail || 'Не указан' }}</p>
              <p><strong>Телефон:</strong> {{ userPhone || 'Не указан' }}</p>
            </div>
          </div>
          <button @click="toggleEditMode">
            {{ editMode ? 'Сохранить' : 'Изменить' }}
          </button>
        </div>

        <div class="notification-section">
          <label class="message-input">Уведомления</label>
          <label class="checkbox-message">
            <input v-model="notificationsEnabled" type="checkbox">
            <span class="checkbox-message-switch"></span>
          </label>
        </div>

        <div class="language-section">
          <p>Язык</p>
          <span>Русский</span>
        </div>

        <div @click="goToHistoryAnalysis" class="clickable-section">
          <p style="font-weight:bold;">История анализа</p>
          <IconButton><img class="arrow" src="/images/arrow-back.svg"></IconButton>
        </div>

        <div class="reactions-section">
          <p><strong>Реакции:</strong>
            <span v-if="userReactions.length">
              <span v-for="(reaction, index) in userReactions" :key="'reaction-'+index">
                {{ reaction }}{{ index < userReactions.length - 1 ? ', ' : '' }}
              </span>
            </span>
            <span v-else>Нет сохраненных реакций</span>
          </p>
          <button @click="showReactionsModal = true">Редактировать</button>
        </div>

        <div class="allergens-section">
          <p><strong>Аллергены:</strong>
            <span v-if="formattedAllergens.length">
              <span v-for="(allergen, index) in formattedAllergens" :key="'allergen-'+index">
                {{ allergen }}{{ index < formattedAllergens.length - 1 ? ', ' : '' }}
              </span>
            </span>
            <span v-else>Нет сохраненных аллергенов</span>
          </p>
          <button @click="showAllergensModal = true">Редактировать</button>
        </div>

        <div class="help clickable-section" @click="goToSupport">
          <p>Справка и поддержка</p>
          <IconButton><img class="arrow" src="/images/arrow-back.svg"></IconButton>
        </div>

        <div class="exit clickable-section" @click="logout">
          <p>Выйти</p>
          <IconButton><img src="/images/icon-exit.svg"></IconButton>
        </div>
      </article>
    </main>
    <Footer></Footer>

    <!-- Модальное окно редактирования профиля -->
    <div v-if="showEditModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showEditModal = false">&times;</span>
        <h2>Редактировать профиль</h2>
        <form @submit.prevent="saveProfile">
          <div class="form-group">
            <label for="name">Имя:</label>
            <input type="text" id="name" v-model="editName" required>
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="editEmail" required>
          </div>
          <div class="form-group">
            <label for="phone">Телефон:</label>
            <input type="tel" id="phone" v-model="editPhone">
          </div>
          <button type="submit" class="save-btn">Сохранить</button>
        </form>
      </div>
    </div>

    <!-- Модальное окно редактирования реакций -->
    <div v-if="showReactionsModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showReactionsModal = false">&times;</span>
        <h2>Редактировать реакции</h2>
        <div class="input-group">
          <input v-model="newReaction" type="text" placeholder="Добавить реакцию" @keyup.enter="addReaction">
          <button @click="addReaction">+</button>
        </div>
        <ul>
          <li v-for="(reaction, index) in tempReactions" :key="index">
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

    <!-- Модальное окно редактирования аллергенов -->
    <div v-if="showAllergensModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showAllergensModal = false">&times;</span>
        <h2>Редактировать аллергены</h2>
        <FormAllergy />
        <div class="input-group">
          <input v-model="newAllergen" type="text" placeholder="Добавить другой аллерген" @keyup.enter="addAllergen">
          <button @click="addAllergen">+</button>
        </div>
        <ul>
          <li v-for="(allergen, index) in customAllergens" :key="index">
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
import FormAllergy from '@/components/FormAllergy.vue'

const router = useRouter()
const userStore = useUserStore()

// Состояние пользователя
const userName = computed(() => userStore.name)
const userEmail = computed(() => userStore.email)
const userPhone = computed(() => userStore.phone)
const userReactions = computed(() => userStore.reactions || [])
const userAllergens = computed(() => userStore.allergens || [])
const tempName = ref('')
const editMode = ref(false)
const notificationsEnabled = ref(true)
const customAllergens = ref([])

const formattedAllergens = computed(() => {
  const allergenLabels = {
    paraben: 'Парабены',
    aromatizer: 'Ароматизаторы',
    dye: 'Красители',
    sulfate: 'Сульфаты',
    oil: 'Эфирные масла',
    alcohol: 'Алкоголь',
    photosensitizer: 'Фотосенсибилизаторы',
    preservative: 'Консерванты',
    protein: 'Протеины',
    beekeeping: 'Продукты пчеловодства'
  }

  return [
    ...userAllergens.value.map(id => allergenLabels[id] || id),
    ...customAllergens.value
  ]
})

// Редактирование профиля
const showEditModal = ref(false)
const editName = ref('')
const editEmail = ref('')
const editPhone = ref('')

// Реакции и аллергены
const showReactionsModal = ref(false)
const showAllergensModal = ref(false)
const newReaction = ref('')
const newAllergen = ref('')
const tempReactions = ref([])
const tempAllergens = ref([])

// Загрузка данных при монтировании
onMounted(() => {
  loadUserData()
  editName.value = userStore.name
  editEmail.value = userStore.email
  editPhone.value = userStore.phone

  // Загружаем кастомные аллергены (те, которые не входят в стандартный список)
  const standardAllergens = ['paraben', 'aromatizer', 'dye', 'sulfate', 'oil',
    'alcohol', 'photosensitizer', 'preservative', 'protein', 'beekeeping']
  customAllergens.value = userStore.allergens.filter(
    allergen => !standardAllergens.includes(allergen))
})

const loadUserData = () => {
  tempReactions.value = [...userReactions.value]
  tempAllergens.value = [...userAllergens.value]
}

const toggleEditMode = () => {
  if (editMode.value) {
    showEditModal.value = true
  } else {
    tempName.value = userStore.name
  }
  editMode.value = !editMode.value
}

const saveProfile = () => {
  userStore.setUser({
    name: editName.value,
    email: editEmail.value,
    phone: editPhone.value
  })
  showEditModal.value = false
  editMode.value = false
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
  userStore.setReactions(tempReactions.value)
  showReactionsModal.value = false
}

const cancelReactions = () => {
  tempReactions.value = [...userReactions.value]
  showReactionsModal.value = false
}

// Функции для работы с аллергенами
const addAllergen = () => {
  if (newAllergen.value.trim()) {
    customAllergens.value.push(newAllergen.value.trim())
    newAllergen.value = ''
  }
}

const removeAllergen = (index) => {
  customAllergens.value.splice(index, 1)
}

const saveAllergens = () => {
  const allAllergens = [...userStore.allergens.filter(id => {
    const standardAllergens = ['paraben', 'aromatizer', 'dye', 'sulfate', 'oil',
      'alcohol', 'photosensitizer', 'preservative', 'protein', 'beekeeping']
    return standardAllergens.includes(id)
  }), ...customAllergens.value]

  userStore.setAllergens(allAllergens)
  showAllergensModal.value = false
}

const cancelAllergens = () => {
  const standardAllergens = ['paraben', 'aromatizer', 'dye', 'sulfate', 'oil',
    'alcohol', 'photosensitizer', 'preservative', 'protein', 'beekeeping']
  customAllergens.value = userStore.allergens.filter(
    allergen => !standardAllergens.includes(allergen))
  showAllergensModal.value = false
}
</script>

<style scoped>
.page-wrapper {
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 92%;
  margin: 0;
  padding: 20px 16px 114px 16px;
}

header {
  display: flex;
  align-items: center;
}

header h1 {
  width: 100%;
  text-align: center;
}

.data-user {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
}

.data-user > div {
  display: flex;
  gap: 16px;
}

.data-user img {
  width: 64px;
  height: 64px;
  border-radius: 50%;
}

.data-user h2 {
  font-size: 18px;
  margin: 0 0 4px 0;
}

.data-user p {
  margin: 4px 0;
  font-size: 14px;
  color: #666;
}

.data-user button {
  padding: 8px 16px;
  background: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
}

.notification-section,
.language-section,
.reactions-section,
.allergens-section,
.help,
.exit {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #eee;
}

.clickable-section {
  cursor: pointer;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.name-input {
  border: 1px solid #ccc;
  padding: 8px;
  border-radius: 4px;
  width: 100%;
  font-size: 18px;
}

/* Стили для чекбокса уведомлений */
.checkbox-message {
  display: inline-block;
  height: 28px;
  line-height: 28px;
  position: relative;
  vertical-align: middle;
  user-select: none;
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

.checkbox-message input[type=checkbox]:checked + .checkbox-message-switch {
  background: rgba(163, 104, 240, 1);
}

.checkbox-message input[type=checkbox]:checked + .checkbox-message-switch:before {
  transform: translateX(28px);
}

.arrow {
  transform: rotate(180deg);
}

/* Модальные окна */
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
  position: relative;
}

.close {
  position: absolute;
  right: 20px;
  top: 10px;
  font-size: 24px;
  cursor: pointer;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
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

strong {
  font-weight: bold;
}
</style>
