<template>
  <div class="main">
    <div class="main_top">
      <div class="container">
        <div class="image-container">
          <img src="" alt="" class="img_small">
          <div class="num">
              <p>2</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">UserName</p>
          <div class="quantity">
            <p class="quantity_text">480M</p>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="image-container">
          <img src="" alt="" class="img_big">
          <div class="num">
              <p>1</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">UserName</p>
          <div class="quantity">
            <p class="quantity_text">480M</p>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="image-container">
          <img src="" alt="" class="img_smallest">
          <div class="num">
              <p>3</p>
          </div>
        </div>
        <div class="wrapper">
          <p class="wrapper_text">UserName</p>
          <div class="quantity">
            <p class="quantity_text">480M</p>
          </div>
        </div>
      </div>
    </div>
    <div class="center">
      <div class="center_container">
        <div class="ramka">
          <p class="ramka_text">45.6M</p>
        </div>
        <p class="center_text">YOUR BALANCE</p>
      </div>
      <div class="center_container">
        <div class="ramka">
          <p class="ramka_text">23</p>
        </div>
        <p class="center_text">YOUR RANK</p>
      </div>
    </div>
    <div class="bottom">
      <div class="bottom_card" v-for="i in top" :key="i">
        <img :src="top[i].photo_url" alt="" >
        <div class="name_container">
          <p class="name">{{top[i].username}}</p>
          <div class="divider"></div>
        </div>
        <div class="amount">
          <p class="amount_text"> {{top[i].balance}} </p>
          <div class="number">
            <p class="number_text">{{i}} 1</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      top:[],
      user_position: 0,
      numbers: [0,1]
    };
  },
  mounted(){
    this.get_top()
  },
  methods:{
    get_top(){
      try{
            console.log(this.$user.data.user_id)
            const response = this.$axios.get('/get_top/', {params:{user_id: this.$user.data.user_id}})
            console.log(response.data, '----------')
            this.top = response.data.top_users
            this.user_position = response.data.user_position
            
        }catch(error){
            console.log(error)
        }
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
  height: 100vh;
  background: rgb(85, 85, 85);
  border-radius: 7px 7px 0 0;
  box-shadow: 0 -5px 10px rgba(0, 230, 255, 0.3);
  padding: 20px;

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
  z-index: 9999;
}
img{
  object-fit: cover;
}
</style>