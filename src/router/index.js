import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/main.vue'
import Registration from '@/views/registration.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/main',
      name: 'home',
      component: Main,
    },
    {
      path: '/registration',
      name: 'registartion',
      component: Registration,
    }
  ],
})

export default router
