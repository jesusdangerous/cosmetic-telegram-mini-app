<template>
  <div class="page-wrapper">
    <a href="/main-page"><NavButton text="Пропустить"></NavButton></a>
    <div class="main">
      <header>
        <h1>Добро пожаловать!</h1>
        <h2>Введите свои данные для регистрации</h2>
      </header>
      <div class="data-user">
        <form ref="userForm" method="post" @submit="handleSubmit">
          <label>
            <Input v-model="name" placeholder="Имя" required></Input>
          </label>
          <label>
            <Input v-model="email" type="email" placeholder="Почта" required></Input>
          </label>
          <div class="checkbox">
            <div class="checkbox-wrapper">
              <input v-model="consent" type="checkbox" id="true-data" required>
              <label for="true-data">Даю согласие на обработку данных</label>
              <span v-if="showConsentError" class="error-message">Необходимо дать согласие</span>
            </div>
            <Button type="submit" text="Получить код" :disabled="!consent"></Button>
          </div>
        </form>
      </div>
    </div>
    <footer>
      <div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Input from '@/components/UI/Input.vue';
import Button from '@/components/UI/Button.vue';
import NavButton from '@/components/UI/NavButton.vue';
import { useUserStore } from '@/stores/user';

const router = useRouter();
const userStore = useUserStore();
const name = ref('');
const email = ref('');
const consent = ref(false);
const showConsentError = ref(false);

const handleSubmit = async (e) => {
  e.preventDefault();

  if (!consent.value) {
    showConsentError.value = true;
    return;
  }

  try {
    const response = await fetch('https://cosmetic-telegram-mini-app-3.onrender.com/api/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: name.value,
        email: email.value,
        dataProcessingConsent: consent.value
      })
    });

    const data = await response.json();

    if (data.success) {
      userStore.setUser({
        name: name.value,
        email: email.value
      });

      router.push({
        path: '/check-number',
        query: { email: email.value }
      });
    } else {
      alert(data.message);
    }
  } catch (error) {
    console.error('Registration error:', error);
    alert('Registration failed. Please try again.');
  }
};
</script>

<style scoped>
.page-wrapper {
  min-height: 600px;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding-top: 32px;
  justify-content: space-between;
  width: 92%;
}

.main {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.page-wrapper a {
  margin-left: 70%;
}

header {
  display: flex;
  flex-direction: column;
  color: rgba(19, 19, 19, 1);
  text-align: center;
  gap: 12px;
}

h1 {
  margin: 0;
  font-size: 32px;
}

h2 {
  font-size: 16px;
  margin: 0;
}

form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.data-user {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.checkbox {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.checkbox-wrapper {
  display: flex;
  flex-direction: row;
  gap: 4px;
}

.error-message {
  color: red;
  font-size: 12px;
  margin-top: 4px;
}

footer {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
