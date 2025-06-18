<template>
  <div class="purpose">
    <fieldset>
      <legend>Цель использования сервиса</legend>
      <div>
        <div>
          <input type="checkbox" id="analysis" name="analysis"/>
          <label for="analysis">Анализ составов косметических средств</label>
        </div>
        <div>
          <input type="checkbox" id="support" name="support" />
          <label for="support">Поддержка здорового образа жизни</label>
        </div>
        <div>
          <input type="checkbox" id="communication" name="communication" />
          <label for="communication">Общение с экспертом</label>
        </div>
        <div>
          <input type="checkbox" id="skin" name="skin" />
          <label for="skin">Улучшить состояние кожи</label>
        </div>
        <div>
          <input type="checkbox" id="compare" name="compare" />
          <label for="compare">Сравнение составов косметических средств</label>
        </div>
        <div>
          <input type="checkbox" id="other" name="other" />
          <label for="other">Другое</label>
        </div>
        <textarea placeholder="Напишите вашу цель"></textarea>
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
  flex-direction: column;
  gap: 20px;
}
fieldset div div {
  display: flex;
  flex-direction: row;
  gap: 8px;
}
fieldset label {
  font-size: 14px;
}
fieldset input {
  padding: 0;
  margin: 0;
}
fieldset input:checked {
  accent-color: black;
}
textarea {
  height: 100px;
  border-radius: 12px;
  border: none;
  padding: 12px 16px;
}
</style>
