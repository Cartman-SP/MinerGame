<template>
  <div :class="['spinner', `level-${level}`]">
    <div class="spinners-block">
      <img class="spinner-img" src="../assets/test.gif" alt="" style="user-select: none;">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      level: 1,
    };
  },
};
</script>

<style scoped>
.spinner {
  user-select: none;
  width: 450px;
  height: 450px;
  margin: -70px 0 10px 0;
  animation: pulseGlow 2s infinite;
  --glow-color: rgba(0, 192, 255, 1); /* Default color for level 1 */
}

.level-1 {
  --glow-color: rgba(0, 192, 255, 1);
}

.level-2 {
  --glow-color: rgba(255, 0, 0, 1);
}

.level-3 {
  --glow-color: rgba(0, 255, 0, 1);
}

.level-4 {
  --glow-color: rgba(255, 105, 180, 1);
}

.level-5 {
  --glow-color: rgba(255, 255, 0, 1);
}

.level-6 {
  --glow-color: rgba(255, 255, 255, 1);
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
