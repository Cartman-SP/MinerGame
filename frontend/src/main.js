import { createApp, reactive } from 'vue';
import App from './App.vue';
import router from './router';
import axiosPlugin from './plugins/axios'; // Ваш плагин Axios

const app = createApp(App);

// Подключаем плагин Axios
app.use(axiosPlugin);

class User {
  constructor() {
    this.data = reactive({
      user_id: 0,
      username: '',
      usertag: '',
      balance: 0,
      lvl: 0,
      energy: 0,
      gph: 0,
      gpc: 0,
      mining_end: '',
      enery_lvl: 0,
      tap_lvl: 0,
      refresh_energy: 0,
      max_energy : 0,
    });
    this.loading = reactive({ status: true });
    this.error = null;
  }

  async login() {
    const webexample = {
      "id": 612594627,
      "first_name": "CHXRNVKHA",
      "last_name": "",
      "username": "F1owerGG",
      "language_code": "ru",
      "is_premium": true,
      "allows_write_to_pm": true
    };

    const tg = window.Telegram.WebApp;

    if (tg) {
      tg.ready();
      const tginfo = tg.initDataUnsafe.user;
      let data = tginfo ? tginfo : webexample;

      try {
        const response = await app.config.globalProperties.$axios.get('/get_user/', { params: data });
        console.log(response.data);
        this.data.user_id = response.data.user.user_id;
        this.data.username = response.data.user.username;
        this.data.usertag = response.data.user.usertag;
        this.data.balance = response.data.user.balance;
        this.data.lvl = response.data.user.lvl;
        this.data.energy = response.data.user.energy;
        this.data.gph = response.data.user.gph;
        this.data.gpc = response.data.user.gpc;
        this.data.mining_end = response.data.user.mining_end;
        this.data.enery_lvl=response.data.user.enery_lvl
        this.data.tap_lvl=response.data.user.tap_lvl
        this.data.refresh_energy=response.data.user.refresh_energy
        this.data.max_energy = response.data.user.max_energy
        console.log("mining_end after login:", this.data.mining_end);
      } catch (error) {
        this.error = error;
        console.error('Error fetching data:', error);
      } finally {
        this.loading.status = false;
      }
    } else {
      console.error('Telegram WebApp is not available');
      this.loading.status = false;
    }
  }
}

// Создаем экземпляр User
const user = new User();

app.config.globalProperties.$user = user;

app.use(router);

user.login().then(() => {
  app.mount('#app');
});
