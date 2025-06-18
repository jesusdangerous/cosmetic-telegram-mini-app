import { defineStore } from 'pinia'
import { useCookies } from 'vue3-cookies'

const { cookies } = useCookies()

export const useUserStore = defineStore('user', {
  state: () => ({
    name: cookies.get('userName') || '',
    email: '',
    phone: ''
  }),
  actions: {
    updateName(newName) {
      this.name = newName
      cookies.set('userName', newName, '30d')
    },
    clearUser() {
      this.name = ''
      this.email = ''
      this.phone = ''
      cookies.remove('userName')
    }
  }
})
