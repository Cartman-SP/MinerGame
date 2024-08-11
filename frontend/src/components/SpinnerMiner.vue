<template>
  <div :class="['spinner', `level-${level}`]" @touchstart.passive.prevent="onTouchStart">
    <div class="spinners-block">
      <img v-if="isMining" class="spinner-img" :src="preloadedGifPath" alt="Spinner GIF" style="user-select: none;">
      <img v-else class="spinner-img" :src="preloadedStaticPath" alt="Spinner GIF" style="user-select: none;">
    </div>
  </div>
</template>

<script>
export default {
  props: ['isMining', 'level'],
  data() {
    return {
      preloadedGifPath: '',
      preloadedStaticPath: '',
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
  methods: {
    
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

.spinner {
  user-select: none;
  width: 50vh;
  margin: -5vh 0 1vh 0;
  animation: pulseGlow 2s infinite;
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
  --glow-color: rgb(255, 102, 0);
}
.level-9 {
  --glow-color: rgb(255, 183, 0);
}
.level-10 {
  --glow-color: rgb(180, 29, 245);
}
.level-11 {
  --glow-color: rgb(0, 217, 255);
}

.spinner-img {
  width: 100%;
  height: 100%;
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