import { fileURLToPath, URL } from 'node:url'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: parseInt(process.env.PORT) || 3000,
    host: true,
  },
  preview: {
    port: parseInt(process.env.PORT) || 3000,
    allowedHosts: ['cosmetic-telegram-mini-app.onrender.com']
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  plugins: [vue()], // Добавьте плагин здесь
  server: {
    port: 3000,
    host: true
  }
});
