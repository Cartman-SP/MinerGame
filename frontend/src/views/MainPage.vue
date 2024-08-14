<template>
  <div class="mainpage">
    
    <div>

      <div class="gpu_selections" v-if="video2_lvl">
        <div class="gpu_preview" v-for="n in this.spinnerCount" :key="n" :level="[video1_lvl,video2_lvl,video3_lvl,video4_lvl][n-1]" @click="selected_gpu = n, this.$user.playTap()">
          <img :src="staticPath([video1_lvl,video2_lvl,video3_lvl,video4_lvl][n-1])" alt="" :class="[{ currentGPU: n == selected_gpu }]">
        </div>
      </div>
      
      
      <div v-else style="margin-bottom: 50px;"></div>
      <div class="spinner-single">
        <Spinner :isMining="remainingTime > 0" 
        :level="selected_gpu == 1 ? video1_lvl : selected_gpu == 2 ? video2_lvl : selected_gpu == 3 ? video3_lvl : video4_lvl"/>
      </div>
    </div>

    <div class="stats-block">
      <div class="energy-block" @click="moveTo('/boost')">
        <p>{{ formatNumber(energy) }}/{{ formatNumber(max_energy) }}</p>
        <img src="../assets/icon-battery.png" style="width: 20px; height: 10px;" alt="">
      </div>
      <div class="timer-block" @click="mining_start" :style="getStyle">
        <p v-if="remainingTime>0" style="color: #00C0FF; font-size: 10px; margin: 0;">{{ formattedRemainingTime }}</p>
        <p v-else style="color: #00C0FF; font-size: 10px; margin: 0;">START MINING</p>
      </div>
      <div class="upgrade-block" @click="moveTo('/upgrade')">
        <p style="font-size: 8px;">UPGRADE</p>
        <img src="../assets/icon-upgrade.png" style="width: 20px; height: 20px;" alt="">
      </div>
    </div>
    <AlertMessage :message="alertMessage" style="z-index: 200;"/>
  </div>
</template>

<script>
import Spinner from '../components/SpinnerMiner.vue';
import AlertMessage from "../components/AlertMessage.vue";

export default {
  components: { Spinner, AlertMessage } ,
  data() {
    return {
      alertMessage: '',

      socket: null,
      miningSocket: null,
      energySocket: null,
      timer: null,
      
      isBright: false,
      

      selected_gpu: 2,
    };
  },
  methods: {
    
    mining_start(){
      this.$user.start_mining()
    },
    moveTo(url){
        this.$router.push(url)
        this.$user.playTap()
      },
    formatNumber(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    },


    startEnergyUpdate() {
      if(this.$user.data.$energy<=this.$user.data.max_energy){
        setInterval(() => {
          this.$user.data.energy+=1
      }, 2000); 
      }
    }, 

    staticPath(lvl) {
      switch (lvl) {
        case 1:
          return require(`../assets/gpu1-static.png`);
        case 2:
          return require(`../assets/gpu1-static.png`);
        case 3:
          return require(`../assets/gpu1-static.png`);
        case 4:
          return require(`../assets/gpu4-static.png`);
        case 5:
          return require(`../assets/gpu5-static.png`);
        case 6:
          return require(`../assets/gpu6-static.png`);
        case 7:
          return require(`../assets/gpu7-static.png`);
        case 8:
          return require(`../assets/gpu8-static.png`);
        case 9:
          return require(`../assets/gpu9-static.png`);
        case 10:
          return require(`../assets/gpu10-static.png`);
        case 11:
          return require(`../assets/gpu11-static.png`);
      }
      return 1
    }
  },
  computed: {
    getStyle() {
      return this.$user.getStyle
    },
    spinnerCount(){
      if (this.video4_lvl > 0) {
        return 4
      } else if (this.video3_lvl > 0) {
        return 3
      } else if (this.video2_lvl > 0) {
        return 2
      }
      return 1
    },

    video1_lvl(){
      return this.$user.data.video_lvl
    },
    video2_lvl(){
      return this.$user.data.video2_lvl
    },
    video3_lvl(){
      return this.$user.data.video3_lvl
    },
    video4_lvl(){
      return this.$user.data.video4_lvl
    },
    balance() {
      return this.$user.data.balance;
    },
    gph() {
      return this.$user.data.gph;
    },
    modifier(){
      return this.$user.data.modifier;
    },
    energy() {
      return this.$user.data.energy;
    },
    max_energy(){
      return this.$user.data.max_energy;
    },
    formattedRemainingTime() {
      return this.$user.formattedRemainingTime()
    },
    remainingTime(){
      return this.$user.data.remainingTime
    }
  },
  mounted() {
    this.$user.data.toppage = false
    this.selected_gpu = 1
  },
  beforeUnmount() {
    
  }
};
</script>





<style scoped>
.gpu_preview img{
  width: 13vw;
  opacity: .3;
  filter: drop-shadow(0 0px 5px #00E6FF);
}
.currentGPU{
  opacity: 1 !important;
}
.gpu_selections{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 5vh;
  background-color: #171717;
  border-radius: 20px;
  border: 1px solid #00E6FF;
}



.spinner-single {
  display: block;
  width: 100%;
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
.timer-block{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.energy-block, .timer-block, .upgrade-block{
  width: 25vw;
  padding: 5px;
  height: 10vw;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  border-radius: 10px;
  filter: drop-shadow(0 10px 10px rgb(0, 0, 0));
}
.stats-block{
  display: flex;
  justify-content: center;
  gap: 10px;
  align-items: center;
  margin-top: 0;
}

.energy-block:hover, .upgrade-block:hover{
  background: linear-gradient(0deg, rgb(44, 42, 41) 0%, rgb(69, 69, 70) 100%);
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100vw;
}
.title{
  color: white;
  font-family: "Druk Wide";
  font-size: 8px;
  margin: 0;
  margin-top: 10px;
}
</style>