import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import WalletPage from '../views/WalletPage.vue'
import UpgradePage from '../views/UpgradePage.vue'
import BoostPage from '../views/BoostPage.vue'
import ProfilePage from '../views/ProfilePage.vue'
import TaskPage from '../views/TaskPage.vue'
import FriendsPage from '../views/FriendsPage.vue'
import TopPage from '../views/TopPage.vue'
import RanksPage from '../views/RanksPage.vue'
import PlayerPage from '../views/PlayerPage.vue'
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
    path: '/task',
    name: 'task',
    component: TaskPage
  },
  {
    path: '/top',
    name: 'top',
    component: TopPage
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage
  },
  {
    path: '/upgrade',
    name: 'upgrade',
    component: UpgradePage
  },
  {
    path: '/boost',
    name: 'boost',
    component: BoostPage
  },
  {
    path: '/friends',
    name: 'friends',
    component: FriendsPage
  },
  {
    path: '/ranks',
    name: 'ranks',
    component: RanksPage
  },
  {
    path: '/player/:userId',
    name: 'player',
    props: route => ({
      userId: route.params.userId,
    }),
    component: PlayerPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
