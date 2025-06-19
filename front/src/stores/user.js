import { defineStore } from 'pinia'
import { useCookies } from 'vue3-cookies'

const { cookies } = useCookies()

export const useUserStore = defineStore('user', {
  state: () => ({
    name: cookies.get('userName') || '',
    email: cookies.get('userEmail') || '',
    phone: cookies.get('userPhone') || '',
    reactions: JSON.parse(cookies.get('userReactions') || '[]'),
    skinConditions: JSON.parse(cookies.get('userSkinConditions') || '[]'),
    cosmeticBrands: JSON.parse(cookies.get('userCosmeticBrands') || '[]'),
    allergens: JSON.parse(cookies.get('userAllergens') || '[]')
  }),
  actions: {
    setUser(userData) {
      this.name = userData.name
      this.email = userData.email
      this.phone = userData.phone || ''
      cookies.set('userName', userData.name, '30d')
      cookies.set('userEmail', userData.email, '30d')
      if (userData.phone) {
        cookies.set('userPhone', userData.phone, '30d')
      }
    },
    updateUser(newName) {
      this.name = newName
      cookies.set('userName', newName, '30d')
    },
    setReactions(reactions) {
      this.reactions = reactions
      cookies.set('userReactions', JSON.stringify(reactions), '30d')
    },
    setSkinConditions(conditions) {
      this.skinConditions = conditions
      cookies.set('userSkinConditions', JSON.stringify(conditions), '30d')
    },
    setCosmeticBrands(brands) {
      this.cosmeticBrands = brands
      cookies.set('userCosmeticBrands', JSON.stringify(brands), '30d')
    },
    setAllergens(allergens) {
      this.allergens = allergens
      cookies.set('userAllergens', JSON.stringify(allergens), '30d')
    },
    clearUser() {
      this.name = ''
      this.email = ''
      this.phone = ''
      this.reactions = []
      this.skinConditions = []
      this.cosmeticBrands = []
      this.allergens = []
      cookies.remove('userName')
      cookies.remove('userEmail')
      cookies.remove('userPhone')
      cookies.remove('userReactions')
      cookies.remove('userSkinConditions')
      cookies.remove('userCosmeticBrands')
      cookies.remove('userAllergens')
    }
  }
})
