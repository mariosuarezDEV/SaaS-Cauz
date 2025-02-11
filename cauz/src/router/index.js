import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import SolicitudView from '@/views/SolicitudView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Inicio',
      component: IndexView,
    },
    {
      path: '/solicitud',
      name: 'Solicitud',
      component: SolicitudView,
    },
  ],
})

export default router
