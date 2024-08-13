<template>
  <div :class="['spinner', `level-${level}`, { bright: isBright }]" @touchstart.passive.prevent="onTouchStart">
    <div class="spinners-block">
      <img v-if="isMining" class="spinner-img" :src="preloadedGifPath" alt="Spinner GIF" style="user-select: none;">
      <img v-else class="spinner-img" :src="preloadedStaticPath" alt="Spinner GIF" style="user-select: none;">
    </div>

    <transition-group name="coin-fall" tag="div" class="mini-coins-container">
      <div v-for="coin in miniCoins" :key="coin.id" :style="{ top: coin.top + 'px', left: coin.left + 'px' }" class="mini-coin">
        <span class="coin-value">+{{ coin.value }}</span>
      </div>
    </transition-group>
  </div>
</template>

<script>
export default {
  props: ['isMining', 'level'],
  data() {
    return {
      preloadedGifPath: '',
      preloadedStaticPath: '',
      taps: 0,
      miniCoins: [],
      coinId: 0,
      isBright: false,
    };
  },
  computed: {
    gifPath() {
      switch (this.level) {
        case 1:
          return require(`../assets/gpu1.gif`);
        case 2:
          return require(`../assets/gpu1.gif`);
        case 3:
          return require(`../assets/gpu1.gif`);
        case 4:
          return require(`../assets/gpu4.gif`);
        case 5:
          return require(`../assets/gpu5.gif`);
        case 6:
          return require(`../assets/gpu6.gif`);
        case 7:
          return require(`../assets/gpu7.gif`);
        case 8:
          return require(`../assets/gpu8.gif`);
        case 9:
          return require(`../assets/gpu9.gif`);
        case 10:
          return require(`../assets/gpu10.gif`);
        case 11:
          return require(`../assets/gpu11.gif`);
      }
      return 1
    },
    staticPath() {
      switch (this.level) {
        case 1:
          return require(`../assets/gpu1-static.png`);
        case 2:
          return require(`../assets/gpu1-static.png`);
        case 3:
          return require(`../assets/gpu1-static.png`);
        case 4:
          return require(`../assets/gpu4-static.png`);
        case 5:
          return require(`../assets/gpu5-static.png`);
        case 6:
          return require(`../assets/gpu6-static.png`);
        case 7:
          return require(`../assets/gpu7-static.png`);
        case 8:
          return require(`../assets/gpu8-static.png`);
        case 9:
          return require(`../assets/gpu9-static.png`);
        case 10:
          return require(`../assets/gpu10-static.png`);
        case 11:
          return require(`../assets/gpu11-static.png`);
      }
      return 1
    }
  },
  mounted() {
    this.preloadImages();
  },
  watch: {
    level() {
      this.preloadImages();
    }
  },
  methods: {
    onTouchStart(event) {
      if (this.$user.data.energy > 0) {
        this.handleTouchStart(event);
        this.createMiniCoin(event);
      }
    },
    handleTouchStart() {
      if (this.$user.data.energy > 0){
        this.$user.playTap(); // Reusing preloaded audio
        this.isBright = true;

        setTimeout(() => {
          this.isBright = false;
        }, 100);

        const message = {
          user_id: this.$user.data.user_id,
          increment: this.$user.data.gpc,
        };
        this.$user.data.energy -=1
        this.$user.data.tapsocket.send(JSON.stringify(message));
      }
    },
    createMiniCoin(event) {
      const touch = event.touches[0];
      const newCoin = {
        id: this.coinId++,
        value: this.$user.data.gpc,
        top: touch.clientY/5, // Используем координаты касания
        left: touch.clientX/2, // Используем координаты касания
      };
      this.miniCoins.push(newCoin);
      setTimeout(() => {
        this.removeMiniCoin(newCoin.id);
      }, 1000); // Время удаления монетки
    },
    removeMiniCoin(id) {
      this.miniCoins = this.miniCoins.filter(coin => coin.id !== id);
    },
    
    preloadImages() {
      this.preloadedGifPath = this.gifPath;
      this.preloadedStaticPath = this.staticPath;
      
      const gifImage = new Image();
      gifImage.src = this.preloadedGifPath;

      const staticImage = new Image();
      staticImage.src = this.preloadedStaticPath;
    }
  }
};
</script>


<style scoped>
.spinners-block{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  position: relative;
}
.bright {
  /* filter: brightness(80%);
  scale: 0.98; */
  opacity: .8;
  /* scale: 0.98; */
}
.mini-coins-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  overflow: hidden;
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

.spinner {
  user-select: none;
  margin: -5vh 0 1vh 0;
  animation: pulseGlow 2s infinite;
  width: 100%;
}

.level-1 {
  --glow-color: rgba(0, 192, 255, 1);
}

.level-2 {
  --glow-color: rgba(0, 192, 255, 1);
}

.level-3 {
  --glow-color: rgba(0, 192, 255, 1);
}

.level-4 {
  --glow-color: rgba(0, 255, 0, 1);
}

.level-5 {
  --glow-color: rgba(0, 255, 0, 1);
}

.level-6 {
  --glow-color: rgba(0, 255, 0, 1);
}
.level-7 {
  --glow-color: rgba(255, 255, 0, 1);
}
.level-8 {
  --glow-color: rgba(255, 255, 0, 1);
}
.level-9 {
  --glow-color: rgba(255, 255, 0, 1);
}
.level-10 {
  --glow-color: rgb(180, 29, 245);
}
.level-11 {
  --glow-color: rgb(0, 217, 255);
}

.spinner-img {
  width: 35vh;
  aspect-ratio: 1;
  filter: drop-shadow(0 0 20px var(--glow-color));
}

@keyframes pulseGlow {
  0% {
    filter: drop-shadow(0 0 20px var(--glow-color));
  }
  50% {
    filter: drop-shadow(0 0 40px rgba(var(--glow-color, 0.5)));
  }
  100% {
    filter: drop-shadow(0 0 20px var(--glow-color));
  }
}
</style>