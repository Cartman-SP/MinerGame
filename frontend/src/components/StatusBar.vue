<template>
  <div>
    <div class="statusBar" v-if="this.$route.path === '/'">

        <div class="profile"  @click="moveTo('/profile')" ref="profile">
          <img v-if="avatar" class="avatar" :src="avatar" alt="Avatar" @error="setDefaultImage($event)">
          <img v-else class="avatar" src="../assets/noPhoto.png" alt="Avatar">
          <p class="name">{{username || 'MINER'}}</p>
        </div>

        <div style="width: 120px;">
            <img class="logo" ref="logo" src="../assets/logo.png" alt="logo">
        </div>
        
        <div class="level" @click="moveTo('/ranks')" ref="level">
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
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.path === '/ranks'">
      <h1 class="title">RANK</h1>
    </div>
    <div class="statusBar" style="justify-content: center;" v-if="this.$route.name === 'player'">
      <h1 class="title">PLAYER</h1>
    </div>
  </div>
    
  </template>
  
  <script>
  export default {
    data(){
      return{
        next_lvl: [0,17500,90000,400000 ,5000000,22000000,100000000 ,510000000 ,800000000,1800000000],
        ranks: ['','IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','IMMORTAL','TRADER','SHARK','WHALE']
      }
    },
    methods:{
      setDefaultImage(event) {
      event.target.src = "/img/noPhoto.d73ad49f.png";
    },

      moveTo(url){
        this.$user.playTap()
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
      },
      
    },
    watch: {
      '$route.path'() {
        setTimeout(() => {
          const profileblock = this.$refs.profile;
          if (profileblock) {
            profileblock.classList.add('profile-show');
          }

          const logo = this.$refs.logo;
          if (logo) {
            logo.classList.add('logo-show');
          }

          const levelblock = this.$refs.level;
          if (levelblock) {
            levelblock.classList.add('level-show');
          }
        }, 10);
      }
    },
    mounted(){
      setTimeout(() => {
        const profileblock = this.$refs.profile;
        if (profileblock) {
          profileblock.classList.add('profile-show');
        }

        const logo = this.$refs.logo;
        if (logo) {
          logo.classList.add('logo-show');
        }

        const levelblock = this.$refs.level;
        if (levelblock) {
          levelblock.classList.add('level-show');
        }
      }, 10);
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
    transform: translateY(-100px);
  }

  .logo-show{
    transform: translateY(0px);
    transition: transform .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
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
    object-fit: cover;
  }

  .profile{
    width: 120px;
    height: 50px;
    border-radius: 15px;
    padding: 5px;
    color: white;
    font-family: "Druk Wide";
    font-size: 2.5vw;
    display: flex;
    gap: 5px;
    align-items: center;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    transform: translateX(-100px);
  }

  .level{
    height: 50px;
    width: 120px;
    border-radius: 15px;
    padding: 5px;
    color: white;
    font-family: "Druk Wide";
    font-size: 2vw;
    align-items: center;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    transform: translateX(100px);
  }
  .profile-show{
    transform: translateX(0);
    transition: transform .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
  }
  .level-show{
    transform: translateX(0);
    transition: transform .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
  }
  </style>