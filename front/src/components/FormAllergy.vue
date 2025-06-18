<template>
  <div class="skin">
    <fieldset>
      <legend>На что была выявлена аллергия?</legend>
      <div>
        <div>
          <input type="checkbox" id="paraben" name="paraben"/>
          <label for="paraben">Парабены</label>
        </div>
        <div>
          <input type="checkbox" id="aromatizer" name="aromatizer" />
          <label for="aromatizer">Ароматизаторы</label>
        </div>
        <div>
          <input type="checkbox" id="dye" name="dye" />
          <label for="dye">Красители</label>
        </div>
        <div>
          <input type="checkbox" id="sulfate" name="sulfate" />
          <label for="sulfate">Сульфаты</label>
        </div>
        <div>
          <input type="checkbox" id="oil" name="oil" />
          <label for="oil">Эфирные масла</label>
        </div>
        <div>
          <input type="checkbox" id="alcohol" name="alcohol" />
          <label for="alcohol">Алкоголь</label>
        </div>
        <div>
          <input type="checkbox" id="photosensitizer" name="photosensitizer" />
          <label for="photosensitizer">Фотосенсибилизаторы</label>
        </div>
        <div>
          <input type="checkbox" id="preservative" name="preservative" />
          <label for="preservative">Консерванты</label>
        </div>
        <div>
          <input type="checkbox" id="protein" name="protein" />
          <label for="protein">Протеины</label>
        </div>
        <div>
          <input type="checkbox" id="beekeeping" name="beekeeping" />
          <label for="beekeeping">Продукты пчеловодства</label>
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
  font-size: 14px;
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
