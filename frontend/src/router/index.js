import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import WalletPage from '../views/WalletPage.vue'

const routes = [
  {
    path: '/',
    name: 'mainpage',
    component: MainPage
  },
  {
    path: '/wallet',
    name: 'wallet',
    component: WalletPage
  },
  {
    path: '/top',
    name: 'top',
    component: MainPage
  },
  {
    path: '/friends',
    name: 'friends',
    component: MainPage
  },
  {
    path: '/profile',
    name: 'profile',
    component: MainPage
  },
  {
    path: '/upgrade',
    name: 'upgrade',
    component: MainPage
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
