<template>
  <div class="bal">
    <p class="title">ВАШ БАЛАНС:</p>
    <div class="balance-block">
      <div class="balance">
        <div class="logo-background">
          <img class="logoSmall" src="../assets/logo-small.png" alt="">
        </div>
        <div style="width: 100%;">
          <h1 class="balNum">{{ Math.floor(balance) }}</h1>
        </div>
      </div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 10px; gap: 10px;" >
      <p class="subtitle">ПРИБЫЛЬ В ЧАС:</p>
      <div class="earning">
        {{ gph*modifier }} YL
    </div>
    </div>
    
  </div>
</template>

<script>
export default {
  computed:{
    balance() {
      return this.$user.data.balance;
    },
    gph() {
      return this.$user.data.gph;
    },
    modifier(){
      return this.$user.data.modifier;
    },
  }
}
</script>

<style scoped>
.bal{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: column;
  margin-bottom: 10px;
}
.earning{

  width: fit-content;
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
}
.balance{
  width: 100%;
  display: flex;
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
.title{
  
  color: white;
  font-family: "Druk Wide";
  font-size: 8px;
  margin: 0;
  margin-top: 10px;
}
.balance-block{
  width: 80%;
  padding: 5px;
  height: 50px;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  border-radius: 35px;
  filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.balNum{
  width: 100%;
  text-align: center;
  margin: 0;
  margin-top: 15px;
  margin-bottom: 5px;
  color: white;
  font-family: "Druk Wide";
  font-size: 18px;
}
</style>