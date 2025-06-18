<template>
  <div class="skin">
    <fieldset>
      <legend>Что из перечисленного у вас уже было?</legend>
      <div>
        <div>
          <input type="checkbox" id="allergy" name="allergy"/>
          <label for="allergy">Аллергия</label>
        </div>
        <div>
          <input type="checkbox" id="acne" name="acne" />
          <label for="acne">Акне</label>
        </div>
        <div>
          <input type="checkbox" id="dermatitis" name="dermatitis" />
          <label for="dermatitis">Дерматит</label>
        </div>
        <div>
          <input type="checkbox" id="peeling" name="peeling" />
          <label for="peeling">Шелушение кожи</label>
        </div>
        <div>
          <input type="checkbox" id="itch" name="itch" />
          <label for="itch">Зуд</label>
        </div>
        <div>
          <input type="checkbox" id="burn" name="burn" />
          <label for="burn">Жжение</label>
        </div>
        <div>
          <input type="checkbox" id="dryness" name="dryness" />
          <label for="dryness">Сухость</label>
        </div>
        <div>
          <input type="checkbox" id="pigment" name="pigment" />
          <label for="pigment">Пигментация</label>
        </div>
        <div>
          <input type="checkbox" id="nothing" name="nothing" />
          <label for="nothing">Ничего</label>
        </div>
      </div>
    </fieldset>
  </div>
</template>

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
  font-size: 16px;
  padding: 8px 12px;
  background-color: #FBFBFB;
  border-radius: 12px;
  cursor: pointer;
  transition: background-color 0.2s;
  user-select: none;
}
fieldset input[type="checkbox"]:checked + label {
  background-color: #000; /* Черный фон */
  color: #fff; /* Белый текст */
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
