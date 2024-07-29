<template>
  <div class="spinner">
    <div class="spinners-block" @click="tap">
      <!-- <img class="spinner-one" src="../assets/spinner-1.png" alt=""> -->
      <img class="spinner-one-fan" src="../assets/spinner-1-fan.png" alt="">
    </div>
  </div>
</template>

<script>
export default {
    methods:{
        tap(){
            this.$emit('tap')
        }
    }
}
</script>

<style scoped>
@keyframes rotate {
from {
    transform: rotate(360deg);
}
}
.spinner-one-fan{
  width: 100%;
  /* position: absolute; */
  right: 0%;
  top: 26.5%;
  animation: rotate 1s linear infinite;
}
.spinner-one{
  position: relative;
  width: 100%;
}
</style>