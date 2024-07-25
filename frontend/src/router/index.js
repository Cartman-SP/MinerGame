import { createRouter, createWebHistory } from 'vue-router'
import lootpage from '../components/Views/LootView.vue';
import clickerpage from '../components/Views/ClickerView.vue';
import boostspage from '../components/Views/BoostsView.vue';
import userpage from '../components/Views/UserView.vue';
import model from '../components/Views/ModelView.vue';

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes:[
    {
      path: '/loot',
      name: 'loot',
      component: lootpage,
    },
    {
      path: '/clicker',
      name: 'clicker',
      component: clickerpage,
    },
    {
      path: '/boosts',
      name: 'boosts',
      component: boostspage,
    },
    {
      path: '/user',
      name: 'user',
      component: userpage,
    },
    {
      path: '/model',
      name: 'model',
      component: model,
    },
  ]
})


router.beforeEach((to, from, next) => {
  // Если это перезагрузка страницы (to.name === null), перенаправляем на /clicker
  if (!from.name && to.name !== 'clicker') {
    next({ name: 'clicker' });
  } else {
    next();
  }
});

export default router
