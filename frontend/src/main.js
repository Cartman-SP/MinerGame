import { createApp } from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/aura-light-green/theme.css';
import axiosPlugin from './plugins/axios';

const app = createApp(App);

app.use(store);
app.use(router);
app.use(PrimeVue);
app.use(axiosPlugin);

const tg = window.Telegram.WebApp;
tg.ready();
/// let userId = tg.initDataUnsafe.user.id;
let userId = 612594627;
app.config.globalProperties.$websocket = new WebSocket(`ws://127.0.0.1:8001/ws/change_balance/${userId}/`);
app.mount('#app');
