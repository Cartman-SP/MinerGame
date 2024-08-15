<template>
  <div :class="['spinner', `level-${level}`, { bright: isBright }]" @touchend="onTouchEnd" :style="{ animation: hardGraphic ? '' : '0s !important' }">
    <div class="spinners-block" ref="clicker">
      <img v-if="isMining&&hardGraphic" class="spinner-img" :src="preloadedGifPath" alt="Spinner GIF" style="user-select: none;">
      <img v-else class="spinner-img" :src="preloadedStaticPath" alt="Spinner GIF" style="user-select: none;">
      <div v-for="coin in miniCoins" :key="coin.id" :style="{ top: coin.top + 'px', left: coin.left + 'px' }" class="mini-coin">
        <span class="coin-value">+{{ coin.value }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['isMining', 'level'],
  data() {
    return {
      imageAssets: {},
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
      const lvls={'1':1,'2':1,'3':1,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'11':11}
      return this.imageAssets[`gif${lvls[this.level]}`];
    },
    staticPath() {
      const lvls={'1':1,'2':1,'3':1,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'11':11}
      return this.imageAssets[`static${lvls[this.level]}`];
    },
    hardGraphic(){
      return this.$user.data.hard_graphic
    },
  },
  mounted() {
    this.preloadImages();
    setTimeout(() => {
      const clickerwindow = this.$refs.clicker;
      if (clickerwindow) {
        clickerwindow.classList.add('clicker-show');
      }
    }, 10);
  },
  watch: {
    level() {
      this.preloadImages();
      const clickerwindow = this.$refs.clicker;
      clickerwindow.classList.remove('clicker-show');
      setTimeout(() => {
        if (clickerwindow) {
          clickerwindow.classList.add('clicker-show');
        }
      }, 10);
    }
  },
  methods: {
    onTouchEnd(event) {
      this.handleTouchStart(event);
    },
    handleTouchStart(event) {
      if (this.$user.data.energy > 0){
        this.createMiniCoin(event);

        if (this.hardGraphic) {
          this.isBright = true;
        }
        
        const message = {
          user_id: this.$user.data.user_id,
          increment: this.$user.data.gpc,
        };
        this.$user.data.energy -=1;
        this.$user.data.tapsocket.send(JSON.stringify(message));
        setTimeout(() => {
          this.isBright = false;
        }, 100);
      }
    },
    createMiniCoin(event) {
      const touch = event.changedTouches[0];
      const newCoin = {
        id: this.coinId++,
        value: this.$user.data.gpc,
        top: touch.clientY - 300,
        left: touch.clientX - 50,
      };
      this.miniCoins.push(newCoin);
      setTimeout(() => {
        this.removeMiniCoin(newCoin.id);
      }, 1000);
    },
    removeMiniCoin(id) {
      this.miniCoins = this.miniCoins.filter(coin => coin.id !== id);
    },
    preloadImages() {
      const levels = [1,4, 5, 6, 7, 8, 9, 10, 11];
      levels.forEach(level => {
        this.imageAssets[`gif${level}`] = require(`../assets/gpu${level}.gif`);
        this.imageAssets[`static${level}`] = require(`../assets/gpu${level}-static.avif`);
      });

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
  width: 95vw;
  position: relative;
  scale: 0;
}
.bright {
  opacity: .8;
  scale: 0.98;
}
.mini-coins-container {
  position: absolute;
  width: 35vh;
  aspect-ratio: 1;
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
    transform: translateY(0);
  }
  100% {
    transform: translateY(-100px);
    opacity: 0;
  }
}

.spinner {
  user-select: none;
  margin: -5vh 0 1vh 0;
  animation: pulseGlow 2s infinite;
  width: 100%;
}
.clicker-show{
  scale: 1 !important;
  transition: scale .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
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