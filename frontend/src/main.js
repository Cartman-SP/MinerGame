import { createApp } from 'vue';
import App from './App.vue';


class User {
  constructor() {
    this.username = '';
    this.email = '';
  }

  login() {
    const webexample = { "id": 612594627, "first_name": "CHXRNVKHA", "last_name": "", "username": "F1owerGG", "language_code": "ru", "is_premium": true, "allows_write_to_pm": true }
    const tg = window.Telegram.WebApp;
    tg.ready();
    const tginfo = tg.initDataUnsafe.user;
    if(tginfo){
        return tginfo
    }else{
        return webexample
    }
    
  }
}

const user = new User();
const app = createApp(App);

app.config.globalProperties.$user = user;

// Монтирование приложения
app.mount('#app');
