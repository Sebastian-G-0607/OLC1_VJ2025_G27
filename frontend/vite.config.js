import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    proxy: {
      '/api': { //este es el prefijo que se le pone a la URL y tiene que coincidir con el del backend
        target: 'http://localhost:4000', // URL CONFIGURACIÓN DOCKER
        changeOrigin: true,
      },
    }
  }
})
