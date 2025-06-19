<template>
  <div class="skin">
    <fieldset>
      <legend>На что была выявлена аллергия?</legend>
      <div>
        <div v-for="allergen in allergens" :key="allergen.id">
          <input
            type="checkbox"
            :id="allergen.id"
            :name="allergen.id"
            :checked="isAllergenChecked(allergen.id)"
            @change="toggleAllergen(allergen.id)"
          />
          <label :for="allergen.id">{{ allergen.label }}</label>
        </div>
      </div>
    </fieldset>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const allergens = [
  { id: 'paraben', label: 'Парабены' },
  { id: 'aromatizer', label: 'Ароматизаторы' },
  { id: 'dye', label: 'Красители' },
  { id: 'sulfate', label: 'Сульфаты' },
  { id: 'oil', label: 'Эфирные масла' },
  { id: 'alcohol', label: 'Алкоголь' },
  { id: 'photosensitizer', label: 'Фотосенсибилизаторы' },
  { id: 'preservative', label: 'Консерванты' },
  { id: 'protein', label: 'Протеины' },
  { id: 'beekeeping', label: 'Продукты пчеловодства' }
]

const isAllergenChecked = (id) => {
  return userStore.allergens.includes(id)
}

const toggleAllergen = (id) => {
  const currentAllergens = [...userStore.allergens]
  const index = currentAllergens.indexOf(id)

  if (index === -1) {
    currentAllergens.push(id)
  } else {
    currentAllergens.splice(index, 1)
  }

  userStore.setAllergens(currentAllergens)
}
</script>

<style scoped>
legend {
  font-size: 20px;
  margin-bottom: 16px;
}
.purpose {
  display: flex;
  flex-direction: column;
  gap: 16px;
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
  font-size: 14px;
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
fieldset div:checked {
  background-color: black;
}
textarea {
  height: 100px;
  border-radius: 12px;
  border: none;
  padding: 12px 16px;
}
</style>
