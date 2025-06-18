<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="user-account"><img src="../assets/images/arrow-back.svg"></IconButton>
      <h1>Справка и поддержка</h1>
    </header>
    <main>
      <article class="questions">
       <h2>FAQ</h2>
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
      </article>
      <article>
        <div class="politics">
          <h3>Политика конфиденциальности</h3>
          <IconButton><img src="../assets/images/arrow-back.svg"></IconButton>
        </div>
        <div class="support">
          <h3>Техподдержка</h3>
          <div>
            <p>С удовольствием поможем Вам с 8:00 до 18:00 (Мск)</p>
            <a href="#">Позвонить</a>
          </div>
        </div>
        <div class="feedback">
          <h3>Остались вопросы?</h3>
          <p>Если у вас возникли вопросы
              о работе нашего сервиса — напишите
              нам! Наша команда специалистов
              всегда рада помочь.</p>
          <div>
            <h4>Как к вам обращаться?</h4>
            <Input placeholder="Имя" v-model="feedback.name"></Input>
            <Input type="email" placeholder="Ваш email" v-model="feedback.email"></Input>
          </div>
          <div>
            <h4>Ваш вопрос</h4>
            <textarea placeholder="Вопросы, комментарии, предложения" v-model="feedback.question"></textarea>
            <Button text="Отправить" @click="submitFeedback"></Button>
          </div>
        </div>
      </article>
    </main>
    <Footer></Footer>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import Button from '@/components/UI/Button.vue';
  import Input from '@/components/UI/Input.vue';
  import IconButton from '@/components/UI/IconButton.vue';
  import Footer from '@/components/Footer.vue';
  const faqItems = ref([
    {
      question: 'Как проверить состав косметического средства?',
      answer: 'Здесь выпадающая информация!',
      isOpen: false
    },
    {
      question: 'Что такое безопасность?',
      answer: 'Здесь выпадающая информация!',
      isOpen: false
    }
  ]);

  const toggleDropdown = (index) => {
    faqItems.value[index].isOpen = !faqItems.value[index].isOpen;
  };

    const feedback = ref({
    name: '',
    email: '',
    question: ''
  });

  const submitFeedback = async () => {
    if (!feedback.value.email?.trim()) {
      alert("Пожалуйста, введите email");
      return;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(feedback.value.email)) {
      alert("Введите корректный email (например, user@example.com)");
      return;
    }

    if (!feedback.value.question.trim()) {
      alert("Пожалуйста, введите ваш вопрос");
      return;
    }

    try {
      const response = await fetch('/api/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: feedback.value.name,
          email: feedback.value.email,
          question: feedback.value.question
        })
      });

      const contentType = response.headers.get('content-type');
      let data;

      if (contentType && contentType.includes('application/json')) {
        data = await response.json();
      } else {
        const text = await response.text();
        throw new Error(`Unexpected response: ${text}`);
      }

      if (!response.ok) {
        alert(data.error || data.message || "Неизвестная ошибка");
        return;
      }

      feedback.value = { name: '', email: '', question: '' };

      if (data.emailSent) {
        alert('Спасибо! Ваше сообщение отправлено.');
      } else {
        alert('Сообщение сохранено, но не отправлено. Мы свяжемся с вами позже.');
      }
    } catch (error) {
      console.error('Ошибка при отправке:', error);
      alert('Ошибка сервера: ' + error.message);
    }
  };
</script>

<style scoped>
  .feedback {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .feedback div {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .feedback textarea {
    height: 120px;
    border: none;
    border-radius: 12px;
  }

  .feedback textarea::placeholder {
    padding: 16px 12px;
  }


  .feedback p {
    color: #545454;
    font-size: 14px;
  }
  .support {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .support div {
    display: flex;
    justify-content: space-between;
  }

  .support a {
    border: 1px solid black;
    border-radius: 12px;
    display: flex;
    padding: 8px;
    align-items: center;
  }

  .support p {
    width: 60%;
    color: #545454;
  }

  main {
    display: flex;
    flex-direction: column;
    gap: 24px;
    margin-bottom: 200px;
  }

  main article:last-child {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  .politics {
    display: flex;
    justify-content: space-between;
  }

  .politics img {
    transform: rotate(180deg);
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

  .page-wrapper {
    width: 92%;
    padding-top: 20px;
    gap: 32px;
  }

  header {
    width: 100%;
    display: flex;
  }

  header h1 {
    width: 87%;
    text-align: center;
  }

  .questions {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  main h2 {
    font-size: 20px;
  }
</style>
