<template>
  <div class="friends">
    <div class="buttons">
      <div class="invite" @click="shareLink()">
          <p class="name">ПРИГЛАСИТЬ ДРУГА</p>
          <img src="../assets/icon-addfriend-friends.png" alt="" class="invite-icon">
      </div>
      <div class="link">
          <p style="font-size: 10px;" class="name">СКОПИРОВАТЬ ССЫЛКУ</p>
          <img src="../assets/icon-link-friends.png" alt="" class="link-icon">
      </div>
    </div>

    <div class="premium">
      <div class="card">
        <p class="subtitle">БЕЗ PREMIUM</p>
        <div class="money">
          <p class="money-amount">+ 2 000</p>
          <img src="../assets/logo-small-blue.png" alt="">
        </div>
      </div>
      <div class="card">
        <p class="subtitle">С PREMIUM</p>
        <div class="money">
          <p class="money-amount">+ 7 000</p>
          <img src="../assets/logo-small-blue.png" alt="">
        </div>
      </div>
    </div>

    <div class="table-container">
      <div class="header">
        <span>FRIENDS</span>
        <span>ДОХОД ОТ <br>РЕФЕРАЛОВ</span>
      </div>
      <div class="table">
        <div v-for="i in friends" :key="i" >
          <div class="human">
            <div class="leftPart">
              <div class="avatar">
                <img :src="i.photo_url" alt="" srcset="">
              </div>
              <h4 class="player">
                {{i.username}}
              </h4>
            </div>
            
            <div class="earningBlock">
              <h2 class="earning" v-if="i.ispremium">
                {{Math.floor(i.balance * 0.01)}}
              </h2>
              <h2 class="earning" v-else>
                {{Math.floor(i.balance * 0.005)}}
              </h2>
              
              <h2 class="percent" v-if="i.ispremium">
                0.5
                <br>
                %
              </h2>
              <h2 class="percent" v-else>
                0.5
                <br>
                %
              </h2>
            </div>
          </div>
          <hr>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      friends: [],
    }
  },
  computed:{
        invite(){
            return 'https://t.me/M1nerGamebot/Miner?startapp='+this.$user.data.user_id
        } 
    },
  methods:{
    shareLink(){
        const url = this.invite;
        const text = '\nПривет! Хочу пригласить тебя поиграть в классную игру, где ты сможешь создать свою собственную майнинг ферму прямо на телефоне! Развивай свою империю, добывай криптовалюту и зарабатывай вместе со мной! \nА в качестве бонуса при запуске игры тебя ждет приятное вознаграждение 💸';
        window.location.href = `https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`;
    },
    async get_friends() {
    try {
        const response = await this.$axios.get('/get_friends/', { params: { user_id: this.$user.data.user_id } });
        this.friends = response.data;
        console.log(response);
        console.log(this.friends);
    } catch (error) {
        console.error(error);
    }
}

  },
  mounted(){
    this.get_friends()
  }
}
</script>

<style scoped>
.hr{
  border: 1px solid #A8A8A8;
}
.percent{
  color: #ffffff;
  font-family: "Druk Wide";
  font-size: 10px;
  margin: 0;
  background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  border-radius: 5px;
  height: 40px;
  width: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.earning{
  color: #ffffff;
  font-family: "Druk Wide";
  font-size: 10px;
  margin: 0;
}
.earningBlock{
  height: 40px;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  display: flex;
  align-items: center;
  gap: 10px;
  justify-content: space-between;
  padding: 0px 0px 0px 20px;
  border-radius: 5px;
}
.player{
  color: #272727;
  font-family: "Druk Wide";
  font-size: 8px;
  margin: 0;
}
.leftPart{
  display: flex;
  justify-content: start;
  gap: 10px;
  align-items: center;
}
.avatar img{
  width: 40px;
  aspect-ratio: 1;
  border-radius: 50%;
  background-color: red;
}
.human{
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.table{
  padding: 10px;
  background: linear-gradient(180deg, rgba(165,165,164,1) 0%, rgba(223,223,223,1) 100%);
  border-radius: 10px;
}
.header{
  display: flex;
  justify-content: space-between;
  color: white;
  font-family: "Druk Wide";
  font-size: 10px;
  margin: 0;
  align-items: center;
}
.table-container{
  padding: 10px;
  margin-bottom: 70px;
}
.money img{
  width: 16px;
}
.money{
  gap: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.money-amount{
  color: white;
  font-family: "Druk Wide";
  font-size: 14px;
  margin: 0;
}
.subtitle{
  color: white;
  font-family: "Druk Wide";
  font-size: 10px;
  margin: 0;
}
.card{
  background-color: #171717;
  border-radius: 10px;
  padding: 15px 25px;
}
.premium{
  display: flex;
  justify-content: space-between;
  padding: 10px;
}
.friends{
  overflow-y: scroll;
  height: 70vh;
}
.name{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
    margin: 0;
    width: 100%;
}
.invite-icon, .link-icon{
    width: 40px;
    height: 40px;
    background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
    border-radius: 10px;
}
.invite, .link{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 5px;
    margin: 20px 40px;
    height: 50px;
    border-radius: 15px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
</style>