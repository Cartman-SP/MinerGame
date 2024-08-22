<template>
  <div class="friends">
    <div class="buttons">
      <div class="invite" @click="shareLink()" ref="block_first">
        <p v-if="language == 'ru'" class="name-invite">ПРИГЛАСИТЬ ДРУГА</p>
        <p v-else class="name-invite">INVITE FRIEND</p>
          <img src="../assets/icon-addfriend-friends.png" alt="" class="invite-icon">
      </div>
      <div class="link" @click="copyLink" ref="block_second">
        <p v-if="language == 'ru'" style="font-size: 10px;" class="name-invite">СКОПИРОВАТЬ ССЫЛКУ</p>
        <p v-else class="name-invite">COPY LINK</p>
        <img src="../assets/icon-link-friends.png" alt="" class="link-icon">
      </div>
    </div>

    <div class="premium">
      <div class="card" ref="block_third">
        <p v-if="language == 'ru'" class="subtitle">БЕЗ PREMIUM</p>
        <p v-else class="subtitle">NO PREMIUM</p>
        <div class="money">
          <p class="money-amount">+ 10 000</p>
          <img src="../assets/logo-small-blue.png" alt="">
        </div>
      </div>
      <div class="card" ref="block_fourth">
        <p v-if="language == 'ru'" class="subtitle">С PREMIUM</p>
        <p v-else class="subtitle">WITH PREMIUM</p>
        <div class="money">
          <p class="money-amount">+ 25 000</p>
          <img src="../assets/logo-small-blue.png" alt="">
        </div>
      </div>
    </div>

    <div class="table-container" ref="block_fifth">
      <div class="description" v-if="language == 'ru'">
        <p>ДРУЗЬЯ</p>
        <p>ДОХОД ОТ <br>РЕФЕРАЛОВ</p>
      </div>
      <div class="description" v-else>
        <p>FRIENDS</p>
        <p>PROFIT FROM <br>REFERRALS</p>
      </div>
      <div class="bottom" v-if="friends.length>0">
        <div class="bottom_card" v-for="i in friends" :key="i" @click="this.$router.push({ path: `/player/${i.user_id}`, params: { userId: i.user_id }}), this.$user.playTap()">
          <img v-if="i.photo_url" :src="i.photo_url" alt="" srcset="">
          <img v-else src="../assets/noPhoto.png">
          <div class="name_container">
            <p class="name">{{i.username || 'MINER'}}</p>
            <div class="divider"></div>
          </div>
          <div class="amount">
            <p class="amount_text" v-if="i.ispremium"> {{formatNumber(Math.floor(25000 + i.balance * 0.01))}} </p>
            <p class="amount_text" v-else> {{formatNumber(Math.floor(10000 + i.balance * 0.005))}} </p>
            <div class="number">
              <p class="number_text" v-if="i.ispremium">
                1
                <br>
                %
              </p>
              <p class="number_text" v-else>
                0.5
                <br>
                %
              </p>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="bottom">
        <h3 v-if="language == 'ru'"  class="noFriends">ТЫ ПОКА НЕ ПРИГЛАСИЛ <br> НИ ОДНОГО ДРУГА :(</h3>
        <h3 v-else class="noFriends">YOU HAVEN'T INVITED <br> ANY FRIENDS YET :(</h3>
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
      friends: [],
      alertMessage: '',
      alertColor: '',
    }
  },
  computed:{
        invite(){
            return 'https://t.me/ylionminerbot/ylionminer?startapp='+this.$user.data.user_id
        },
        language(){
          return this.$user.data.lang;
        },
    },
  methods:{
    setDefaultImage(event) {
      event.target.src = "../assets/noPhoto.png";
    },

    formatNumber(num) {
    return num >= 1_000_000 ? `${(num / 1_000_000).toFixed(1)}M` : 
           num >= 1_000 ? `${(num / 1_000).toFixed(1)}K` : 
           num.toString();
  },
    async copyLink() {
      window.Telegram.WebApp.HapticFeedback.impactOccurred('light');

      this.alertMessage = '';
      try {
        await navigator.clipboard.writeText(this.invite);
        this.alertMessage = 'Ссылка скопирована!';
        this.alertColor = '#212326';
      } catch (err) {
        console.error('Ошибка при копировании: ', err);
      }
    },
    shareLink(){
      window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
      
        const url = this.invite;
        const text = '\nПривет! Хочу пригласить тебя поиграть в классную игру, где ты сможешь создать свою собственную майнинг ферму прямо на телефоне! Развивай свою империю, добывай криптовалюту и зарабатывай вместе со мной! \nА в качестве бонуса при запуске игры тебя ждет приятное вознаграждение 💸';
        window.location.href = `https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`;
    },
    async get_friends() {
    try {
        const response = await this.$axios.get('/get_friends/', { params: { user_id: this.$user.data.user_id } });
        this.friends = response.data;
        setTimeout(() => {
          this.$user.data.toppage = false

          let index = 0;
          const blocks = [
          this.$refs.block_first,
          this.$refs.block_second,
          this.$refs.block_third,
          this.$refs.block_fourth,
          this.$refs.block_fifth
          ];

          const interval = setInterval(() => {
              if (index < blocks.length) {
                  const block = blocks[index];
                  if (block) {
                      block.classList.add('friends-block-show');
                  }
                  index++;
              } else {
                  clearInterval(interval);
              }
          }, 50);
        }, 300);
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
.noFriends{
  font-family: "Druk Wide";
  color: #FFFFFF;
  font-size: 3vw;
  margin: 30px 0;
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
  min-height: 300px;
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
  max-width: 30vw;
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
  width: 7vw;
  font-size: 3vw;
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

.friends-block-show{
  scale: 1 !important;
  opacity: 1 !important;
  transition: all .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
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
  font-size: 3.5vw;
  margin: 0;
}
.subtitle{
  color: white;
  font-family: "Druk Wide";
  font-size: 2.5vw;
  margin: 0;
}
.card{
  background-color: #171717;
  border-radius: 10px;
  padding: 15px 25px;
  width: 30vw;
  scale: 0;
  opacity: 0;
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
.name-invite{
    color: white;
    font-family: "Druk Wide";
    font-size: 3vw;
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
    scale: 0;
    opacity: 0;
}
.invite:hover, .link:hover{
  background: linear-gradient(0deg, rgb(44, 42, 41) 0%, rgb(69, 69, 70) 100%);
}
</style>