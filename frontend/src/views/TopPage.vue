<template>
  <div class="main">
    <div class="main_top">
      <div class="container" ref="block_second" @click="this.$user.data.toppage=true,this.$router.push({ path: `/player/${top2.user_id}`, params: { userId: top2.user_id }}), this.$user.playTap()">
        <div class="image-container">
          <img v-if="top2.photo_url" :src="top2.photo_url" alt="" class="img_small">
          <img v-else src="../assets/noPhoto.png" class="img_small">
          <div class="num">
              <p>2</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">{{top2.username || 'MINER'}}</p>
          <div class="quantity" style="background-color: rgb(225, 215, 215);">
            <p class="quantity_text">{{formatNumber(Math.floor(top2.balance))}}</p>
          </div>
        </div>
      </div>
      <div class="container" ref="block_first" @click="this.$user.data.toppage=true,this.$router.push({ path: `/player/${top1.user_id}`, params: { userId: top1.user_id }}), this.$user.playTap()">
        <div class="image-container">
          <img v-if="top1.photo_url" :src="top1.photo_url" alt="" class="img_big">
          <img v-else src="../assets/noPhoto.png" class="img_big">
          <div class="num">
              <p>1</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">{{top1.username || 'MINER'}}</p>
          <div class="quantity" style="background-color: rgb(212, 196, 51);">
            <p class="quantity_text">{{formatNumber(Math.floor(top1.balance))}}</p>
          </div>
        </div>
      </div>
      <div class="container" ref="block_third" @click="this.$user.data.toppage=true,this.$router.push({ path: `/player/${top3.user_id}`, params: { userId: top3.user_id }}), this.$user.playTap()">
        <div class="image-container">
          <img v-if="top3.photo_url" :src="top3.photo_url" alt="" class="img_smallest">
          <img v-else src="../assets/noPhoto.png" class="img_smallest">
          <div class="num">
              <p>3</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">{{top3.username || 'MINER'}}</p>
          <div class="quantity" style="background-color: rgb(167, 115, 88);">
            <p class="quantity_text">{{formatNumber(Math.floor(top3.balance))}}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="center" v-if="language == 'ru'">
      <div class="center_container">
        <div class="ramka">
          <p class="ramka_text">{{ your_balance }}</p>
        </div>
        <p class="center_text">ТВОЙ БАЛАНС</p>
      </div>
      <div class="center_container">
        <div class="ramka">
          <p class="ramka_text">{{ user_position }}</p>
        </div>
        <p class="center_text">ТВОЯ ПОЗИЦИЯ</p>
      </div>
    </div>
    <div class="center" v-else>
      <div class="center_container">
        <div class="ramka">
          <p class="ramka_text">{{ your_balance }}</p>
        </div>
        <p class="center_text">YOUR BALANCE</p>
      </div>
      <div class="center_container">
        <div class="ramka">
          <p class="ramka_text">{{ user_position }}</p>
        </div>
        <p class="center_text">YOUR RANK</p>
      </div>
    </div>
    <div class="description" v-if="language == 'ru'">
      <p>ИГРОКИ</p>
      <p>БАЛАНС/МЕСТО</p>
    </div>
    <div class="description" v-else>
      <p>PLAYERS</p>
      <p>BALANCE/PLACE</p>
    </div>
    <div class="bottom">
      <div class="bottom_card" v-for="(user, index) in top" :key="index" @click="this.$user.data.toppage=true,this.$router.push({ path: `/player/${user.user_id}`, params: { userId: user.user_id }}), this.$user.playTap()">
        <img v-if="user.photo_url" :src="user.photo_url" alt="" >
        <img v-else src="../assets/noPhoto.png">
        <div class="name_container">
          <p class="name">{{user.username || 'MINER'}}</p>
          <div class="divider"></div>
        </div>
        <div class="amount">
          <p class="amount_text"> {{formatNumber(Math.floor(user.balance))}} </p>
          <div class="number">
            <p class="number_text">{{4 + index}}</p>
          </div>
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
  data() {
    return {
      top:[],
      user_position: 0,
      top1:NaN,
      top2:NaN,
      top3:NaN,
    };
  },
   mounted(){
    this.get_top()

    
  },

  methods:{
    formatNumber(num) {
    return num >= 1_000_000 ? `${(num / 1_000_000).toFixed(1)}M` : 
           num >= 1_000 ? `${(num / 1_000).toFixed(1)}K` : 
           num.toString();
  },

    async get_top(){
      try{
        console.log(this.$user.data.user_id)
        const response = await this.$axios.get('/get_top/', {params:{user_id: this.$user.data.user_id}})
        const top = response.data.top_users
        this.top1 = top[0]
        this.top2 = top[1]
        this.top3 = top[2]
        this.top = top.slice(3);
        console.log(this.top)
        this.user_position = response.data.user_position
        setTimeout(() => {
          this.$user.data.toppage = false
          let index = 0;
          const blocks = [
          this.$refs.block_first,
          this.$refs.block_second,
          this.$refs.block_third,
          ];

          const interval = setInterval(() => {
          if (index < blocks.length) {
              const block = blocks[index];
              if (block) {
                  block.classList.add('top-block-show');
              }
              index++;
          } else {
              clearInterval(interval);
          }
          }, 50);
        }, 300);
      }catch(error){
          console.log(error)
      }
    }
  },

  computed:{
    your_balance(){
      return this.formatNumber(Math.floor(this.$user.data.balance))
    },
    language(){
      return this.$user.data.lang;
    },
  }
}
</script>

<style scoped>


p{
  margin: 0;
  font-family: "Druk Wide";
}
.container{
  display: flex;
  flex-direction: column;
  justify-content: end;
  gap: 20px;
  align-items: center;
  height: 180px;
  
  scale: 0;
  opacity: 0;
}
.main{
  display: flex;
  flex-direction: column;
  gap: 10px;
  height: 70vh;
  overflow-y: scroll;
}
.main_top{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
}
.main_top img{
  border-radius: 100px;
  border: 1px solid #00E6FF;
  object-fit: cover;
}
.img_small{
  width: 80px;
  aspect-ratio: 1;
}
.img_big{
  width: 100px;
  aspect-ratio: 1;
}
.img_smallest{
  width: 70px;
  aspect-ratio: 1;
}
.wrapper_text{
  color: #FFFFFF;
  font-size: 12px;
  width: 70px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.quantity{
  background: #00E6FF;
  border-radius: 25px;
  padding: 5px;
}
.quantity_text{
  color: #FFFFFF;
  font-size: 12px;
}
.wrapper{
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.top-block-show{
    scale: 1 !important;
    opacity: 1 !important;;
    transition: all .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
}
.center{
  display: flex;
  gap: 15px;
  justify-content: center;
}
.center_container{
  background: rgb(80, 80, 80);
  padding: 5px 20px;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  width: 130px;
}
.ramka{
  border: 1px solid #00E6FF;
  border-radius: 10px;
  padding: 5px 15px;
}
.ramka_text{
  color: #FFFFFF;
  font-size: 12px;
}
.center_text{
  color: #FFFFFF;
  font-size: 8px;
}

.description{
  font-family: "Druk Wide";
  display: flex;
  align-items: center;
  justify-content: space-between; 
  margin-top: 20px;
  padding: 0 10px;
}
.description p{
  color: #FFFFFF;
  font-size: 3vw;
  margin: 0;
}

.bottom{
  display: block;
  border-top: 1px solid #00E6FF;
  background: rgb(85, 85, 85);
  border-radius: 7px 7px 0 0;
  box-shadow: 0 -5px 10px rgba(0, 230, 255, 0.3);
  padding: 20px;
  padding-bottom: 70px;
  margin-bottom: 50px;
}
.bottom_card img{
  height: 65px;
  width: 65px;
  border: 1px solid #FFFFFF;
  border-radius: 50%;
}
.name{
  font-family: "Druk Wide";
  color: #FFFFFF;
  text-align: left;
  font-size: 3.5vw;
  max-width: 25vw;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
.bottom_card{
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 10px;
}
.divider {
  border-bottom: 1px solid rgba(255, 255, 255, 1); 
  width: 100%;
  margin: 0;
}
.name_container{
  width: 100%;
  display: flex;
  gap: 3vh;
  flex-direction: column;
}
.amount{
  padding-left: 10px;
  background: rgb(65, 65, 65);
  display: flex;
  align-items: center;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.6);
}
.amount_text{
  color: #FFFFFF;
  font-family: "Druk Wide";
  font-size: 3vw;
}
.number{
  background: #00E6FF;
  border-radius: 10px;
  padding: 10px;
  margin-left: 5px;
  font-family: "Druk Wide";
  height: 7vw;
  width: 8vw;
  font-size: 4vw;
}
.number_text{
  font-family: "Druk Wide";
  color: #FFFFFF;
  margin: 0;
}
.num{
  border-radius: 50%;
  font-family: "Druk Wide";
}
.num p{
  font-size: 3vw;
}
.image-container {
  position: relative;
  display: inline-block;
}

.num {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 20px;
  width: 20px;
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%); 
  border-radius: 10px; 
  color: white;
  background: #00E6FF;
  z-index: 10;
}
img{
  object-fit: cover;
}
</style>