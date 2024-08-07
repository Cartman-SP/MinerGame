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
      return require(`../assets/gpu${this.level}.gif`);
    },
    staticPath() {
      return require(`../assets/gpu${this.level}-static.png`);
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
}

.spinner-img {
  width: 100%;
  height: 100%;
}
</style>
