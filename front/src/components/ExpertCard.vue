<template>
  <div class="expert-card">
    <div class="expert-card__header">
      <div>
        <h3 class="expert-card__position">{{ expert.position }}</h3>
        <h2 class="expert-card__name">{{ expert.name }}</h2>
      </div>
      <p class="expert-card__experience">Стаж работы: {{ expert.experience }}</p>
    </div>


    <div class="expert-card__image-wrapper" v-if="expert.imageUrl">
      <img
        :src="expert.imageUrl"
        :alt="`Фото ${expert.name}`"
        class="expert-card__image"
      >

      <p class="expert-card__bio" v-if="expert.bioItems">
        {{ expert.bioItems.join('. ') }}.
      </p>
    </div>
    <div class="card-button">
      <button class="expert-card__button" @click="emit('consult')">
        Получить консультацию
      </button>
    </div>
  </div>
</template>


<script setup>
const props = defineProps({
  expert: {
    type: Object,
    required: true,
    validator: (expert) => {
      return [
        'position',
        'experience',
        'name'
      ].every(prop => prop in expert)
    }
  }
})

const emit = defineEmits(['consult'])
</script>

<style scoped>
.expert-card {
  border: 1px solid #eaeaea;
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  gap: 8px;
  background-color: #FBFBFB;
}

h3 {
  color: #545454;
  font-size: 14px;
}

h2 {
  font-size: 1em;
}


.expert-card__image-wrapper {

  display: flex;
  gap: 12px;
}

.expert-card__image {
  width: 68px;
  height: 68px;
  object-fit: cover;
  object-position: center;
  border-radius: 50%;
}

.expert-card__header {
  display: flex;
  justify-content: space-between;
}


.expert-card__experience {
  display: flex;
  color: #A368F0;
  border: 1px solid #A368F0;
  border-radius: 16px;
  text-align: center;
  align-items: center;

  padding: 0 4px;
}

.expert-card__bio {
  color: #545454;
}

.expert-card__button {
  background-color: #131313;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 12px;
  width: 68%;
}

.card-button {

  display: flex;
  justify-content: flex-end;
}
</style>
