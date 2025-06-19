<template>
  <div class="product-card">
    <div class="product-header">
      <div>
        <div>
          <h3 class="product-name">{{ product.name }}</h3>
          <p class="product-brand">{{ product.brand }}</p>
        </div>
          <IconButton><img src='/images/trashcan.svg'></IconButton>
      </div>

      <div class="safety-rating">
        <p>Безопасность: {{ product.safety }}%</p>
      </div>
    </div>

    <div class="product-content">
      <div class="product-image-container">
        <img
          :src="product.imageUrl"
          :alt="product.imageAlt || product.name"
          class="product-image"
          @error="handleImageError"
        />
      </div>
      <div class="ingredients">
        <p>{{ truncatedIngredients }}</p>
      </div>
    </div>
    <div class="analysis">
      <Button class="button-analysis" text="Результат анализа"></Button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import IconButton from './UI/IconButton.vue';
import Button from './UI/Button.vue';
// Импорт изображения по умолчанию
import defaultImage from '/images/photo-product.png';

const props = defineProps({
  product: {
    type: Object,
    required: true,
    validator: (value) => {
      return (
        'name' in value &&
        'brand' in value &&
        'safety' in value &&
        'ingredients' in value &&
        'imageUrl' in value
      );
    }
  },
  maxIngredientsLength: {
    type: Number,
    default: 100
  },
  defaultImage: {
    type: String,
    default: defaultImage
  }
});

const truncatedIngredients = computed(() => {
  if (props.product.ingredients.length > props.maxIngredientsLength) {
    return props.product.ingredients.substring(0, props.maxIngredientsLength) + '...';
  }
  return props.product.ingredients;
});

const handleImageError = (event) => {
  event.target.src = props.defaultImage;
};
</script>

<style scoped>
.product-card {
  background-color: #fff;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.product-image-container {
  width: 80px;
  height: 80px;
  flex-shrink: 0;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.product-content {
  display: flex;
  flex: 1;
  min-width: 0;
}

.product-header {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 8px;
}

.product-header div {
  display: flex;
  justify-content: space-between;

}

.product-header div div{
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.product-name {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  color: #333;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.product-brand {
  font-size: 14px;
  margin: 4px 0 0;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.safety-rating {
  background-color: #D0F068;
  border-radius: 12px;
  width: 45%;
  padding: 4px;
}

.safety-rating p {
  text-align: center;
  width: 100%;
}

.ingredients {
  margin: 12px 0;
  font-size: 13px;
  color: #555;
  line-height: 1.4;
}

.button-analysis {
  background-color: #131313;
  padding: 4px 0;
  color: white !important;
  width: 55%;
  height: 20%;
  font-weight: 400;
}

.analysis {
  display: flex;
  justify-content: end;
}
</style>
