<template>
  <div class="profilepage">
    <!-- <div class="header">
        <h1 class="title">PROFILE</h1>
    </div> -->
    <div class="profile"  @click="this.$router.push('/profile')">
        <img v-if="user.avatar" class="avatar" :src="user.avatar" alt="Avatar">
        <img v-else class="avatar" src="../assets/noPhoto.png" alt="Avatar">
        <p class="profile-name">{{user.username||'MINER'}}</p>
    </div>
    <div class="information">
      <div class="container">
        <p class="name">БАЛАНС</p>
        <div class="info">
          <p class="value">{{ formatNumber(user.balance) }}</p>
        </div>
      </div>
      <div class="container">
        <p class="name">РАНГ</p>
        <div class="info">
          <p class="value">{{ ranks[user.lvl] }}</p>
        </div>
      </div>
      <div class="container">
        <p class="name">ДРУЗЕЙ</p>
        <div class="info">
          <p class="value">{{ user.friends_invited }}</p>
        </div>
      </div>
      <div class="container">
        <p class="name">МИНУТ В ИГРЕ</p>
        <div class="info">
          <p class="value">{{Math.floor(user.secs_in_game/60)}}</p>
        </div>
      </div>
      <div class="container">
        <p class="name">ПРИБЫЛЬ В ЧАС</p>
        <div class="info">
          <p class="value">{{ formatNumber(user.gph) }}</p>
        </div>
      </div>
    </div>
    <AlertMessage :message="alertMessage" :color="alertColor"/>
  </div>
</template>

<script>
import AlertMessage from "../components/AlertMessage.vue";
export default {
  components: { AlertMessage } ,
  data(){
    return {
      ranks: ['','IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','IMMORTAL','TRADER','SHARK','WHALE']
    }
  },
  computed:{
    user(){
        return this.$user.data
    }
  },
  methods:{
    formatNumber(num) {
    return num >= 1_000_000 ? `${(num / 1_000_000).toFixed(1)}M` : 
           num >= 1_000 ? `${(num / 1_000).toFixed(1)}K` : 
           num.toString();
  },
  }
}
</script>

<style scoped>
.profilepage{
  overflow-y: scroll;
  height: 70vh;
}
.avatar{
  width: 70px;
  height: 70px;
  border-radius: 50%;
  border: 2px solid #00E6FF;
}
.profile-name{
  color: white;
  font-family: "Druk Wide";
  font-size: 10px;
  margin-top: 10px;
}

.profile{
  width: 100%;
  height: fit-content;
  color: white;
  font-family: "Druk Wide";
  font-size: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  align-items: center;
  margin-bottom: 20px;
}
.value{
  background: rgb(37, 37, 37);
  border-radius: 10px;
  border: 1px solid #00E6FF;
  padding: 10px 15px;
  color: white;
  font-family: "Druk Wide";
  font-size: 12px;
  margin: 0;
  width: 90px;
}
.information{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
  gap: 10px;
  margin-bottom: 150px;
}
.name{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
    margin: 0;
    margin-left: 10px;
}

.container{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    display: flex;
    width: 90%;
    align-items: center;
    justify-content: space-between;
    padding: 5px;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.header{
    width: 100%;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.title{
    width: fit-content;
    padding: 5px 50px;
    height: 30px;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    color: white;
    font-family: "Druk Wide";
    font-size: 16px;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 25px;
}
</style>