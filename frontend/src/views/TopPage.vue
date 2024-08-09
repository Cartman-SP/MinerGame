<template>
  <div class="main">
    <div class="main_top">
      <div class="container">
        <div class="image-container">
          <img v-if="top2.photo_url" :src="top2.photo_url" alt="" class="img_small">
          <img v-else src="../assets/noPhoto.png" class="img_small">
          <div class="num">
              <p>2</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">{{top2.username || 'MINER'}}</p>
          <div class="quantity">
            <p class="quantity_text">{{formatNumber(Math.floor(top2.balance))}}</p>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="image-container">
          <img v-if="top1.photo_url" :src="top1.photo_url" alt="" class="img_big">
          <img v-else src="../assets/noPhoto.png" class="img_big">
          <div class="num">
              <p>1</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">{{top1.username || 'MINER'}}</p>
          <div class="quantity">
            <p class="quantity_text">{{formatNumber(Math.floor(top1.balance))}}</p>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="image-container">
          <img v-if="top3.photo_url" :src="top3.photo_url" alt="" class="img_smallest">
          <img v-else src="../assets/noPhoto.png" class="img_smallest">
          <div class="num">
              <p>3</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">{{top3.username || 'MINER'}}</p>
          <div class="quantity">
            <p class="quantity_text">{{formatNumber(Math.floor(top3.balance))}}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="center">
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
    <div class="bottom">
      <div class="bottom_card" v-for="(user, index) in top" :key="index">
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
            console.log(response.data, '----------')
            const top = response.data.top_users
            this.top1 = top[0]
            this.top2 = top[1]
            this.top3 = top[2]
            this.top = top.slice(3);
            this.user_position = response.data.user_position
            setTimeout(() => {
              this.$user.data.toppage = false
            }, 300);
        }catch(error){
            console.log(error)
        }
    }
  },

  computed:{
    your_balance(){
      return this.formatNumber(this.$user.data.balance)
    }
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
  padding: 5px 0 5px 0;
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
.bottom{
  display: flex;
  flex-direction: column;
  gap: 10px;
  border-top: 1px solid #00E6FF;
  margin-top: 20px;
  background: rgb(85, 85, 85);
  border-radius: 7px 7px 0 0;
  box-shadow: 0 -5px 10px rgba(0, 230, 255, 0.3);
  padding: 20px;
  min-height: 100px;
  padding-bottom: 100px;
}
.bottom_card img{
  height: 65px;
  width: 65px;
  border: 1px solid #FFFFFF;
  border-radius: 50%;
}
.name{
  color: #FFFFFF;
  text-align: left;
  font-size: 14px;
}
.bottom_card{
  display: flex;
  align-items: center;
  gap: 20px;
}
.divider {
  border-bottom: 1px solid rgba(255, 255, 255, 1); 
  width: 100%;
  margin: 0;
}
.name_container{
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
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
}
.number{
  background: #00E6FF;
  border-radius: 10px;
  padding: 10px;
  margin-left: 5px;
}
.number_text{
  color: #FFFFFF;
}
.num{
  border-radius: 50%;
}
.num p{
  font-size: 12px;
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