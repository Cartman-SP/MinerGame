<template>
  <div class="taskpage">
    <!-- <div class="header">
        <h1 class="title">TASK</h1>
    </div> -->

    <div class="daily">
      <p v-if="language == 'ru'" class="naming">ЕЖЕДНЕВНЫЕ ЗАДАНИЯ</p>
      <p v-else class="naming">DAILY TASKS</p>
        <div class="daily-tasks">
            <div class="task" @click="toggleModal" v-if="claimed" ref="block_first">
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-calendar-task.png" alt="">
                </div>
                <p class="name" style="font-size: 10px;" v-if="language == 'ru'">ЕЖЕДНЕВНАЯ НАГРАДА</p>
                <p class="name" style="font-size: 10px;" v-else>DAILY REWARD</p>
                <div class="logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="task" @click="toggleModal" v-else ref="block_first">
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-calendar-task.png" alt="">
                </div>
                <p class="name" style="font-size: 10px;" v-if="language == 'ru'">ЕЖЕДНЕВНАЯ НАГРАДА</p>
                <p class="name" style="font-size: 10px;" v-else>DAILY REWARD</p>
                <div class="logo-background" style="background: #a0a0a0;">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="task" @click="shareLink" v-if="friends_invited<3" ref="block_second">  
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-addfriend-task.png" alt="">
                </div>
                <p class="name" v-if="language == 'ru'">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 12 000</p>
                <p class="name" v-else>INVITE 3 FRIENDS <br>+ 12 000</p>
                <div class="logo-background" style="background: #a0a0a0;">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>

            <div class="task" @click="shareLink" v-else ref="block_second">  
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-addfriend-task.png" alt="">
                </div>
                <p class="name" v-if="language == 'ru'">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 12 000</p>
                <p class="name" v-else>INVITE 3 FRIENDS <br>+ 12 000</p>
                <div class="logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>

            
            <div class="task" @click="redirectToTelegram" ref="block_telegram">
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-telegram-task.png" alt="">
                </div>
                <p class="name" v-if="language == 'ru'">ПОДПИСАТЬСЯ НА КАНАЛ<br>+ 4 000</p>
                <p class="name" v-else>SUBSCRIBE TO THE CHANNEL<br>+ 4 000</p>
                <div class="logo-background" v-if="subscribed">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
                <div class="logo-background" style="background: #a0a0a0;" v-else>
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
        </div>
        
    </div>
    <div class="other">
      <p class="naming" style="margin-top: 30px;" v-if="language == 'ru'">ЗАДАНИЯ</p>
      <p class="naming" style="margin-top: 30px;" v-else>TASKS</p>
        <div class="other-tasks"  ref="block_customs">
          <div v-for="i in tasks" :key="i">


            <div class="other-task" @click="visit_site(i.id,i.site_link)" v-if="i.typeT=='visit'">
              <p class="other-name" v-if="language == 'ru'">ПЕРЕЙТИ ПО ССЫЛКЕ <br>+ {{formatNumber(i.reward)}}</p>
              <p class="other-name" v-else>FOLLOW THE LINK <br>+ {{formatNumber(i.reward)}}</p>
                <div class="other-logo-background" v-if="i.complete">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
                <div class="other-logo-background" style="background: #a0a0a0;" v-else>
                  <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
              </div>
            </div>
            <div class="other-task" @click="shareLink" v-if="i.typeT=='invite'">
              <p class="other-name" v-if="language == 'ru'">ПРИГЛАСИТЬ {{ i.friends_toAdd }} ДРУЗЕЙ<br>+ {{formatNumber(i.reward)}}</p>
              <p class="other-name" v-else>INVITE {{ i.friends_toAdd }} FRIENDS<br>+ {{formatNumber(i.reward)}}</p>
              <div class="other-logo-background" v-if="i.complete">
                  <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
              </div>
              <div class="other-logo-background" style="background: #a0a0a0;" v-else>
                <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
            </div>
          </div>
          <div class="other-task" @click="redirectToTelegram2(i.channel_id)" v-if="i.typeT=='join'">
            <p class="other-name" v-if="language == 'ru'">ПОДПИСАТЬСЯ НА КАНАЛ<br>+ {{formatNumber(i.reward)}}</p>
            <p class="other-name" v-else>SUBSCRIBE<br>+ {{formatNumber(i.reward)}}</p>
            <div class="other-logo-background" v-if="i.complete">
                <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
            </div>
            <div class="other-logo-background" style="background: #a0a0a0;" v-else>
              <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
          </div>
        </div>


          </div>
        </div>
    </div>
    
    


    <div class="overlay" ref="overlay" @click="toggleModal" v-if="showModal"></div>
    <div class="modal" v-if="showModal" ref="modal">
        <img class="icon" src="../assets/icon-gift.png" alt="">
        <h3 v-if="language == 'ru'">ЕЖЕДНЕВНАЯ НАГРАДА</h3>
        <h3 v-else>DAILY REWARD</h3>
        <p v-if="language == 'ru'">Забирайте ежедневно приз без пропусков<br>иначе счетчик дней начнется с 1 дня</p>
        <p v-else>Collect the prize daily without skipping<br>otherwise the day counter will start from first day</p>

        <div class="awards">
          <div class="day">
            <p class="day-num" >1 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">500</p>
          </div>
          <div class="day" v-if="days>0">
            <p class="day-num">2 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">1000</p>
          </div>
          <div class="day" style="opacity: .4;" v-else>
            <p class="day-num">2 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">1000</p>
          </div>
          <div class="day" v-if="days>1">
            <p class="day-num">3 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">3000</p>
          </div>
          <div class="day" style="opacity: .4;" v-else>
            <p class="day-num">3 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">3000</p>
          </div>
          <div class="day" v-if="days>3">
            <p class="day-num">4 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">5000</p>
          </div>
          <div class="day" style="opacity: .4;" v-else>
            <p class="day-num">4 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">5000</p>
          </div>
          <div class="day" v-if="days>4">
            <p class="day-num">5 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">10 000</p>
          </div>
          <div class="day" style="opacity: .4;" v-else>
            <p class="day-num">5 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">10 000</p>
          </div>
          <div class="day" v-if="days>5">
            <p class="day-num">6 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">20 000</p>
          </div>
          <div class="day" style="opacity: .4;" v-else>
            <p class="day-num">6 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">20 000</p>
          </div>
          <div class="day" v-if="days>6">
            <p class="day-num">7 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">40 000</p>
          </div>
          <div class="day" style="opacity: .4;" v-else>
            <p class="day-num">7 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">40 000</p>
          </div>
          <div class="day" v-if="days>7">
            <p class="day-num">8 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">100 000</p>
          </div>
          <div class="day" style="opacity: .4;" v-else>
            <p class="day-num">8 DAY</p>
            <img class="logoSmall" src="../assets/logo-small-blue.png" alt="">
            <p class="amount">100 000</p>
          </div>
        </div>
        <div v-if="language == 'ru'">
          <div @click="toggleModal" class="collect" style="font-size: 10px; background: linear-gradient(180deg, rgba(84,86,85,1) 0%, rgba(50,52,51,1) 100%)" v-if="this.$user.data.daily_reward_claimed">
            БУДЕТ ДОСТУПНО ЧЕРЕЗ: {{ countdown }}
          </div>
          <div v-else class="collect" @click="toggleModal">
            ЗАБРАТЬ ПРИЗ
          </div>
        </div>
        <div v-else>
          <div @click="toggleModal" class="collect" style="font-size: 10px; background: linear-gradient(180deg, rgba(84,86,85,1) 0%, rgba(50,52,51,1) 100%)" v-if="this.$user.data.daily_reward_claimed">
            WILL BE AVAILABLE IN: {{ countdown }}
          </div>
          <div v-else class="collect" @click="toggleModal">
            CLAIM PRIZE
          </div>
        </div>
        
    </div>
    <AlertMessage :message="alertMessage" style="z-index: 200;"/>
  </div>
</template>

<script>
import AlertMessage from "../components/AlertMessage.vue";

export default {
  components: { AlertMessage },
  data() {
    return {
      showModal: false,
      tasks: [],
      alertMessage: '',
      alertColor: '',
      countdown: '',
      timer: null,
      resetTimer: null, // Таймер для сброса claimed
    };
  },
  computed: {
    days() {
      return this.$user.data.daily_reward_day;
    },
    invite() {
      return 'https://t.me/ylionminerbot/ylionminer?startapp=' + this.$user.data.user_id;
    },
    claimed() {
      return this.$user.data.daily_reward_claimed;
    },
    friends_invited() {
      return this.$user.data.friends_invited;
    },
    subscribed() {
      return this.$user.data.subscribed;
    },
    language(){
      return this.$user.data.lang;
    },
  },
  methods: {
    async fetchDailyRewardStatus() {
      try {
        const response = await this.$axios.get('/check_daily_reward_status/', {
          params: { user_id: this.$user.data.user_id }
        });
        this.$user.data.daily_reward_claimed = response.data.daily_reward_claimed;
      } catch (error) {
        console.error('Error fetching daily reward status:', error);
      }
    },
    calculateRemainingTime() {
      const nowUTC = new Date();
      const endOfDayUTC = new Date(Date.UTC(nowUTC.getUTCFullYear(), nowUTC.getUTCMonth(), nowUTC.getUTCDate(), 23, 59, 59));
      const timeDiff = endOfDayUTC - nowUTC;
      const remainingHours = Math.floor(timeDiff / (1000 * 60 * 60));
      const remainingMinutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
      const remainingSeconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
      this.countdown = `${String(remainingHours).padStart(2, '0')}:${String(remainingMinutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
    },
    startCountdown() {
      this.calculateRemainingTime();
      this.timer = setInterval(this.calculateRemainingTime, 1000);
    },
    stopCountdown() {
      clearInterval(this.timer);
    },
    startResetTimer() {
      this.resetTimer = setInterval(() => {
        const nowUTC = new Date();
        if (nowUTC.getUTCHours() === 0 && nowUTC.getUTCMinutes() === 0 && nowUTC.getUTCSeconds() === 0) {
          this.resetDailyRewardClaimed();
        }
      }, 1000); // Проверяем каждую секунду
    },
    stopResetTimer() {
      clearInterval(this.resetTimer);
    },
    async resetDailyRewardClaimed() {
      try {
        this.$user.data.daily_reward_claimed = false;
        console.log('Daily reward status reset at midnight UTC.');
      } catch (error) {
        console.error('Error resetting daily reward status:', error);
      }
    },
    async visit_site(task_id, link) {
      this.$user.playTap()
      window.open(link, '_blank');
      try {
        const response = await this.$axios.post('/sitevisited/', {
          user_id: this.$user.data.user_id,
          task_id: task_id
        }, { withCredentials: true });
        this.$user.data.balance = response.data.balance;
        const task = this.tasks.find(task => task.id === task_id);
        if (task) {
          task.complete = true;
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    formatNumber(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    },
    async gettasks() {
      try {
        const response = await this.$axios.get('/get_task/', { params: { user_id: this.$user.data.user_id } });
        this.tasks = response.data;
        console.log(this.tasks);
      } catch (error) {
        console.log(error);
      }
    },
    open_link() {
      const url = 'https://vk.com/';
      window.open(url, '_blank');
    },
    async claim_reward() {
      try {
        const response = await this.$axios.post('/claim_reward/', { user_id: this.$user.data.user_id, }, { withCredentials: true });
        this.$user.data.balance = response.data.balance;
        this.$user.data.daily_reward_claimed = response.data.daily_reward_claimed;
        this.$user.data.daily_reward_day = response.data.daily_reward_day;
        console.log("Mining end time set to:", this.$user.data.mining_end);
        this.calculateRemainingTime();
        this.startCountdown();
        this.$user.playTap()
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async check_subscribe() {
      try {
        console.log(this.$user.data.user_id);
        const response = await this.$axios.get('/check_subscribe/', { params: { user_id: this.$user.data.user_id } });
        this.$user.data.balance = response.data.balance;
        this.$user.data.subscribed = response.data.subscribed;
        this.$user.data.subscribed_money_gived = response.data.subscribed_money_gived;
      } catch (error) {
        console.log(error);
      }
    },
    redirectToTelegram() {
      this.$user.playTap()
      window.location.href = 'https://t.me/ylionminer';
      this.check_subscribe();
    },
    redirectToTelegram2(tag) {
      this.$user.playTap()
      const url = tag.slice(1);
      window.location.href = `https://t.me/${url}`;
      this.check_subscribe();
    },
    shareLink() {
      this.$user.playTap()
      const url = this.invite;
      const text = '\nПривет! Хочу пригласить тебя поиграть в классную игру, где ты сможешь создать свою собственную майнинг ферму прямо на телефоне! Развивай свою империю, добывай криптовалюту и зарабатывай вместе со мной! \nА в качестве бонуса при запуске игры тебя ждет приятное вознаграждение 💸';
      window.location.href = `https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`;
    },
    toggleModal() {
      this.$user.playTap()
      this.alertMessage = ''
      if (this.showModal) {
        if (this.$user.data.daily_reward_claimed) {
          console.log('already claimed');
          this.alertMessage = 'Награда уже получена'
          this.$user.playError()
        } else {
          this.claim_reward();
        }
        const modalwindow = this.$refs.modal;
        modalwindow.classList.remove('show');
        const modaloverlay = this.$refs.overlay;
        modaloverlay.classList.remove('showOverlay');

        setTimeout(() => {
          this.showModal = false;
        }, 400);
      } else {
        this.showModal = true;
        setTimeout(() => {
          const modalwindow = this.$refs.modal;
          modalwindow.classList.add('show');
          const modaloverlay = this.$refs.overlay;
          modaloverlay.classList.add('showOverlay');
        }, 10);
      }
    },
  },
  mounted() {
    this.check_subscribe();
    this.gettasks();
    this.startCountdown();
    this.startResetTimer();

    let index = 0;
    const blocks = [
    this.$refs.block_first,
    this.$refs.block_second,
    this.$refs.block_telegram,
    this.$refs.block_customs,
    ];

    const interval = setInterval(() => {
    if (index < blocks.length) {
        const block = blocks[index];
        if (block) {
            block.classList.add('task-block-show');
        }
        index++;
    } else {
        clearInterval(interval);
    }
    }, 50);
  },
  beforeUnmount() {
    this.stopCountdown();
    this.stopResetTimer();
  }
};
</script>






<style scoped>
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
@keyframes scale {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(0.9);
  }
  100% {
    transform: scale(1);
  }
}
.icon{
  animation: scale 2s ease infinite;
  width: 200px;
  filter: drop-shadow(0 0px 10px rgb(0, 0, 0));
}
.modal{
    background: linear-gradient(180deg, rgba(84,86,85,1) 0%, rgba(50,52,51,1) 100%);
    border-top: 2px solid #00C5FF;
    filter: drop-shadow(0 -5px 5px #00c3ff8d);
    border-radius: 10px 10px 0 0;
    padding: 20px 0;
    position: absolute;
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
    height: 550px;
    bottom: -600px;
    transform: translateY(0px);
    z-index: 10;
    transition: transform .5s cubic-bezier(1.000, -0.440, 0.615, 0.745);
}
.show{
    transform: translateY(-600px);
    transition: transform .5s cubic-bezier(0.410, 0.245, 0.025, 1.295);
}
.showOverlay{
    opacity: 1 !important;
    transition: transform .5s cubic-bezier(0.410, 0.245, 0.000, 1.365);
}
.overlay{
    opacity: 0;
    position: absolute;
    z-index: 9;
    top: 0;
    background-color: rgba(0, 0, 0, 0.551);
    height: 100vh;
    width: 100vw;
    transition: all .4s ease;
}
.modal h3{
    color: white;
    font-family: "Druk Wide";
    font-size: 14px;
    margin: 5px 0;
}

.modal p{
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    margin: 5px 0;
}
.awards{
  padding: 10px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 10px;
  grid-row-gap: 10px; 
}
.day{
  display: flex;
  flex-direction: column;
  align-items: center;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  padding: 5px;
  border-radius: 15px;
  filter: drop-shadow(0 5px 3px rgba(21, 21, 21, 0.566));
  height: fit-content;
}
.day-num{
  color: white;
  font-family: "Druk Wide";
  font-size: 16px;
  margin: 5px 0;
}
.amount{
  color: white;
  font-family: "Druk Wide";
  font-size: 12px;
  padding: 3px;
  margin: 0;
  width: 65px;
  background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  border-radius: 10px;
}
.collect{
  
  color: white;
  font-family: "Druk Wide";
  font-size: 14px;
  border-radius: 10px;
  padding: 15px 40px;
  margin: 0;
  margin-top: 20px;
  background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  filter: drop-shadow(0 0px 3px rgb(0, 0, 0));
}
.other-tasks{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(3, 1fr);
    grid-column-gap: 1%;
    grid-row-gap: 10px;
    padding: 0 4%;
    margin-bottom: 150px;
}
.task:hover{
  background: linear-gradient(0deg, rgb(44, 42, 41) 0%, rgb(69, 69, 70) 100%);
}

.other-task:hover{
  background: linear-gradient(0deg, rgb(44, 42, 41) 0%, rgb(69, 69, 70) 100%);
}
.taskpage{
    overflow-y: scroll;
    height: 70vh;
}
.naming{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
}
.daily-tasks{
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.task-icon{
    width: 25px;
}
.name{
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    margin: 0;
}
.other-name{
    color: white;
    font-family: "Druk Wide";
    font-size: 6px;
    margin: 0;
    width: 100%;
}
.daily-tasks{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    
}
.task{
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
.other-tasks{
  scale: 0;
  opacity: 0;
}
.task-block-show{
    scale: 1 !important;
    opacity: 1 !important;;
    transition: all .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
}
.other-task{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    display: flex;
    width: 95%;
    align-items: center;
    justify-content: space-between;
    padding: 5px;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.logo-background{
  width: 40px;
  height: 35px;
  background: linear-gradient(180deg, rgb(0, 166, 255) 0%, rgba(0,230,255,1) 100%);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  font-family: "Druk Wide";
  font-size: 14px;
}
.other-logo-background{
  width: 35px;
  height: 30px;
  background: linear-gradient(180deg, rgb(0, 166, 255) 0%, rgba(0,230,255,1) 100%);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  font-family: "Druk Wide";
  font-size: 14px;
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