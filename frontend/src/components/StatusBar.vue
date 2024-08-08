<template>
  <div>
    <div class="statusBar" v-if="this.$route.path === '/'">
        <div class="profile"  @click="moveTo('/profile')">
          <img v-if="avatar" class="avatar" :src="avatar" alt="Avatar">
          <img v-else class="avatar" src="../assets/noPhoto.png" alt="Avatar">
          <p class="name">{{username || 'MINER'}}</p>
        </div>
        <div style="width: 120px;">
            <img class="logo" src="../assets/logo.png" alt="logo">
        </div>
        
        <div class="level">
            <p class="levelName">{{ranks[lvl] || 'RANK'}}</p>
            <div class="lineContainer" v-if="lvl<10">
              <div class="line" :style="lineStyle" ></div>
            </div>
            <div class="lineContainer" v-else>
              <div class="line" style="width:100%;" ></div>
            </div>
            <p v-if="lvl<10" class="goals">{{ lvl }}/10</p>
        </div>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/profile'">
      <h1 class="title">PROFILE</h1>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/wallet'">
      <h1 class="title">WALLET</h1>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/task'">
      <h1 class="title">TASKS</h1>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/friends'">
      <h1 class="title">FRIENDS</h1>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/top'">
      <h1 class="title">TOP</h1>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/upgrade'">
      <h1 class="title">UPGRADE</h1>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/boost'">
      <h1 class="title">BOOST</h1>
    </div>
  </div>
    
  </template>
  
  <script>
  export default {
    data(){
      return{
        next_lvl: [0,17500,90000,400000 ,5000000,650000,100000000 ,510000000 ,1600000000,3800000000],
        ranks: ['','IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','IMMORTAL','TRADER','SHARK','WHALE']
      }
    },
    methods:{
      moveTo(url){
        window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
        this.$router.push(url)
      }
    },
    computed:{
      username(){
        return this.$user.data.username
      },
      lvl(){
        return this.$user.data.lvl
      },
      avatar(){
        return this.$user.data.avatar
      },
      lineStyle() {
      return {
        width: (this.$user.data.balance / this.next_lvl[this.$user.data.lvl])*100 +'%'
      }
    }
    }
  }
  </script>
  
  <style scoped>
  .lineContainer{
    border: 1px solid #404040;
    height: 8px;
  }
  .line{
    height: 6px;
    background-color: #00E6FF;
  }
  .name{
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow:hidden !important;
    width: 100px;
  }
  .levelName{
    margin-bottom: 0;
  }
  .goals{
    margin-top: 0;
  }
  .title{
    color: white;
    font-family: "Druk Wide";
    font-size: 18px;
    margin: 0;
  }
  
  .logo{
    width: 100%;
    scale: .8;
  }
  .statusBar{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #383637;
    padding: 2px 10px;
    height: 60px;
  }
  .avatar{
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid #00E6FF;
  }

  .profile{
    width: 120px;
    height: 50px;
    border-radius: 15px;
    padding: 5px;
    color: white;
    font-family: "Druk Wide";
    font-size: 10px;
    display: flex;
    gap: 5px;
    align-items: center;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  }

  .level{
    height: 50px;
    width: 120px;
    border-radius: 15px;
    padding: 5px;
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    align-items: center;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  }
  </style>