<template>
  <div class="spinner">
    <div class="spinners-block" >
      <img class="spinner" src="../assets/test.gif" alt="" style="user-select: none;">
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>

.spinner {
  user-select: none;
  width: 450px;
  height: 450px;
  margin: -40px 0 -30px 0;
  filter: drop-shadow(0 0 20px rgba(0, 192, 255, 1));
  animation: pulseGlow 2s infinite;
}

@keyframes pulseGlow {
  0% {
    filter: drop-shadow(0 0 20px rgba(0, 192, 255, 1));
  }
  50% {
    filter: drop-shadow(0 0 20px rgba(0, 192, 255, 0.5));
  }
  100% {
    filter: drop-shadow(0 0 20px rgba(0, 192, 255, 1));
  }
}
</style>