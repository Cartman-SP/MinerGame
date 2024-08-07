<template>
  <div class="mainpage">

    <Spinner @click="tap()"/>

    <div class="stats-block">
      <div class="energy-block" @click="this.$router.push('/boost')">
        <p>{{ energy }}/{{ max_energy }}</p>
        <img src="../assets/icon-battery.png" style="width: 20px; height: 10px;" alt="">
      </div>
      <div class="timer-block" @click="start_mining" :style="getStyle">
        <p v-if="formattedRemainingTime === '00:00:00'" style="color: #00C0FF; font-size: 10px; margin: 0;">START MINING</p>
        <p v-else style="color: #00C0FF; font-size: 10px; margin: 0;">{{ formattedRemainingTime }}</p>
      </div>
      <div class="upgrade-block" @click="this.$router.push('/upgrade')">
        <p style="font-size: 8px;">UPGRADE</p>
        <img src="../assets/icon-upgrade.png" style="width: 20px; height: 20px;" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import Spinner from '../components/SpinnerMiner.vue';

export default {
  components: { Spinner } ,
  data() {
    return {
      
      socket: null,
      miningSocket: null,
      energySocket: null,
      timer: null,
      miningTimer: null,
      remainingTime: 0,
    };
  },
  methods: {
    
    async start_mining() {
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
    tap() {
      if (this.$user.data.energy > 0) {
        if (this.socket) {
          const message = {
            user_id: this.$user.data.user_id,
            increment: this.$user.data.gpc,
          };
          this.socket.send(JSON.stringify(message));
        }
      }
    },
    onMessage(event) {
      const data = JSON.parse(event.data);
      this.$user.data.balance = data.balance;
      this.$user.data.energy = data.energy;
    },
    onMiningMessage(event) {
      const data = JSON.parse(event.data);
      this.$user.data.balance = data.balance;
      this.$user.data.energy = data.energy;
    },
    onEnergyMessage(event) {
      const data = JSON.parse(event.data);
      this.$user.data.energy = data.energy;
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
        clearInterval(this.miningTimer);
      }
      this.miningTimer = setInterval(() => {
        if (this.remainingTime > 0) {
          if (this.miningSocket) {
            const message = {
              user_id: this.$user.data.user_id,
              gph: this.$user.data.gph,
            };
            this.miningSocket.send(JSON.stringify(message));
          }
        } else {
          clearInterval(this.miningTimer);
        }
      }, 1000); // каждую 1 секунд
    },
    initializeWebSocketConnections() {
      const userId = this.$user.data.user_id;

      this.socket = new WebSocket(`ws://localhost:8001/ws/some_path/${userId}/`);
      this.socket.onmessage = this.onMessage;
      this.socket.onopen = () => {
        console.log('WebSocket connection established');
      };
      this.socket.onclose = () => {
        console.log('WebSocket connection closed');
      };
      this.socket.onerror = (error) => {
        console.error('WebSocket error:', error);
      };

      this.miningSocket = new WebSocket(`ws://localhost:8001/ws/mining/${userId}/`);
      this.miningSocket.onmessage = this.onMiningMessage;
      this.miningSocket.onopen = () => {
        console.log('Mining WebSocket connection established');
        this.startMiningTimer();
      };
      this.miningSocket.onclose = () => {
        console.log('Mining WebSocket connection closed');
      };
      this.miningSocket.onerror = (error) => {
        console.error('Mining WebSocket error:', error);
      };

      this.energySocket = new WebSocket(`ws://localhost:8001/ws/energy/${userId}/`);
      this.energySocket.onmessage = this.onEnergyMessage;
      this.energySocket.onopen = () => {
        console.log('Energy WebSocket connection established');
        this.startEnergyUpdate(); // Start energy updates
      };
      this.energySocket.onclose = () => {
        console.log('Energy WebSocket connection closed');
      };
      this.energySocket.onerror = (error) => {
        console.error('Energy WebSocket error:', error);
      };
    },
    startEnergyUpdate() {
      setInterval(() => {
        if (this.energySocket) {
          const message = {
            user_id: this.$user.data.user_id,
          };
          this.energySocket.send(JSON.stringify(message));
        }
      }, 5000); // каждые 5 секунд
    }
  },
  computed: {
    getStyle() {
      return this.formattedRemainingTime === '00:00:00'
        ? 'filter: drop-shadow(0 0 10px rgb(0, 192, 255))'
        : 'filter: drop-shadow(0 0 3px rgb(0, 0, 0))';
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
    console.log("Component mounted, calculating remaining time...");
    this.calculateRemainingTime();
    this.timer = setInterval(() => {
        this.updateRemainingTime();
    }, 1000);

    this.initializeWebSocketConnections();

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
  width: 100px;
  padding: 5px;
  height: 35px;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  border-radius: 10px;
}
.stats-block{
  display: flex;
  justify-content: center;
  gap: 10px;
  align-items: center;
  margin-top: -60px;
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