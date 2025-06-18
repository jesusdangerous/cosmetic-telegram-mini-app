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
            <Input v-model="name" placeholder="Имя"></Input>
          </label>
          <label>
            <Input v-model="email" type="email" placeholder="Почта"></Input>
          </label>
          <div class="checkbox">
            <div>
              <input v-model="consent" type="checkbox" id="true-data">
              <label for="true-data">Даю согласие на обработку данных</label>
            </div>
            <Button type="submit" text="Получить код"></Button>
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
  import IconButton from '@/components/UI/IconButton.vue';
  import NavButton from '@/components/UI/NavButton.vue';

  const router = useRouter();
  const name = ref('');
  const email = ref('');
  const consent = ref(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8080/api/auth/register', {
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
  }

  .skip-button {
    border: none;
    background-color: transparent;
  }

  .main {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  button {
    margin-left: auto;
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

  footer {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  footer p {
    margin: 0;
    text-align: center;
  }

  footer div {
    display: flex;
    gap: 16px;
  }
</style>
