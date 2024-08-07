<template>
  <div :class="['spinner', `level-${level}`]">
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
      preloadedStaticPath: ''
    };
  },
  computed: {
    gifPath() {
      return require(`../assets/GPUs/lvl${this.level}/gpu${this.level}.gif`);
    },
    staticPath() {
      return require(`../assets/GPUs/lvl${this.level}/gpu${this.level}-static.png`);
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
  width: 350px;
  height: 350px;
  margin: -20px 0 10px 0;
  animation: pulseGlow 2s infinite;
  --glow-color: rgba(0, 192, 255, 1); /* Default color for level 1 */
}

.level-1 {
  --glow-color: rgba(0, 192, 255, 1);
}

.level-2 {
  --glow-color: rgba(0, 192, 255, 1);
}

.level-3 {
  --glow-color: rgba(0, 255, 0, 1);
}

.level-4 {
  --glow-color: rgba(0, 255, 0, 1);
}

.level-5 {
  --glow-color: rgba(255, 255, 0, 1);
}

.level-6 {
  --glow-color: rgba(0, 255, 0, 1);
}
.level-7 {
  --glow-color: rgb(245, 245, 29);
}
.level-8 {
  --glow-color: rgba(0, 255, 0, 1);
}
.level-9 {
  --glow-color: rgba(0, 255, 0, 1);
}
.level-10 {
  --glow-color: rgb(245, 245, 29);
}
.level-11 {
  --glow-color: rgb(255, 111, 0);
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
