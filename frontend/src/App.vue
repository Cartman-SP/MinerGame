<template>
  <div v-if="!loaded" >
    <img src="../src/assets/load.jpg" style="object-fit: cover; width: 100%;height: 100%;" alt="">
  </div>
  <div v-else>
  <StatusBar/>
  <Balance/>
  <div style="height: 100%;">
    <router-view/>
  </div>
  
  <NavBar/>
  </div>

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
    load() {
      setTimeout(() => {
        this.loaded = true;
      }, 2000); // 5 seconds delay
    }
  },
  mounted() {
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
