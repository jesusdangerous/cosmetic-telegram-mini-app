<template>
  <div class="page-wrapper">
    <header>
      <IconButton href="/main-page"><img src="/images/arrow-back.svg"></IconButton>
      <h1>Сравнение составов</h1>
    </header>
    <main>
      <div class="ps">
        <p>Загрузите фото состава косметического средства или вставьте его текстом.</p>
      </div>
      <div class="compare">
        <h2>1 косметическое средство</h2>
        <div>
          <button @click="openGallery(1)" class="button" :class="{'button__ready': firstComposition.image, 'button__unready': !firstComposition.image}">
            <p>Фото состава</p>
            <img v-if="firstComposition.image" src="/images/icon-check.svg" alt="иконка галочки">
            <img v-else src="/images/icon-parameters.svg" alt="иконка параметров">
          </button>
          <button @click="showTextInput(1)" class="button" :class="{'button__ready': firstComposition.text, 'button__unready': !firstComposition.text}">
            <p>Текст состава</p>
            <img v-if="firstComposition.text" src="/images/icon-check.svg" alt="иконка галочки">
            <img v-else src="/images/icon-text.svg" alt="иконка текста">
          </button>
        </div>

        <h2>2 косметическое средство</h2>
        <div>
          <button @click="openGallery(2)" class="button" :class="{'button__ready': secondComposition.image, 'button__unready': !secondComposition.image}">
            <p>Фото состава</p>
            <img v-if="secondComposition.image" src="/images/icon-check.svg" alt="иконка галочки">
            <img v-else src="/images/icon-parameters.svg" alt="иконка параметров">
          </button>
          <button @click="showTextInput(2)" class="button" :class="{'button__ready': secondComposition.text, 'button__unready': !secondComposition.text}">
            <p>Текст состава</p>
            <img v-if="secondComposition.text" src="/images/icon-check.svg" alt="иконка галочки">
            <img v-else src="/images/icon-text.svg" alt="иконка текста">
          </button>
        </div>

        <button
          @click="compareCompositions"
          class="compare-button"
          :disabled="!canCompare"
        >
          Сравнить составы
        </button>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script setup>
  import IconButton from '@/components/UI/IconButton.vue';
  import Footer from '@/components/Footer.vue';
    import { ref, computed } from 'vue';
    import { useRouter } from 'vue-router';

    const router = useRouter();
    const firstComposition = ref({ image: null, text: '' });
    const secondComposition = ref({ image: null, text: '' });

    const canCompare = computed(() => {
    return (firstComposition.value.image || firstComposition.value.text) &&
    (secondComposition.value.image || secondComposition.value.text);
  });

    const openGallery = async (compositionNumber) => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = async (e) => {
    const file = e.target.files[0];
    if (file) {
    const formData = new FormData();
    formData.append('file', file);

    try {
    const response = await fetch('/api/analysis/image', {
    method: 'POST',
    body: formData
  });
    const result = await response.json();

    if (compositionNumber === 1) {
    firstComposition.value = { image: result, text: '' };
  } else {
    secondComposition.value = { image: result, text: '' };
  }
  } catch (error) {
    console.error('Error uploading image:', error);
  }
  }
  };
    input.click();
  };

    const showTextInput = (compositionNumber) => {
    const text = prompt('Введите состав косметического средства:');
    if (text) {
    if (compositionNumber === 1) {
    firstComposition.value = { image: null, text };
  } else {
    secondComposition.value = { image: null, text };
  }
  }
  };

    const compareCompositions = async () => {
    try {
    const response = await fetch('/api/analysis/compare', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json',
  },
    body: JSON.stringify({
    firstComposition: firstComposition.value.text || firstComposition.value.image.compositionText,
    secondComposition: secondComposition.value.text || secondComposition.value.image.compositionText
  })
  });
    const result = await response.json();
    router.push({
    path: '/analysis-result',
    state: { comparisonResult: result }
  });
  } catch (error) {
    console.error('Error comparing compositions:', error);
  }
  };
</script>

<style scoped>
.compare-button {
  margin-top: 20px;
  padding: 12px;
  background-color: #131313;
  color: white;
  border-radius: 12px;
  border: none;
  cursor: pointer;
}

.compare-button:disabled {
  background-color: #ADADAD;
  cursor: not-allowed;
}

  .compare {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .compare div {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  .button {
    width: 40%;
    display: flex;
    justify-content: space-between;
    border-radius: 12px;
    padding: 8px 12px;
  }
  .button__ready {
    border: 1px solid #131313;
  }
  .button__unready {
    border: 1px solid #ADADAD;
  }
  .button__unready p {
    color: #545454;
  }
  h2 {
    font-size: 20px;
  }
  h1 {
    width: 87%;
  }
  .page-wrapper {
    width: 92%;
    padding: 20px 0;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  main {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  header {
    display: flex;
    justify-content: space-between;
  }
</style>
