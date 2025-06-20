import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useFavoritesStore = defineStore('favorites', () => {
  const favorites = ref([])
  
  // Загрузка избранного из localStorage с обработкой ошибок
  const loadFavorites = () => {
    try {
      const stored = localStorage.getItem('favorites')
      if (stored) {
        favorites.value = JSON.parse(stored)
      }
    } catch (e) {
      console.error('Failed to parse favorites from localStorage', e)
      localStorage.removeItem('favorites') // Удаляем поврежденные данные
    }
  }

  // Инициализация при создании хранилища
  loadFavorites()

  // Проверка наличия товара в избранном по ID (более надежно, чем по name)
  const isFavorite = computed(() => (productId) => {
    return favorites.value.some(item => item.id === productId)
  })

  // Добавление в избранное с проверкой на дубликаты
  const addToFavorites = (product) => {
    if (!product || !product.id) return
    
    if (!favorites.value.some(item => item.id === product.id)) {
      favorites.value.push(product)
      saveToLocalStorage()
    }
  }

  // Удаление из избранного
  const removeFromFavorites = (productId) => {
    const newFavorites = favorites.value.filter(item => item.id !== productId)
    if (newFavorites.length !== favorites.value.length) {
      favorites.value = newFavorites
      saveToLocalStorage()
    }
  }

  // Сохранение с обработкой ошибок
  const saveToLocalStorage = () => {
    try {
      localStorage.setItem('favorites', JSON.stringify(favorites.value))
    } catch (e) {
      console.error('Failed to save favorites to localStorage', e)
    }
  }

  // Количество избранных товаров (может пригодиться для UI)
  const favoritesCount = computed(() => favorites.value.length)

  return { 
    favorites, 
    favoritesCount,
    addToFavorites, 
    removeFromFavorites, 
    isFavorite,
    loadFavorites
  }
})
