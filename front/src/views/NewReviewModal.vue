<template>
  <div class="review-modal">
    <h2>Оставить отзыв</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label>Ваше имя</label>
        <input v-model="formData.userName" required maxlength="100">
      </div>

      <div class="form-group">
        <label>Оценка</label>
        <select v-model.number="formData.rating" required>
          <option :value="5">5 - Отлично</option>
          <option :value="4">4 - Хорошо</option>
          <option :value="3">3 - Удовлетворительно</option>
          <option :value="2">2 - Плохо</option>
          <option :value="1">1 - Ужасно</option>
        </select>
      </div>

      <div class="form-group">
        <label>Достоинства</label>
        <textarea v-model="formData.pros" required maxlength="500"></textarea>
      </div>

      <div class="form-group">
        <label>Недостатки</label>
        <textarea v-model="formData.cons" required maxlength="500"></textarea>
      </div>

      <div class="buttons">
        <button type="button" @click="cancel">Отмена</button>
        <button type="submit">Отправить</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['submit-review', 'cancel'])

const formData = ref({
  userName: '',
  rating: 5,
  pros: '',
  cons: ''
})

const isSubmitting = ref(false)
const errorMessage = ref('')

const validateForm = () => {
  if (!formData.value.userName.trim()) {
    errorMessage.value = 'Пожалуйста, укажите ваше имя'
    return false
  }
  if (!formData.value.pros.trim()) {
    errorMessage.value = 'Пожалуйста, укажите достоинства'
    return false
  }
  if (!formData.value.cons.trim()) {
    errorMessage.value = 'Пожалуйста, укажите недостатки'
    return false
  }
  errorMessage.value = ''
  return true
}

const submitForm = async () => {
  if (!validateForm()) return

  isSubmitting.value = true

  try {
    const reviewData = {
      ...formData.value,
      userName: formData.value.userName.trim(),
      pros: formData.value.pros.trim(),
      cons: formData.value.cons.trim()
    }

    emit('submit-review', reviewData)

    // Сброс формы после успешной отправки
    formData.value = {
      userName: '',
      rating: 5,
      pros: '',
      cons: ''
    }

  } catch (error) {
    console.error('Ошибка при отправке отзыва:', error)
    errorMessage.value = 'Произошла ошибка при отправке отзыва'
  } finally {
    isSubmitting.value = false
  }
}

const cancel = () => {
  emit('cancel')
}
</script>

<style scoped>
.review-modal {
  background: white;
  padding: 20px;
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
}

.review-modal h2 {
  margin-top: 0;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-group textarea {
  height: 80px;
  resize: vertical;
}

.buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.buttons button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.buttons button:first-child {
  background: #f0f0f0;
}

.buttons button:last-child {
  background: #007BFF;
  color: white;
}
</style>
