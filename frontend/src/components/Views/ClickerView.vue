<template>
  <div class="container">
    <div style="width: 100%;">
      <balls v-if="false"/>
      <!-- <h3>Taps left: 100</h3> -->
      <div>
        <img
          :id="boostActive ? 'coin_boost' : 'coin'"
          src="../../static/imgs/Coin.png" 
          @click="handleCoinClick" 
        >
        <img :id="boostActive ? 'shine_boost' : 'shine'" src="../../static/imgs/shine2.png" alt="">

        
        <transition-group name="coin-fall" tag="div" class="mini-coins-container">
          <div v-for="coin in miniCoins" :key="coin.id" :style="{ top: coin.top, left: coin.left }" class="mini-coin">
            <img src="../../static/imgs/Coin.png" alt="" class="mini-coin-img">
            <span class="coin-value">{{ coin.value }}</span>
          </div>
        </transition-group>
      </div>
    </div>
    <div class="statistics">
        <div class="up-block">
            <img src="../../static/imgs/money.png" alt="">
            <div >
              <h3>{{ this.$store.state.data.user.gpc }}</h3>
              <p>Coins / tap</p>
              <p style="color: rgb(255, 255, 255);">Lvl {{ lvls[this.$store.state.data.user.gpc]}}</p>
            </div>
            <button @click="upgrade_click" class="btn-upgrade" style="width: 100%; margin-top: 10px;">{{ this.upgradecost[this.$store.state.data.user.gpc] }}</button>
        </div>
        <div class="up-block">
          <img src="../../static/imgs/taps.png" alt="">
          <div>
            <h3>20/min</h3>
            <p>Taps limit</p>
            <p style="color: rgb(255, 255, 255);">Lvl 1</p>
          </div>
          <button class="btn-upgrade-disabled" style="width: 100%; margin-top: 10px;">Soon!</button>
      </div> 
        <div class="up-block">
            <img src="../../static/imgs/energy.png" alt="">
            <div>
              <h3>2%</h3>
              <p>Super taps</p>
              <p style="color: rgb(255, 255, 255);">Lvl 1</p>
            </div>
            <button class="btn-upgrade-disabled" style="width: 100%; margin-top: 10px;">Soon!</button>
        </div>
        <div class="up-block">
            <img src="../../static/imgs/Picture.png" alt="">
            <div>
              <h3>Gold</h3>
              <p>Coin skin</p>
              <p style="color: rgb(255, 255, 255);">Lvl 1</p>
            </div>
            <button class="btn-upgrade-disabled" style="width: 100%; margin-top: 10px;">Soon!</button>
        </div> 
    </div>
  </div>
</template>

<script>
import balls from "../DropsBalls.vue";

export default {
  components: { balls },
  data() {
    return {
      isEnlarged: false,
      taps: 0,
      miniCoins: [],
      coinId: 0,
      clickTimestamps: [],
      boostActive: false,
      upgradecost: {2: 5000, 3: 10000, 5: 20000, 8: 50000, 12: 100000, 20: 250000, 30: 500000, 50: 1000000, 100: 2500000},
      lvls: {2: 1, 3: 2, 5: 3, 8: 4, 12: 5, 20: 6, 30: 7, 50: 8, 100: 9, 150: 10},
      
    };
  },
  methods: {
    
    async upgrade_click() {
      try {
        const response = await this.$axios.post('/upgrade_coin/', {
          user_id: this.$store.state.data.user.user_id,
        }, {
          withCredentials: true
        });
        this.$store.state.data.user.gpc = response.data.gpc;
        this.$emit('update-value', response.data.cost * -1);
      } catch (error) {
        this.error = error;
        console.error('Error fetching data:', error);
      }
    },
    handleCoinClick() {
      const now = Date.now();
      this.clickTimestamps.push(now);
      

      // Remove timestamps older than 1 second
      this.clickTimestamps = this.clickTimestamps.filter(timestamp => now - timestamp < 2000);

      if (this.clickTimestamps.length >= 20 && !this.boostActive) {
        this.activateBoost();
      }

      this.isEnlarged = !this.isEnlarged;
      setTimeout(() => {
        this.isEnlarged = !this.isEnlarged;
      }, 300);

      this.sendBalanceUpdate(this.$store.state.data.user.user_id, this.$store.state.data.user.gpc * this.$store.state.data.user.lvl * (this.boostActive ? 2 : 1));
      this.createMiniCoin();
    },
    activateBoost() {
      this.boostActive = true;
      setTimeout(() => {
        this.boostActive = false;
      }, 2000); // Boost duration: 5 seconds
    },
    updateBalance(message) {
      this.$websocket.send(JSON.stringify(message));
      this.$emit('update-value', message.increment);
    },
    sendBalance(user_id, increment) {
      const message = {
        user_id: user_id,
        increment: increment,
        type: 'click'
      };
      this.updateBalance(message);
    },
    sendBalanceUpdate(user_id, increment) {
      this.sendBalance(user_id, increment);
    },
    createMiniCoin() {
      const newCoin = {
        id: this.coinId++,
        value: this.$store.state.data.user.gpc * this.$store.state.data.user.lvl * (this.boostActive ? 2 : 1),
        top: Math.random() * 100 + '%',
        left: Math.random() * 100 + '%',
      };
      this.miniCoins.push(newCoin);
      setTimeout(() => {
        this.removeMiniCoin(newCoin.id);
      }, 1000); // Adjust the time to remove the coin as needed
    },
    removeMiniCoin(id) {
      this.miniCoins = this.miniCoins.filter(coin => coin.id !== id);
    },
  },
};
</script>


<style scoped>
@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

#shine {
  display: block;
  position: absolute;
  top: 13%;
  left: 0;
  width: 100%;
  filter: saturate(0);
  scale: 1;
  z-index: 10;
  animation: rotate 10s linear infinite;
  transition: all .2s ease;
}

#shine_boost {
  display: block;
  position: absolute;
  top: 13%;
  left: 0;
  width: 100%;
  scale: 1.5;
  filter: saturate(100%);
  z-index: 10;
  animation: rotate 10s linear infinite;
  transition: all .2s ease;
}

#coin {
  margin-bottom: 40px;
  transition: transform 0.2s ease;
  z-index: 11;
  position: absolute;
  top: 10%;
  left: 0;
  width: 100%;
  scale: 0.5;
  animation: MainCoin 2s ease-in-out infinite;
}


#coin_boost {
  margin-bottom: 40px;
  transition: transform 0.2s ease;
  z-index: 11;
  position: absolute;
  top: 10%;
  left: 0;
  width: 100%;
  scale: 0.5;
  animation: MainCoin 2s ease-in-out infinite;
  animation: ShakeCoin 1s ease infinite;
}

.enlarged {
  transform: scale(0.4);
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
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
  top: -10px;
  left: 10px;
  color: white;
  font-size: 12px;
  font-weight: bold;
}

@keyframes coin-fall {
  0% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
  100% {
    opacity: 0;
    transform: translate(-50%, -200%) scale(0.5);
  }
}

@keyframes ShakeCoin {
  0% {
    transform: scale(1) rotate(0deg);
  }
  100% {
    transform: scale(.9) rotate(-10deg);
  }
  20% {
    transform: scale(1) rotate(10deg);
  }
  30% {
    transform: scale(.9) rotate(0deg);
  }
  40% {
    transform: scale(1) rotate(-10deg);
  }
  50% {
    transform: scale(.9) rotate(10deg);
  }
  60% {
    transform: scale(1) rotate(0deg);
  }
  70% {
    transform: scale(.9) rotate(-10deg);
  }
  80% {
    transform: scale(1) rotate(10deg);
  }
  90% {
    transform: scale(.9) rotate(0deg);
  }
  100% {
    transform: scale(1) rotate(0deg);
  }
}


@keyframes MainCoin {
  0% {
    transform: translate(0, 5%);
  }
  50% {
    transform: translate(0, -5%);
  }
  100% {
    transform: translate(0, 5%);
  }
}

.statistics{
  display: flex;
  gap: 10px;
  overflow-x: scroll;
  padding: 15px;
  width: inherit;
}

.statistics::-webkit-scrollbar{
    display: none;
}
.up-block{
  backdrop-filter: blur(10px);
  border: 1px solid rgb(59, 59, 59);
  border-radius: 15px;
  text-align: start;
  padding: 10px;
}
.up-block img{
  width: 25px;
  border-radius: 7.5px;
}
.row{
  display: flex;
  align-items: center;
  gap: 10px;
}
.btn-upgrade{
  background-color: #EB95F9;
  color: white;
  border: none;
  border-radius: 7.5px;
  padding: 10px 20px;
  font-family: 'Montserrat';
  filter: drop-shadow(0 0 10px #df67f19a);
}

.btn-upgrade-disabled{
  background-color: #885590;
  color: white;
  border: none;
  border-radius: 7.5px;
  padding: 10px 20px;
  font-family: 'Montserrat';
  filter: none;
}
</style>
