<template>
  <img v-if="!loaded" src="../src/assets/load.jpg" style="object-fit: cover; width: 100%;height: 100%; position:absolute; z-index: 999; left:0; top:0;" alt="">
  <StatusBar/>
  <Balance/>
  <div style="height: 100%;">
    <router-view/>
  </div>
  <NavBar/>

</template>

<script>
import Balance from '../src/components/BalanceBlock.vue';
import StatusBar from '../src/components/StatusBar.vue';
import NavBar from '../src/components/NavBar.vue';

export default {
  components: { NavBar, StatusBar, Balance },
  data() {
    return {
      logs: '',
      loaded: false,
    }
  },
  methods: {
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
@font-face {
    font-family: "Druk Wide";
    src: url("https://db.onlinewebfonts.com/t/11289a678c4607112a7ffdb6b86812c8.eot");
    src: url("https://db.onlinewebfonts.com/t/11289a678c4607112a7ffdb6b86812c8.eot?#iefix")format("embedded-opentype"),
    url("https://db.onlinewebfonts.com/t/11289a678c4607112a7ffdb6b86812c8.woff2")format("woff2"),
    url("https://db.onlinewebfonts.com/t/11289a678c4607112a7ffdb6b86812c8.woff")format("woff"),
    url("https://db.onlinewebfonts.com/t/11289a678c4607112a7ffdb6b86812c8.ttf")format("truetype"),
    url("https://db.onlinewebfonts.com/t/11289a678c4607112a7ffdb6b86812c8.svg#Druk Wide Cy Bold Regular")format("svg");
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
  background: linear-gradient(0deg, rgba(155,155,155,1) 0%, rgba(1,0,1,1) 40%, rgba(1,0,1,1) 70%, rgba(155,155,155,1) 100%);
  background-position-y: 30px;
}
</style>
