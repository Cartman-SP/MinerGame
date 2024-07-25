<template>
  <div>
    <video autoplay muted loop playsinline controlsList="nodownload" id="bg-video">
      <source src="./static/effect_1717319774214_seamless_loop.mp4">
      Your browser does not support HTML5 video.
    </video>
    <div class="content">
      <div class="header">
        <div class="userinfo">
          <h3>{{ data.user.username || 'test name' }}</h3>
          <p>@{{ data.user.usertag || 'test_tag' }}</p>
        </div>
        <div class="money-block">
          <div>
            <h3>{{ data.user.balance || 'NaN' }}</h3>
            <p>{{ totalIncome }}/ час</p>
          </div>
          <svg width="30" height="20" viewBox="0 0 36 26" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22.9091 0C26.381 0 29.7107 1.36964 32.1658 3.80761C34.6208 6.24558 36 9.55219 36 13C36 16.4478 34.6208 19.7544 32.1658 22.1924C29.7107 24.6304 26.381 26 22.9091 26C19.4372 26 16.1074 24.6304 13.6524 22.1924C11.1974 19.7544 9.81818 16.4478 9.81818 13C9.81818 9.55219 11.1974 6.24558 13.6524 3.80761C16.1074 1.36964 19.4372 0 22.9091 0ZM22.9091 22.75C25.513 22.75 28.0103 21.7228 29.8516 19.8943C31.6929 18.0658 32.7273 15.5859 32.7273 13C32.7273 10.4141 31.6929 7.93419 29.8516 6.10571C28.0103 4.27723 25.513 3.25 22.9091 3.25C20.3051 3.25 17.8079 4.27723 15.9666 6.10571C14.1253 7.93419 13.0909 10.4141 13.0909 13C13.0909 15.5859 14.1253 18.0658 15.9666 19.8943C17.8079 21.7228 20.3051 22.75 22.9091 22.75ZM3.27273 13C3.27273 17.2412 6.00545 20.8487 9.81818 22.1812V25.5775C4.17273 24.1313 0 19.0613 0 13C0 6.93875 4.17273 1.86875 9.81818 0.4225V3.81875C6.00545 5.15125 3.27273 8.75875 3.27273 13Z" fill="#EB95F9"/>
          </svg>
        </div>
      </div>

      <div class="progressbar">
        <div class="progressbar-header">
          <h3 v-if="data.user.lvl<5">{{data.user.balance}} / {{ lvls[data.user.lvl] }}</h3>
          <h3 v-else>Max level</h3>
          <h3>lvl. {{data.user.lvl}}/5</h3>
        </div>
        <div class="bar">
          <ProgressBar v-if="data.user.lvl<5" :value="((data.user.balance/lvls[data.user.lvl])*100).toFixed(1)"></ProgressBar>
          <ProgressBar v-else :value="100"></ProgressBar>

        </div>
      </div>

      <router-view @update-value="updateValue" @update-bal="updateBal"/>
    </div>
    <div class="row_nav">
      <Nav/>
    </div>
    <div v-if="dialog" :class="{'dialog' : dialogClass, 'dialog-hide' : !dialogClass}">
      <div class="container-dialog">
        <h3>Нападало за время Вашего отсутствия монет:</h3>
        <h4>{{ offline_cash }}</h4>
        <button class="collect" @click="toggleDialog">Collect!</button>
      </div>
    </div>
  </div>
</template>


<script>
import ProgressBar from 'primevue/progressbar';
import Nav from "../src/components/NavBar.vue";
import { calculateTotalIncome } from './calculate.js';
import { getUpgradePrices } from './upgrade.js'
import { getMinutesSince } from './timesplit'
export default {
  components: { Nav, ProgressBar },
  data() {
    return {
      data: {user:{username:'F1owerGG',first_name:'CHXRNVKHA',id:'612594627'}},
      totalIncome: 0 , // Добавляем поле для хранения общего дохода
      income: 0,
      offline_cash: 0,
      dialog: false,
      dialogClass: false,
      lvls: {1:25000,2:100000,3:500000,4:1000000}
    }
  },
  methods: {
    toggleDialog(){
      if (this.dialog) {
        this.dialogClass = false;
        console.log('false')
        setTimeout(() => {
          this.dialog = false;
        }, 200);
        
      }else{
        this.dialogClass = true;
        console.log('true')
        setTimeout(() => {
          this.dialog = true;
        }, 300);
      }
    },
    updateValue(newValue) {
      this.data.user.balance += newValue;
    },
    updateBal(message){
      this.data.user.balance-=message.upgrade_cost
      this.totalIncome = calculateTotalIncome(this.$store.state.rooms);
    },
    async get_user(user_id, username, usertag) {
      try {
        const response = await this.$axios.get('/get_user/', {
          params: {
            user_id: user_id,
            username: username,
            usertag: usertag,
          },
          withCredentials: true,
        });
        this.data = response.data;
        this.$store.commit('ADD_TO_DATA', this.data)
        this.$store.commit('ADD_TO_ROOMS', this.data.rooms)
        console.log(this.data.user.created_at)
        let time_went = getMinutesSince(this.data.user.created_at)
        this.totalIncome = calculateTotalIncome(this.data.rooms);
        if(time_went>0){
          this.offline_cash = time_went+2*(Math.trunc(this.totalIncome/60))
          this.$websocket.send(JSON.stringify({user_id: this.data.user.user_id, increment: this.offline_cash,type:'offline'}));
          this.toggleDialog();
          this.data.user.balance += this.offline_cash
          console.log(this.data.user.balance)
        }
        console.log(getUpgradePrices(this.data.rooms[0]))
      } catch (error) {
        this.error = error;
        console.error('Error fetching data:', error);
      }
    },
    loopWithDelay() {
      setTimeout(() => {
        this.income = this.income + this.totalIncome/720;
        if(this.income>1){
          let a = Math.trunc(this.income)
          console.log(a)
          this.$websocket.send(JSON.stringify({user_id: this.data.user.user_id, increment: a,type:'offline'}));
          this.data.user.balance+=a
          this.income = this.income - a

        }
        this.loopWithDelay(); // Рекурсивно вызываем функцию для создания цикла
      }, 5000); // Задержка в 1500 миллисекунд (1.5 секунды)
    },
    async lvl_up(newLevel) {
    try {
      const response = await this.$axios.post('/lvl_up/', {
        user_id: this.data.user.user_id,
        lvl: newLevel
      }, {
        withCredentials: true
      });
      this.data = response.data;
      this.data.user.lvl = newLevel;
    } catch (error) {
      this.error = error;
      console.error('Error fetching data:', error);
    }
  }
  },
  mounted() {
    const tg = window.Telegram.WebApp;
    tg.ready();
    const user = tg.initDataUnsafe.user;
    if (!user || Object.keys(user).length === 0) {
      let id = 612594627;
      let first_name = "CHXRNVKHA";
      let username = "F1owerGG";
      this.get_user(id, first_name, username);
    } else {
      this.get_user(user.id, user.first_name, user.username);
    }
    this.loopWithDelay()
  },
  watch: {
    'data.user.balance': function(newBalance) {
      this.$store.state.data.user.balance = newBalance;
      if ((newBalance > 25000) && (this.data.user.lvl<2)) {
        this.lvl_up(2); // Вызываем функцию lvl_up(), если баланс становится больше 25000
      }
      if (newBalance > 100000 && this.data.user.lvl<3) {
        this.lvl_up(3); // Вызываем функцию lvl_up(), если баланс становится больше 25000
      }
      if (newBalance > 500000 && this.data.user.lvl<4) {
        this.lvl_up(4); // Вызываем функцию lvl_up(), если баланс становится больше 25000
      }
      if (newBalance > 1000000 && this.data.user.lvl<5) {
        this.lvl_up(5); // Вызываем функцию lvl_up(), если баланс становится больше 25000
      }
    }
  }
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

#app {
  font-family: 'Montserrat';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-tap-highlight-color: rgba(0,0,0,0);
  text-align: center;
  color: #2c3e50;
}

* {

-webkit-user-select: none;

-khtml-user-select: none;

-moz-user-select: none;

-ms-user-select: none;

user-select: none;

}

.container-dialog{
  backdrop-filter: blur(20px);
  border: 1px solid rgb(59, 59, 59);
  border-radius: 15px;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 350px;
  margin: 15px;
  padding: 15px;
}
.dialog{
  background-color: rgba(0, 0, 0, 0.737);
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: end;
  z-index: 99;
  opacity: 1;
  transition: all .3s ease;
}

.dialog-hide{
  background-color: rgba(0, 0, 0, 0.737);
  opacity: 0;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: end;
  z-index: 99;
  transition: all .3s ease;
}

h4{
  margin: 0;
  font-size: 3rem;
  color: #EB95F9;
}

.collect{
  background-color: #EB95F9;
  color: white;
  border: none;
  border-radius: 7.5px;
  font-size: 1rem;
  width: 100%;
  padding: 10px 20px;
  font-family: 'Montserrat';
  filter: drop-shadow(0 0 10px #df67f19a);
}

#bg-video {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}

.progressbar-header{
  display: flex;
  justify-content: space-between;
  padding: 10px 15px 0 15px;
}

.progressbar-header h3{
  font-weight: 400;
}

.progressbar{
  margin-bottom: 10px;
}

.content{
  height: 100vh;
  overflow: hidden;
}

.bar{
  padding: 0 15px;
}

.p-progressbar-determinate{
  background: #404557;
  border-radius: 20px;
}

.p-progressbar-value{
  background: #EB95F9;
}

.row_nav{
  height: 0vh;
  display: flex;
  flex-direction: column;
  justify-content: end;
}

body{
  margin: 0;
  padding: 0;
  background-color: #1F262D;

  touch-action: manipulation;
  overflow: hidden;
}

h3{
  color: white;
  font-size: 1rem;
  margin: 0;
}

p{
  color: #7D7D7D;
  font-size: .8rem;
  margin: 0;
}

.userinfo{
  text-align: start;
}

.header{
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
}

.money-block{
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  text-align: start;

  /* background-color: #404557; */
  border-radius: 15px;
  padding: 15px;
  max-width: 200px;
  backdrop-filter: blur(10px);
  border: 1px solid rgb(59, 59, 59);
}


</style>
