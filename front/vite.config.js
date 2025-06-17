import { fileURLToPath, URL } from 'node:url'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: 3000,
    host: true,
  },
  preview: {
    port: isNaN(parseInt(process.env.PORT)) ? 3000 : parseInt(process.env.PORT),
    host: true,
    allowedHosts: ['cosmetic-telegram-mini-app.onrender.com']
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  plugins: [vue()],
});
