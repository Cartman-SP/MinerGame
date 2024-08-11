<template>
  <div class="mainpage" @touchstart.passive.prevent="onTouchStart">
    
    <!-- <h1>{{ video1_lvl + ' ' + video2_lvl + ' ' + video3_lvl + ' ' + video4_lvl}}</h1> -->
    <div>
      <div :class="[spinnerClass(), { bright: isBright }]" >
        <Spinner v-for="n in this.spinnerCount" :key="n" :level="[video1_lvl,video2_lvl,video3_lvl,video4_lvl][n-1]" :isMining="remainingTime > 0" />
      </div>
    </div>
    
    <transition-group name="coin-fall" tag="div" class="mini-coins-container">
      <div v-for="coin in miniCoins" :key="coin.id" :style="{ top: coin.top + 'px', left: coin.left + 'px' }" class="mini-coin">
        <span class="coin-value">+{{ coin.value }}</span>
      </div>
    </transition-group>
    

    <div class="stats-block">
      <div class="energy-block" @click="moveTo('/boost')">
        <p>{{ formatNumber(energy) }}/{{ formatNumber(max_energy) }}</p>
        <img src="../assets/icon-battery.png" style="width: 20px; height: 10px;" alt="">
      </div>
      <div class="timer-block" @click="start_mining" :style="getStyle">
        <p v-if="remainingTime>0" style="color: #00C0FF; font-size: 10px; margin: 0;">{{ formattedRemainingTime }}</p>
        <p v-else style="color: #00C0FF; font-size: 10px; margin: 0;">START MINING</p>
      </div>
      <div class="upgrade-block" @click="moveTo('/upgrade')">
        <p style="font-size: 8px;">UPGRADE</p>
        <img src="../assets/icon-upgrade.png" style="width: 20px; height: 20px;" alt="">
      </div>
    </div>
    <AlertMessage :message="alertMessage" style="z-index: 200;"/>
  </div>
</template>

<script>
import Spinner from '../components/SpinnerMiner.vue';
import AlertMessage from "../components/AlertMessage.vue";

export default {
  components: { Spinner, AlertMessage } ,
  data() {
    return {
      alertMessage: '',

      socket: null,
      miningSocket: null,
      energySocket: null,
      timer: null,
      miningTimer: null,
      remainingTime: 0,
      miniCoins: [],
      coinId: 0,
      isBright: false,
    };
  },
  methods: {
    onTouchStart(event) {
      if (this.$user.data.energy > 0) {
        this.handleTouchStart(event);
        this.createMiniCoin(event);
      }
    },
    handleTouchStart() {
      if (this.$user.data.energy <= 0) return;

      this.$user.playTap(); // Reusing preloaded audio
      this.isBright = true;

      setTimeout(() => {
        this.isBright = false;
      }, 100);

      const message = {
        user_id: this.$user.data.user_id,
        increment: this.$user.data.gpc,
      };

      this.$user.data.tapsocket.send(JSON.stringify(message));
    },
    createMiniCoin(event) {
      const touch = event.touches[0];
      const newCoin = {
        id: this.coinId++,
        value: this.$user.data.gpc,
        top: touch.clientY - 200, // Используем координаты касания
        left: touch.clientX - 30, // Используем координаты касания
      };
      this.miniCoins.push(newCoin);
      setTimeout(() => {
        this.removeMiniCoin(newCoin.id);
      }, 1000); // Время удаления монетки
    },
    removeMiniCoin(id) {
      this.miniCoins = this.miniCoins.filter(coin => coin.id !== id);
    },
    
    moveTo(url){
        this.$router.push(url)
        this.$user.playTap()
      },
    formatNumber(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    },
    async start_mining() {
      this.$user.playTap()

      if (this.remainingTime > 0) {
        console.log("Mining already in progress");
        return;
      }

      try {
        const response = await this.$axios.post('/start_mining/', {user_id: this.$user.data.user_id,}, {withCredentials: true});
        this.$user.data.mining_end = response.data.mining_end;
        console.log("Mining end time set to:", this.$user.data.mining_end);
        this.calculateRemainingTime();
        this.startMiningTimer();
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    formatTime(duration) {
      const hours = Math.floor(duration / 3600);
      const minutes = Math.floor((duration % 3600) / 60);
      const seconds = Math.floor(duration % 60);

      return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    },
    calculateRemainingTime() {
      console.log("Calculating remaining time...");
      if (this.$user.data.mining_end) {
        const now = new Date().getTime();
        const end = new Date(this.$user.data.mining_end).getTime();
        console.log("Current time (now):", now);
        console.log("Mining end time (end):", end);
        const remaining = end - now;
        console.log("Time remaining (ms):", remaining);
        this.remainingTime = remaining > 0 ? remaining / 1000 : 0;
        console.log("Remaining time in seconds:", this.remainingTime);
      } else {
        this.remainingTime = 0;
      }
    },
    updateRemainingTime() {
      if (this.remainingTime > 0) {
        this.remainingTime -= 1;
        console.log("Updated remaining time in seconds:", this.remainingTime);
      }
    },
    handleMiningEndChange(newEndTime) {
      console.log("Handling mining end change:", newEndTime);
      this.$user.data.mining_end = newEndTime;
      this.calculateRemainingTime();
    },
    startMiningTimer() {
      if (this.miningTimer) {
        clearInterval(this.miningTimer);  // Clear any existing timer to avoid multiple intervals running simultaneously.
      }

      this.miningTimer = setInterval(() => {
        if (this.remainingTime > 0) {
          const message = {
            user_id: this.$user.data.user_id,
            gph: this.$user.data.gph,
          };
          this.$user.data.miningsocket.send(JSON.stringify(message));

          this.remainingTime -= 1;  // Decrement remaining time after each second.
        } else {
          clearInterval(this.miningTimer);  // Stop the interval when remainingTime reaches 0.
        }
      }, 1000);  // Send a message every second (1000 milliseconds).
    },

    startEnergyUpdate() {
      setInterval(() => {
          const message = {
            user_id: this.$user.data.user_id,
          };
          console.log(123)
          this.$user.data.energysocket.send(JSON.stringify(message));
      }, 4000); // каждые 5 секунд
    }, 

    spinnerClass() {
      switch (this.spinnerCount) {
        case 1:
          return 'spinner-single';
        case 2:
          return 'spinner-double';
        case 3:
          return 'spinner-triple';
        case 4:
          return 'spinner-grid';
        default:
          return '';
      }
    },
  },
  computed: {
    getStyle() {
      return this.formattedRemainingTime === '00:00:00'
        ? 'filter: drop-shadow(0 0 10px rgb(0, 192, 255))'
        : 'filter: drop-shadow(0 10px 10px rgb(0, 0, 0))';
    },
    spinnerCount(){
      if (this.video4_lvl > 0) {
        return 4
      } else if (this.video3_lvl > 0) {
        return 3
      } else if (this.video2_lvl > 0) {
        return 2
      }
      return 1
    },

    video1_lvl(){
      return this.$user.data.video_lvl
    },
    video2_lvl(){
      return this.$user.data.video2_lvl
    },
    video3_lvl(){
      return this.$user.data.video3_lvl
    },
    video4_lvl(){
      return this.$user.data.video4_lvl
    },
    balance() {
      return this.$user.data.balance;
    },
    gph() {
      return this.$user.data.gph;
    },
    modifier(){
      return this.$user.data.modifier;
    },
    energy() {
      return this.$user.data.energy;
    },
    max_energy(){
      return this.$user.data.max_energy;
    },
    formattedRemainingTime() {
      const formattedTime = this.formatTime(this.remainingTime);
      console.log("Formatted remaining time:", formattedTime);
      return formattedTime;
    }
  },
  mounted() {
    this.$user.data.toppage = false
    console.log("Component mounted, calculating remaining time...");
    this.calculateRemainingTime();
    this.timer = setInterval(() => {
        this.updateRemainingTime();
    }, 1000);

    this.startMiningTimer();
    this.startEnergyUpdate();

    this.$watch(() => this.$user.data.mining_end, (newVal) => {
      console.log("mining_end changed:", newVal);
      if (newVal) {
        this.handleMiningEndChange(newVal);
      }
    });
  },
  beforeUnmount() {
    if (this.timer) {
      clearInterval(this.timer);
    }
    if (this.miningTimer) {
      clearInterval(this.miningTimer);
    }
    if (this.socket) {
      this.socket.close();
    }
    if (this.miningSocket) {
      this.miningSocket.close();
    }
    if (this.energySocket) {
      this.energySocket.close();
    }
  }
};
</script>





<style scoped>

.bright {
  filter: brightness(80%);
  scale: 0.98;
}
.mini-coins-container {
  position: absolute;
  width: 100%;
  height: 50%;
  top: 20%;
  overflow: visible;
}

.mini-coin {
  position: absolute;
  z-index: 999;
  transform: translate(-50%, -50%);
  animation: coin-fall 1s ease forwards;
}

.mini-coin-img {
  width: 30px;
  height: 30px;
}

.coin-value {
  position: absolute;
  top: 0px;
  left: 10px;
  color: white;
  font-size: 30px;
  font-family: "Druk Wide";
}

@keyframes coin-fall {
  0% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
  100% {
    opacity: 0;
    transform: translate(-10%, -50%) scale(0.5);
  }
}
.spinner-single {
  display: flex;
  justify-content: center;
  align-items: center;
}

.spinner-double {
  margin: 10vh 0;
  display: flex;
  justify-content: space-between;
}
.spinner-double > *{
  width: 50%;
}

.spinner-triple {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: auto;
}

.spinner-triple > *{
  width: 100%;
}

.spinner-triple > :nth-child(3) {
  grid-column: span 2;
  justify-self: center;
  width: 50%;
}

.spinner-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}
.spinner-grid > *{
  width: 100%;
  scale: .8;
}


.energy-block, .upgrade-block{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.stats-block p{
  margin: 3px;
  color: white;
  font-family: "Druk Wide";
  font-size: 6px;
}
.timer-block{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.energy-block, .timer-block, .upgrade-block{
  width: 25vw;
  padding: 5px;
  height: 10vw;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  border-radius: 10px;
  filter: drop-shadow(0 10px 10px rgb(0, 0, 0));
}
.stats-block{
  display: flex;
  justify-content: center;
  gap: 10px;
  align-items: center;
  margin-top: 0;
}

.energy-block:hover, .upgrade-block:hover{
  background: linear-gradient(0deg, rgb(44, 42, 41) 0%, rgb(69, 69, 70) 100%);
}


.logo-background{
  width: 50px;
  height: 50px;
  background: linear-gradient(180deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logoSmall{
  width: 35px;
  height: 25px;
}
.mainpage{
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title{
  
  color: white;
  font-family: "Druk Wide";
  font-size: 8px;
  margin: 0;
  margin-top: 10px;
}
</style>