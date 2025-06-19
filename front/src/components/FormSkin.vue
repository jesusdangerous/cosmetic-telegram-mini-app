<template>
  <div class="skin">
    <fieldset>
      <legend>Что из перечисленного у вас уже было?</legend>
      <div>
        <div v-for="condition in skinConditions" :key="condition.id">
          <input
            type="checkbox"
            :id="condition.id"
            :name="condition.id"
            v-model="condition.checked"
            @change="updateSelectedConditions"
          >
          <label :for="condition.id">{{ condition.label }}</label>
        </div>
      </div>
    </fieldset>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const skinConditions = ref([
  { id: 'allergy', label: 'Аллергия', checked: false },
  { id: 'acne', label: 'Акне', checked: false },
  { id: 'dermatitis', label: 'Дерматит', checked: false },
  { id: 'peeling', label: 'Шелушение кожи', checked: false },
  { id: 'itch', label: 'Зуд', checked: false },
  { id: 'burn', label: 'Жжение', checked: false },
  { id: 'dryness', label: 'Сухость', checked: false },
  { id: 'pigment', label: 'Пигментация', checked: false },
  { id: 'nothing', label: 'Ничего', checked: false }
])

onMounted(() => {
  // Загружаем сохраненные состояния
  const savedConditions = userStore.skinConditions
  if (savedConditions && savedConditions.length) {
    skinConditions.value = savedConditions
  }
})

const updateSelectedConditions = () => {
  const selectedConditions = skinConditions.value
    .filter(cond => cond.checked)
    .map(cond => cond.label)

  // Сохраняем в хранилище
  userStore.setSkinConditions(skinConditions.value)
  userStore.setReactions(selectedConditions)
}
</script>

<style scoped>
/* Стили остаются такими же */
legend {
  font-size: 20px;
  margin-bottom: 16px;
}
fieldset{
  border: none;
  padding: 0;
  margin: 0;
}
fieldset div {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
fieldset div div {
  display: flex;
  gap: 0;
}
fieldset label {
  display: inline-block;
  font-size: 16px;
  padding: 8px 12px;
  background-color: #FBFBFB;
  border-radius: 12px;
  cursor: pointer;
  transition: background-color 0.2s;
  user-select: none;
}
fieldset input[type="checkbox"]:checked + label {
  background-color: #000;
  color: #fff;
}
fieldset label:hover {
  background-color: #eee;
}
fieldset input {
  padding: 0;
  margin: 0;
  appearance: none;
}
</style>
