import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/main.vue'
import Registration from '@/views/registration.vue'
import CheckNumber from '@/views/check-number.vue'

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
    },
    {
      path: '/check-number',
      name: 'number',
      component: CheckNumber,
    }
  ],
})

export default router
