<template>
  <div class="spinner">
    <div class="spinners-block" >
      <img class="spinner-one-fan" src="../assets/spinner-1-fan.png" alt="">
      <img class="spinner-one" src="../assets/spinner-1.png" alt="">
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
@keyframes rotate {
from {
    transform: rotate(360deg);
}
}
.spinners-block{
  width: 100%;
}
.spinner-one-fan{
  width: 70%;
  position: absolute;
  animation: rotate 1s linear infinite;
}
.spinner-one{
  width: 70%;
  position: relative;
  right: 0%;
}
</style>