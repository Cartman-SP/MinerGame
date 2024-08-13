<template>
  <img v-if="!loaded" src="../src/assets/load.gif" style="object-fit: cover; width: 100%;height: 100%; position:absolute; z-index: 999; left:0; top:0;" alt="">
  <StatusBar/>
  <Balance/>
  <div class="loading" v-if="isLoading">
      <Loader/>
    </div>
  <div style="height: 100%;">
    <router-view/>
  </div>
  <div class="overlay" ref="overlay" @click="toggleModal(1)" v-if="showModal"></div>
  <div class="modal" v-if="showModal" ref="modal">
      <p  class="price">ПОКА ТЕБЯ <br> НЕ БЫЛО В ИГРЕ</p>
      <img style="margin-top: 20px; scale: .6;" src="../src/assets/logo-small-blue.png" alt="">
      <h3 class="collected">+{{ formatNumber(Math.floor(this.$user.data.mined_while_of)) }}</h3>
      <button class="ok" @click="toggleModal">ЗАБРАТЬ</button>
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
    }
  },
  computed:{
    isLoading(){
      return this.$user.data.toppage
    }
  },
  methods: {
    formatNumber(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    },
    toggleModal(){
      window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      if (this.showModal) {
          const modalwindow = this.$refs.modal;
          modalwindow.classList.remove('show');
          const modaloverlay = this.$refs.overlay;
          modaloverlay.classList.remove('showOverlay');

          setTimeout(() => {
              this.showModal = false
          }, 400);
          this.nav=true
          

      } else {
          this.showModal = true
          setTimeout(() => {
              const modalwindow = this.$refs.modal;
              modalwindow.classList.add('show');
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
    load() {
      setTimeout(() => {
        this.loaded = true;
        this.toggleModal()
      }, 2000); // 5 seconds delay
    }
  },
  mounted() {
    window.Telegram.WebApp.expand();
    this.load();
  }
}
</script>


<style>
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
    width: 70%;
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
    height: 300px;
    bottom: -400px;
    transform: translateY(0px);
    z-index: 10;
    transition: transform .5s cubic-bezier(1.000, -0.440, 0.615, 0.745);
}
.show{
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
  -webkit-tap-highlight-color: transparent; /* отключает подсветку при клике */
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
