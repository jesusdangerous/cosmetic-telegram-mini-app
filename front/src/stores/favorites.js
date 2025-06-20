import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useFavoritesStore = defineStore('favorites', () => {
  const favorites = ref([])

  // Загрузка из localStorage
  const loadFavorites = () => {
    const saved = localStorage.getItem('favorites')
    if (saved) {
      favorites.value = JSON.parse(saved)
    }
  }

  // Сохранение в localStorage
  const saveFavorites = () => {
    localStorage.setItem('favorites', JSON.stringify(favorites.value))
  }

  // Проверка наличия по title
  const isFavorite = (title) => {
    return favorites.value.some(item => item.title === title)
  }

  // Добавление в избранное
  const addFavorite = (product) => {
    if (!isFavorite(product.title)) {
      favorites.value.push(product)
      saveFavorites()
    }
  }

  // Удаление из избранного
  const removeFavorite = (title) => {
    favorites.value = favorites.value.filter(item => item.title !== title)
    saveFavorites()
  }

  // Переключение состояния
  const toggleFavorite = (product) => {
    if (isFavorite(product.title)) {
      removeFavorite(product.title)
    } else {
      addFavorite(product)
    }
  }

  // Инициализация
  loadFavorites()

  return {
    favorites,
    isFavorite,
    addFavorite,
    removeFavorite,
    toggleFavorite
  }
})
