import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/main.vue'
import Registration from '@/views/registration.vue'
import CheckNumber from '@/views/check-number.vue'
import MainPage from '@/views/main-page.vue'
import Support from '@/views/support.vue'
import UserAccount from '@/views/user-account.vue'
import WarningAccount from '@/views/warning-account.vue'
import WarningFavourites from '@/views/warning-favourites.vue'
import Favourites from '@/views/favourites.vue'

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
    },
    {
      path: '/main-page',
      name: 'main',
      component: MainPage,
    },
    {
      path: '/user-account',
      name: 'account',
      component: UserAccount,
    },
    {
      path: '/support',
      name: 'support',
      component: Support
    },
    {
      path: '/warning-account',
      name: 'warningAccount',
      component: WarningAccount,
    },
    {
      path: '/warning-favourites',
      name: "warningFavourites",
      component: WarningFavourites
    },
    {
      path: '/favourites',
      name: 'favourites',
      component: Favourites,
    }
  ],
})

export default router
