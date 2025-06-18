import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import Vue3Cookies from 'vue3-cookies'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)
app.use(createPinia())

const pinia = createPinia()

app.use(pinia)
app.use(router)
app.use(Vue3Cookies, {
  expireTimes: '30d',
  path: '/',
  domain: '',
  secure: true,
  sameSite: 'Lax'
})

app.config.globalProperties.$axios = axios

app.mount('#app')
