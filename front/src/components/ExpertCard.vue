<template>
  <div class="expert-card">
    <div class="expert-card__header">
      <div>
        <h3 class="expert-card__position">{{ expert.position }}</h3>
        <router-link
          :to="'/expert' + expert.id"
          class="expert-card__name"
        >
          {{ expert.name }}
        </router-link>
      </div>
      <router-link
        :to="'/expert' + expert.id"
        class="expert-card__experience"
      >
        Стаж работы: {{ expert.experience }}
      </router-link>
    </div>

    <router-link
      :to="'/expert' + expert.id"
      class="expert-card__image-wrapper"
      v-if="expert.imageUrl"
    >
      <img
        :src="expert.imageUrl"
        :alt="`Фото ${expert.name}`"
        class="expert-card__image"
      >
      <p class="expert-card__bio" v-if="expert.bioItems">
        {{ expert.bioItems.join('. ') }}.
      </p>
    </router-link>
    <div class="card-button">
      <button
        class="expert-card__button"
        @click="openTelegram"
      >
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
        'name',
        'telegram',
        'id'
      ].every(prop => prop in expert)
    }
  }
})

const openTelegram = (e) => {
  e.stopPropagation()
  const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)

  if (isMobile) {
    window.location.href = `tg://resolve?domain=${props.expert.telegram}`
    setTimeout(() => {
      window.open(`https://t.me/${props.expert.telegram}`, '_blank')
    }, 2000)
  } else {
    window.open(`https://t.me/${props.expert.telegram}`, '_blank')
  }
}
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
  position: relative;
}

h3 {
  color: #545454;
  font-size: 14px;
  margin: 0;
}

.expert-card__name {
  font-size: 1em;
  color: inherit;
  text-decoration: none;
  display: block;
}

.expert-card__image-wrapper {
  display: flex;
  gap: 12px;
  text-decoration: none;
  color: inherit;
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
  align-items: center;
}

.expert-card__experience {
  display: flex;
  color: #A368F0;
  border: 1px solid #A368F0;
  border-radius: 16px;
  text-align: center;
  align-items: center;
  padding: 4px 8px;
  font-size: 12px;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s;
}

.expert-card__experience:hover {
  background-color: #A368F0;
  color: white;
}

.expert-card__bio {
  color: #545454;
  font-size: 14px;
  margin: 0;
}

.expert-card__button {
  background-color: #131313;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 12px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
  z-index: 2;
  position: relative;
}

.expert-card__button:hover {
  background-color: #333;
}

.card-button {
  display: flex;
  justify-content: flex-end;
}
</style>
