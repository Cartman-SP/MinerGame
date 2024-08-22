import { createApp, reactive, watch  } from 'vue';
import App from './App.vue';
import router from './router';
import axiosPlugin from './plugins/axios'; // Ваш плагин Axios
import buymp3 from './assets/buy.mp3';
import tapmp3 from './assets/tap.mp3';
import errormp3 from './assets/error.mp3';




const app = createApp(App);


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
      subscribed: false,
      subscribed_money_gived: false,
      friends_invited: 0,
      avatar: '' ,
      daily_reward_claimed: false,
      daily_reward_day: 0,
      daily_reward_date: '',
      secs_in_game: 0,
      video_lvl: 0,
      tapsocket: NaN,
      energysocket:NaN,
      miningsocket:NaN,
      mined_while_of: 0,
      mining_time_lvl: 0,
      toppage: false,
      vibrate: true,
      sound: true,
      buyaudio: new Audio(buymp3),
      tapaudio: new Audio(tapmp3),
      erroraudio: new Audio(errormp3),
      video2_lvl: 0,
      video3_lvl: 0,
      video4_lvl: 0,
      costs: {},
      lang: '', 
      hard_graphic: false
    });
    this.loading = reactive({ status: false });
    this.error = null;

    // Добавляем watcher для поля balance
    watch(() => this.data.balance, (newBalance) => {
      if(newBalance > 17500 && this.data.lvl < 2){
        this.lvlup(2);
      } else if(newBalance > 90000 && this.data.lvl < 3){
        this.lvlup(3);
      } else if(newBalance > 400000 && this.data.lvl < 4){
        this.lvlup(4);
      } else if(newBalance > 5000000 && this.data.lvl < 5){
        this.lvlup(5);
      } else if(newBalance > 22000000 && this.data.lvl < 6){
        this.lvlup(6);
      } else if(newBalance > 100000000 && this.data.lvl < 7){
        this.lvlup(7);
      } else if(newBalance > 510000000 && this.data.lvl < 8){
        this.lvlup(8);
      } else if(newBalance > 800000000 && this.data.lvl < 9){
        this.lvlup(9);
      } else if(newBalance > 1800000000 && this.data.lvl < 10){
        this.lvlup(10);
      }
    });
  }

  async lvlup(lvl) {
    this.data.lvl = lvl;
    try {
      const response = await app.config.globalProperties.$axios.post('/lvlup/', {
        'user_id': this.data.user_id,
        'lvl': lvl
      }, { withCredentials: true });
      this.data.gpc = response.data.gpc;
      this.data.modifier = response.data.modifier;
      this.data.max_energy = response.data.max_energy;
    } catch (error) {
      console.log(error);
    }
  }

  onMessage(event) {
    const data = JSON.parse(event.data);
    this.data.balance = data.balance;
    this.data.energy = data.energy;
  }
  onMiningMessage(event) {
    const data = JSON.parse(event.data);
    this.data.balance = data.balance;
    this.data.energy = data.energy;
  }
  onEnergyMessage(event) {
    const data = JSON.parse(event.data);
    this.data.energy = data.energy;
  }

  reconnectSocket(socketName) {
    if (this.data[socketName] && this.data[socketName].readyState !== WebSocket.OPEN) {
      setTimeout(() => {
        if (socketName === 'tapsocket') {
          this.initTapSocket();
        } else if (socketName === 'energysocket') {
          this.initEnergySocket();
        } else if (socketName === 'miningsocket') {
          this.initMiningSocket();
        }
      }, this.reconnectDelay);
    }
  }

  initTapSocket() {
    this.data.tapsocket = new WebSocket(`wss://ylionminer.fun/ws/some_path/${this.data.user_id}/`);
    this.data.tapsocket.onmessage = this.onMessage.bind(this);
    this.data.tapsocket.onopen = () => {
    };
    this.data.tapsocket.onclose = () => {
      this.reconnectSocket('tapsocket');
    };
    this.data.tapsocket.onerror = (error) => {
      console.error('WebSocket error:', error);
      this.reconnectSocket('tapsocket');
    };
  }

  initEnergySocket() {
    this.data.energysocket = new WebSocket(`wss://ylionminer.fun/ws/energy/${this.data.user_id}/`);
    this.data.energysocket.onmessage = this.onEnergyMessage.bind(this);
    this.data.energysocket.onopen = () => {
    };
    this.data.energysocket.onclose = () => {
      this.reconnectSocket('energysocket');
    };
    this.data.energysocket.onerror = (error) => {
      console.error('Energy WebSocket error:', error);
      this.reconnectSocket('energysocket');
    };
  }

  initMiningSocket() {
    this.data.miningsocket = new WebSocket(`wss://ylionminer.fun/ws/mining/${this.data.user_id}/`);
    this.data.miningsocket.onmessage = this.onMiningMessage.bind(this);
    this.data.miningsocket.onopen = () => {
      this.loading.status = true;
    };
    this.data.miningsocket.onclose = () => {
      this.reconnectSocket('miningsocket');
    };
    this.data.miningsocket.onerror = (error) => {
      console.log(error)
      this.reconnectSocket('miningsocket');
    };
  }


  playBuy(){
    if(this.data.vibrate){
      window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
    }
    if(this.data.sound){
      this.data.buyaudio.volume = 0.1
      this.data.buyaudio.play()
    }
  }
  playTap(){
    if(this.data.vibrate){
      window.Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }
    if(this.data.sound){
      this.data.tapaudio.play()
    }
  }
  playError(){
    if(this.data.vibrate){
      window.Telegram.WebApp.HapticFeedback.notificationOccurred('error');
    }
    if(this.data.sound){
      this.data.erroraudio.volume = 0.1
      this.data.erroraudio.play()
    }
  }
  
async login() {
  const tg = window.Telegram.WebApp;

  if (tg) {
    tg.ready();
    const tginfo = tg.initDataUnsafe.user || {
      "id": 7139071601,
      "first_name": "CHXRNVKHA",
      "last_name": "",
      "username": "F1owerGG",
      "language_code": "en",
      "is_premium": true,
      "allows_write_to_pm": true,
      "photo_url": "default-avatar-url" // Добавляем аватарку по умолчанию
    };

    const start = tg.initDataUnsafe.start_param ? tg.initDataUnsafe.start_param : 0;
    tginfo.start = start;
    let data = tginfo;

    // Функция тайм-аута для ограничения времени выполнения одной итерации
    const timeout = (ms) => new Promise((_, reject) => setTimeout(() => reject(new Error('Iteration timed out')), ms));

    try {
      const response = await Promise.race([
        app.config.globalProperties.$axios.get('/get_user/', { params: data }),
        timeout(7000) // Лимит времени на выполнение одной итерации: 7 секунд
      ]);

      // Обработка данных пользователя
      const userData = response.data.user;
      this.data.lang = tginfo.language_code;
      this.data.user_id = userData.user_id;
      this.data.username = userData.username;
      this.data.usertag = userData.usertag;
      this.data.balance = userData.balance;
      this.data.lvl = userData.lvl;
      this.data.energy = userData.energy;
      this.data.gph = userData.gph;
      this.data.gpc = userData.gpc;
      this.data.mining_end = userData.mining_end;
      this.data.enery_lvl = userData.enery_lvl;
      this.data.tap_lvl = userData.tap_lvl;
      this.data.refresh_energy = userData.refresh_energy;
      this.data.max_energy = userData.max_energy;
      this.data.modifier = userData.modifier;
      this.data.subscribed = userData.subscribed;
      this.data.subscribed_money_gived = userData.subscribed_money_gived;
      this.data.avatar = userData.avatar || this.data.avatar;
      this.data.avatar = userData.photo_url || 'default-avatar-url';
      this.data.friends_invited = userData.friends_invited;
      this.data.daily_reward_claimed = userData.daily_reward_claimed;
      this.data.daily_reward_day = userData.daily_reward_day;
      this.data.daily_reward_date = userData.daily_reward_date;
      this.data.secs_in_game = userData.secs_in_game;
      this.data.video_lvl = userData.video_lvl;
      this.data.mined_while_of = response.data.mined_while_of;
      this.data.mining_time_lvl = userData.mining_time_lvl;
      this.data.toppage = false;
      this.data.sound = userData.sound;
      this.data.vibrate = userData.vibrate;
      this.data.buyaudio.volume = 0.5;
      this.data.tapaudio.volume = 1;
      this.data.erroraudio.volume = 0.5;
      this.data.video2_lvl = userData.video2_lvl;
      this.data.video3_lvl = userData.video3_lvl;
      this.data.video4_lvl = userData.video4_lvl;
      this.data.costs = response.data.costs;
      if (this.data.wallet_address) {
        this.tonConnect.restoreConnection(this.data.wallet_address);
      }

    } catch (error) {
      console.error('Error occurred:', error);
      window.location.reload(); // Перезагрузка страницы при ошибке или тайм-ауте
    }
  } else {
    console.error('Telegram WebApp is not available');
    this.loading.status = false;
  }
  this.initTapSocket();
  this.initEnergySocket();
  this.initMiningSocket();
}

  
  
}


// Создаем экземпляр User
const user = new User();

app.config.globalProperties.$user = user;

app.use(router);

user.login().then(() => {
  document.getElementById('loading').style.display = 'none';
  document.getElementById('app').style.display = 'block';
  app.mount('#app');
})
