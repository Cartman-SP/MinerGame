<template>
  <div class="profilepage">
    <!-- <div class="header">
        <h1 class="title">PROFILE</h1>
    </div> -->
    <div class="profile">
      <div @click="tochat">
        <img v-if="userData.photo_url" class="avatar" :src="userData.photo_url" alt="Avatar" @error="setDefaultImage($event)">
        <img v-else class="avatar" src="../assets/noPhoto.png" alt="Avatar" >
      </div>          
        <p class="profile-name">{{userData.username||'MINER'}}</p>
    </div>
    <div class="information">
      <div class="container" ref="block_first">
        <p class="name" v-if="language == 'ru'">БАЛАНС</p>
        <p class="name" v-else>BALANCE</p>
        <div class="info">
          <p class="value">{{ formatNumber(userData.balance) }}</p>
        </div>
      </div>
      <div class="container" ref="block_second">
        <p class="name" v-if="language == 'ru'">РАНГ</p>
        <p class="name" v-else>RANK</p>
        <div class="info">
          <p class="value">{{ ranks[userData.lvl] }}</p>
        </div>
      </div>
      <div class="container" ref="block_third">
        <p class="name" v-if="language == 'ru'">ДРУЗЕЙ</p>
        <p class="name" v-else>FRIENDS</p>
        <div class="info">
          <p class="value">{{ userData.friends_invited }}</p>
        </div>
      </div>
      <div class="container" ref="block_fourth">
        <p class="name" v-if="language == 'ru'">МИНУТ В ИГРЕ</p>
        <p class="name" v-else>MINUTES IN THE GAME</p>
        <div class="info">
          <p class="value">{{Math.floor(userData.secs_in_game/60)}}</p>
        </div>
      </div>
      <div class="container" ref="block_fifth">
        <p class="name" v-if="language == 'ru'">ПРИБЫЛЬ В ЧАС</p>
        <p class="name" v-else>PROFIT PER HOUR</p>
        <div class="info">
          <p class="value">{{ formatNumber(userData.gph) }}</p>
        </div>
      </div>
      
    </div>
    <AlertMessage :message="alertMessage" style="z-index: 200;"/>
  </div>
</template>

<script>
import AlertMessage from "../components/AlertMessage.vue";
export default {
  components: { AlertMessage } ,
  props: ['userId'],
  data(){
    return {
      ranks: ['','IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','IMMORTAL','TRADER','SHARK','WHALE'],
      userData:{}
    }
  },
  computed:{
    language(){
      return this.$user.data.lang;
    },
  },
  mounted(){
    this.get_player()

    let index = 0;
    const blocks = [
    this.$refs.block_first,
    this.$refs.block_second,
    this.$refs.block_third,
    this.$refs.block_fourth,
    this.$refs.block_fifth,
    ];

    const interval = setInterval(() => {
    if (index < blocks.length) {
        const block = blocks[index];
        if (block) {
            block.classList.add('profile-block-show');
        }
        index++;
    } else {
        clearInterval(interval);
    }
    }, 50);
  },
  methods:{
    setDefaultImage(event) {
      event.target.src = "/img/noPhoto.d73ad49f.png";
    },

    tochat(){
      if (this.userData.usertag != 'Miner') {
        window.location.href = `https://t.me/${this.userData.usertag}`
      }
    },
    async get_player() {
      try {
        const response = await this.$axios.get('/get_userprof/', {
          params: { 'user_id': this.userId }
        });
        this.userData = response.data;
        this.$user.data.toppage = false
      } catch (error) {
        console.error('Error fetching daily reward status:', error);
      }
    },
    moveTo(url){
        this.$user.playTap()
        this.$router.push(url)
      },
    formatNumber(num) {
      return num >= 1_000_000 ? `${(num / 1_000_000).toFixed(1)}M` : 
            num >= 1_000 ? `${(num / 1_000).toFixed(1)}K` : 
            num;
    },
  }
}
</script>

<style scoped>
.help{
  width: 70%;
  height: 30px;
  cursor: pointer;
  background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  filter: drop-shadow(0 1px 3px rgb(23, 23, 23));
  border-radius: 10px;
  border: none;color: white;
  font-family: "Druk Wide";
  font-size: 10px;
}
.switches{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 30px;
  width: 90%;
  margin: 5px;
}
.active{
  background: rgb(117, 182, 77);
  border-radius: 10px;
  border: 1px solid #00E6FF;
  padding: 10px 15px;
  color: white;
  font-family: "Druk Wide";
  font-size: 12px;
  margin: 0;
}
.disabled{
  background: rgb(226, 55, 55);
  border-radius: 10px;
  border: 1px solid #00E6FF;
  padding: 10px 15px;
  color: white;
  font-family: "Druk Wide";
  font-size: 12px;
  margin: 0;
}
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
  scale: 0;
  opacity: 0;

}
.profile-block-show{
    scale: 1 !important;
    opacity: 1 !important;
    transition: all .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
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