import { createRouter, createWebHistory } from 'vue-router'
import SignInComponent from '@/components/SignInComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
        path: '/',
        name: 'home',
        component: () => import('@/components/Home.vue')
      },
      {
        path: '/sign-in',
        name: 'sign-in',
        component: SignInComponent
      }
  ],
})

export default router
