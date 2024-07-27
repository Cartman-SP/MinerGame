<template>
  <div class="mainpage">
    <p class="title">ВАШ БАЛАНС:</p>
    <div class="balance-block">
      <div class="balance">
        <div class="logo-background">
          <img class="logoSmall" src="../assets/logo-small.png" alt="">
        </div>
        <div>
          <h1 class="balNum">150 000 000</h1>
          <p class="subtitle">ПРИБЫЛЬ В ЧАС</p>
        </div>
      </div>
    </div>

    <div class="earning">
      250 000 YL
    </div>

    <div class="spinners-block">
      <img class="spinner-one" src="../assets/spinner-1.png" alt="">
      <img class="spinner-one-fan" src="../assets/spinner-1-fan.png" alt="">
    </div>

    <div class="stats-block">
      <div class="energy-block">
        <p>2000/2000</p>
        <img src="../assets/icon-battery.png" style="width: 25px; height: 15px;" alt="">
      </div>
      <div class="timer-block">
        <p>START MINING</p>
        <p style=" color: #00C0FF; font-size: 10px; margin: 0;">00:25:13</p>
      </div>
      <div class="upgrade-block">
        <p style="font-size: 8px;">UPRADE</p>
        <img src="../assets/icon-upgrade.png" style="width: 25px; height: 25px;" alt="">
      </div>
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
.energy-block, .upgrade-block{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.stats-block p{
  margin: 3px;
  color: white;
  font-family: "Druk Wide";
  font-size: 6px;
}

.energy-block, .timer-block, .upgrade-block{
  width: 100px;
  padding: 5px;
  height: 30px;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  border-radius: 10px;
  filter: drop-shadow(0 0px 3px rgb(0, 0, 0));
}
.stats-block{
  display: flex;
  justify-content: center;
  gap: 10px;
  align-items: center;
  margin-top: -50px;
}
.spinner-one-fan{
  width: 100%;
  position: absolute;
  right: 0%;
  top: 25%;
  animation: rotate 1s linear infinite;
}
.spinner-one{
  position: relative;
  width: 100%;
}
.earning{
  margin-top: 7px;
  padding: 3px 10px;
  background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  color: white;
  font-family: "Druk Wide";
  font-size: 8px;
  border-radius: 10px;
  filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.subtitle{
  color: white;
  font-family: "Druk Wide";
  font-size: 6px;
  margin: 0;
  margin-right: 25px;
}
.balance{
  display: flex;
  justify-content: space-between;
}
.logo-background{
  width: 50px;
  height: 50px;
  background: linear-gradient(180deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logoSmall{
  width: 35px;
  height: 25px;
}
.mainpage{
  height: 100%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title{
  color: white;
  font-family: "Druk Wide";
  font-size: 8px;
  margin: 0;
}
.balance-block{
  padding: 5px 30px 5px 5px;
  height: 50px;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  border-radius: 35px;
  width: fit-content;
  filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.balNum{
  margin: 0;
  margin-top: 15px;
  margin-bottom: 5px;
  margin-left: 20px;
  color: white;
  font-family: "Druk Wide";
  font-size: 18px;
}
</style>