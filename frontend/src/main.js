import { createApp, reactive, watch } from 'vue';
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
      max_energy: 0,
      modifier: 1,
    });
    this.loading = reactive({ status: true });
    this.error = null;

    // Добавляем watcher для поля balance
    watch(() => this.data.balance, (newBalance, oldBalance) => {
      console.log(newBalance,oldBalance)
      if(newBalance>17500 && this.data.lvl<2){
        this.lvlup(2)
      }else if(newBalance>90000 && this.data.lvl<3){
        this.lvlup(3)
      }else if(newBalance>400000 && this.data.lvl<4){
        this.lvlup(4)
      }else if(newBalance>5000000 && this.data.lvl<5){
        this.lvlup(5)
      }else if(newBalance>650000 && this.data.lvl<6){
        this.lvlup(6)
      }else if(newBalance>100000000 && this.data.lvl<7){
        this.lvlup(7)
      }else if(newBalance>510000000 && this.data.lvl<8){
        this.lvlup(8)
      }else if(newBalance>1600000000 && this.data.lvl<9){
        this.lvlup(9)
      }else if(newBalance>3800000000 && this.data.lvl<10){
        this.lvlup(10)
      }

    });
  }

  lvlup(lvl){
    this.data.lvl = lvl
    try {
      const response = app.config.globalProperties.$axios.post('/lvlup/', {'user_id':this.data.user_id, 'lvl':lvl}, {withCredentials: true});
      console.log(response.data);
      this.data.gpc = response.data.gpc
      this.data.modifier= response.data.modifier
      this.data.max_energy =  response.data.max_energy

    } catch (error) {
      console.log(error)
    }
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
        this.data.enery_lvl = response.data.user.enery_lvl;
        this.data.tap_lvl = response.data.user.tap_lvl;
        this.data.refresh_energy = response.data.user.refresh_energy;
        this.data.max_energy = response.data.user.max_energy;
        this.data.modifier = response.data.user.modifier
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
