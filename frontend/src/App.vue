<template>
  <img v-if="!loaded" src="../src/assets/load.gif" style="object-fit: cover; width: 100%;height: 100%; position:absolute; z-index: 9; left:0; top:0;" alt="">
  <StatusBar/>
  <Balance/>
  <div class="loading" v-if="isLoading">
      <Loader/>
    </div>
  <div style="height: 100%;">
    <router-view/>
  </div>
  <div class="overlay" ref="overlay" v-if="showModal"></div>
  <div class="modal-app" v-if="showModal" ref="modal">
    <div v-if="modalType == 'award'">
      <p class="price">ПОКА ТЕБЯ <br> НЕ БЫЛО В ИГРЕ</p>
      <img style="margin-top: 20px; scale: .6;" src="../src/assets/logo-small-blue.png" alt="">
      <h3 class="collected">+{{ formatNumber(Math.floor(this.$user.data.mined_while_of)) }}</h3>
      <button class="ok" @click="toggleModal(), nav=true">ЗАБРАТЬ</button>
    </div>
    <div v-if="modalType == 'animations'">
      <img style="margin-top: -90px; width: 140px;" src="../src/assets/icon-interface.png" alt="">
      <p style="margin-top: 20px;" v-if="language == 'ru'" class="price">ПОКАЗЫВАТЬ АНИМАЦИИ ИНТЕРФЕЙСА?</p>
      <p style="margin-top: 20px;" v-else class="price">SHOW INTERFACE ANIMATIONS?</p>
      <button class="ok" v-if="language == 'ru'" @click="this.$user.data.hard_graphic = true, load(1)">Да, оставить</button>
      <button class="ok" v-else @click="this.$user.data.hard_graphic = true, load(1)">Yes, turn on</button>
      <button class="ok" v-if="language == 'ru'" @click="this.$user.data.hard_graphic = false, load(0)" style="background: none; border: solid 1px rgba(0,230,255,1);">Нет, отключить</button>
      <button class="ok" v-else @click="this.$user.data.hard_graphic = false, load(0)" style="background: none; border: solid 1px rgba(0,230,255,1);">No, turn off</button>
      <!--   -->
    </div>
  </div>
  
  <NavBar style="z-index: 100;" v-if="nav"/>

</template>

<script>
import Balance from '../src/components/BalanceBlock.vue';
import StatusBar from '../src/components/StatusBar.vue';
import NavBar from '../src/components/NavBar.vue';
import Loader from "../src/components/LoaderSpin.vue"; 

export default {
  components: { NavBar, StatusBar, Balance, Loader },
  data() {
    return {
      logs: '',
      loaded: false,
      showModal: false,
      nav: false,

      modalType: 'animations'
    }
  },
  computed:{
    isLoading(){
      return this.$user.data.toppage
    },
    hardGraphic(){
      return this.$user.data.hard_graphic
    },
    language(){
        return this.$user.data.lang;
    },
  },
  methods: {
    startEnergyUpdate() {
      setInterval(() => {
          const message = {
            user_id: this.$user.data.user_id,
          };
          console.log('updated')
          this.$user.data.energysocket.send(JSON.stringify(message));
      }, 6000); // каждые 6 секунд
    },

    formatNumber(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    },
    toggleModal(num){
      if (num == 2) {
        this.modalType = 'award'
      }
      if (num == 1) {
        this.modalType = 'animations'
      }

      window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      if (this.showModal) {
          const modalwindow = this.$refs.modal;
          modalwindow.classList.remove('show-app');
          const modaloverlay = this.$refs.overlay;
          modaloverlay.classList.remove('showOverlay');

          setTimeout(() => {
              this.showModal = false
          }, 400);
          

      } else {
          this.showModal = true
          setTimeout(() => {
              const modalwindow = this.$refs.modal;
              modalwindow.classList.add('show-app');
              const modaloverlay = this.$refs.overlay;
              modaloverlay.classList.add('showOverlay');
          }, 10);
      }
    },
    async copyLink() {
      try {
        await navigator.clipboard.writeText(this.link);
        // Можно добавить уведомление о копировании
        alert('Ссылка скопирована: ' + this.link);
      } catch (err) {
        console.error('Ошибка при копировании: ', err);
      }
    },

    load(condition) {
      
      if (!condition) {
        const style = document.createElement('style');
        style.innerHTML = `
          * {
            transition: all 0s !important;
          }
        `;
        document.head.appendChild(style);
        this.transitionStyleElement = style;
        this.$user.data.sound = false
        this.$user.data.vibrate = false
      }
      this.$user.playTap();

      this.toggleModal()
      setTimeout(() => {
        this.loaded = true;
        
        this.toggleModal(2)
      }, 2000); // 5 seconds delay
    }
  },
  mounted() {
    window.Telegram.WebApp.expand();
    this.toggleModal(1)
    this.startEnergyUpdate()
  },
  watch: {
    // Наблюдение за изменением this.$user.data.hard_graphic
    '$user.data.hard_graphic'(newVal) {
      if (!newVal) {
        // Если включен режим hard graphic, добавляем стиль
        const style = document.createElement('style');
        style.innerHTML = `
          * {
            transition: all 0s !important;
          }
        `;
        document.head.appendChild(style);
        this.transitionStyleElement = style;
      } else {
        // Если режим выключен, удаляем стиль
        if (this.transitionStyleElement) {
          document.head.removeChild(this.transitionStyleElement);
          this.transitionStyleElement = null;
        }
      }
    }
  },
}
</script>


<style>
.collected{
  color: white;
  font-family: "Druk Wide";
  font-size: 18px;
}
.loading{
  background: linear-gradient(180deg, rgba(84,86,85,1) 0%, rgba(50,52,51,1) 100%);
  position: absolute;
  height: 100%;
  top: 0;
  width: 100%;
  z-index: 99;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.ok{
  background: linear-gradient(180deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  border-radius: 10px;
  padding: 10px 30px;
  border: none;
  color: white;
  font-family: "Druk Wide";
  font-size: 18px;
  margin-top: 20px;
  width: 90%;
  height: 50px;
  scale: 1;
}
.ok:hover{
  scale: .8;
  filter: brightness(50%);
  transition: all .3s ease;
}

.price{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
    margin: 0;
    width: 100%;
}
.modal-app{
    background: linear-gradient(180deg, rgba(84,86,85,1) 0%, rgba(50,52,51,1) 100%);
    border-top: 2px solid #00C5FF;
    filter: drop-shadow(0 -5px 5px #00c3ff8d);
    border-radius: 10px 10px 0 0;
    padding: 20px 0;
    position: absolute;
    width: 100%;
    /* display: flex;
    align-items: center;
    flex-direction: column; */
    height: 300px;
    bottom: -400px;
    transform: translateY(0px);
    z-index: 10;
    transition: transform .5s cubic-bezier(1.000, -0.440, 0.615, 0.745);
}
.show-app{
    transform: translateY(-400px);
    transition: transform .5s ease;
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
    font-size: 20px;
    margin: 0;
}
@font-face {
  font-family: "Druk Wide";
  src: url('@/assets/drukwidecyr-bold.otf') format('opentype');
  font-weight: bold;
  font-style: normal;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  touch-action: manipulation;
}

* {
  -webkit-tap-highlight-color: transparent;
  -webkit-appearance: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -o-user-select: none;
  user-select: none;
}

img{
  pointer-events: none;
}

body{
  height: 100vh;
  overflow: hidden;
  margin: 0;
  padding: 0;
  touch-action: manipulation;
  background: linear-gradient(180deg, rgba(155,155,155,1) 0%, rgba(1,0,1,1) 40%, rgba(1,0,1,1) 50%, rgba(155,155,155,1) 100%);
  background-position-y: 30px;
}
</style>
