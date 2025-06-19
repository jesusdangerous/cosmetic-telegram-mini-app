<template>
  <div class="page-wrapper">
    <nav>
      <div>
        <IconButton><img src='/images/arrow-back.svg'></IconButton>
        <NavButton href="/registration" text="Назад"></NavButton>
      </div>
      <NavButton text="Пропустить"></NavButton>
    </nav>
    <div class="check-number">
      <header>
        <h1>Еще немного!</h1>
        <h2>Введите код из смс</h2>
      </header>
      <label>
        <Input v-model="code" placeholder="_ _ _ _"></Input>
      </label>
      <div class="buttons">
        <Button @click="verifyCode" text="Завершить регистрацию"></Button>
        <Button @click="resendCode" text="Отправить код повторно"></Button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import IconButton from '@/components/UI/IconButton.vue';
  import NavButton from '@/components/UI/NavButton.vue';
  import Input from '@/components/UI/Input.vue';
  import Button from '@/components/UI/Button.vue';

  const router = useRouter();
  const route = useRoute();
  const code = ref('');
  const email = ref(route.query.email || '');

  const verifyCode = async () => {
    if (!code.value) {
      alert('Пожалуйста, введите код подтверждения');
      return;
    }

    try {
      const response = await fetch('https://cosmetic-telegram-mini-app-3.onrender.com/api/auth/verify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email.value,
          code: code.value
        })
      });

      const data = await response.json();

      if (data.success) {
        alert('Регистрация успешно завершена!');
        router.push('/user-info');
      } else {
        alert(data.message || 'Ошибка при проверке кода');
      }
    } catch (error) {
      console.error('Ошибка при проверке кода:', error);
      alert('Произошла ошибка при проверке кода. Пожалуйста, попробуйте снова.');
    }
  };

  const resendCode = async () => {
    if (!email.value) {
      alert('Email не найден');
      return;
    }

    try {
      const response = await fetch(`https://cosmetic-telegram-mini-app-3.onrender.com/api/auth/resend-code?email=${encodeURIComponent(email.value)}`, {
        method: 'POST'
      });

      const data = await response.json();

      if (data.success) {
        alert('Новый код подтверждения отправлен на ваш email');
      } else {
        alert(data.message || 'Не удалось отправить код повторно');
      }
    } catch (error) {
      console.error('Ошибка при повторной отправке кода:', error);
      alert('Не удалось отправить код повторно. Пожалуйста, попробуйте позже.');
    }
  };
</script>

<style scoped>
  .page-wrapper {
    width: 100%;
    min-height: 486px;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding-top: 32px;
    justify-content: space-between;
  }

  nav {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }

  nav div {
    display: flex;
    gap: 8px;
    align-items: center;
  }

  .check-number {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  header {
    display: flex;
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }

  .buttons {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }


</style>
