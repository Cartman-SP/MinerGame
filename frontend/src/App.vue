<template>
  <StatusBar/>
  <div style="height: 100%;">
    <router-view/>
  </div>
  
  <NavBar/>
</template>

<script>
import StatusBar from '../src/components/StatusBar.vue';
import NavBar from '../src/components/NavBar.vue';
export default {
  components: { NavBar, StatusBar } ,
  data() {
    return {

    }
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
}

body{
  height: 100vh;
  overflow: hidden;
  margin: 0;
  padding: 0;
  touch-action: manipulation;
  background: linear-gradient(0deg, rgba(155,155,155,1) 0%, rgba(1,0,1,1) 30%, rgba(1,0,1,1) 50%, rgba(155,155,155,1) 100%);
  background-position-y: 30px;
}
</style>
