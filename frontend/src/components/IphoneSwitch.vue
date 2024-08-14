<template>
  <div>
    <div v-if="type == 1" @click="toggle" :class="{'switch-background-active' : isVolume, 'switch' : !(isVolume)}">
      <div class="span" v-if="type == 1" :class="{'switch-active' : isVolume, 'switch-disabled' : !isVolume}">
        <img class="switch-icon" src="../assets/icon-sound.png" alt="">
      </div>
    </div>
    <div v-if="type == 2" @click="toggle" :class="{'switch-background-active' : isVibro, 'switch' : !(isVibro)}">
      <div class="span" v-if="type == 2" :class="{'switch-active' : isVibro, 'switch-disabled' : !isVibro}">
        <img class="switch-icon" src="../assets/icon-vibration.png" alt="">
      </div>
    </div>
    <div v-if="type == 3" @click="toggle" :class="{'switch-background-active' : isHardGraphic, 'switch' : !(isHardGraphic)}">
      <div class="span" v-if="type == 3" :class="{'switch-active' : isHardGraphic, 'switch-disabled' : !isHardGraphic}">
        <img class="switch-icon" src="../assets/icon-animations.png" alt="">
      </div>
    </div>
  </div>
</template>

<style scoped>
.switch-background-active{
  background: linear-gradient(0deg, rgb(27, 187, 40) 0%,rgb(13, 191, 120) 100%);
  width: 50px;
  height: 30px;
  cursor: pointer;
  filter: drop-shadow(0 3px 3px rgb(23, 23, 23));
  -webkit-transition: .4s;
  transition: .4s;
  border-radius: 10px;
  position: relative;
}

.switch {
  position: relative;
  width: 50px;
  height: 30px;
  cursor: pointer;
  background: linear-gradient(0deg, rgb(228, 228, 228) 0%,rgb(176, 176, 176) 100%);
  filter: drop-shadow(0 3px 3px rgb(23, 23, 23));
  -webkit-transition: .4s;
  transition: .4s;
  border-radius: 10px;
}
.switch-active{
  position: absolute;
  left: 20%;
  background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  filter: drop-shadow(0 1px 3px rgb(23, 23, 23));
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80%;
  height: 30px;
  transition: all .2s ease;
}
.switch-disabled{
  position: absolute;
  left: 0;
  background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  filter: drop-shadow(0 1px 3px rgb(23, 23, 23));
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80%;
  height: 30px;
  transition: all .2s ease;
}
.switch-icon{
  width: 100%;
}

</style>

<script>
export default {
  props: {
    type: {
      type: Number,
      default: 0
    }
  },
  computed:{
    isVolume(){
      return this.$user.data.sound
    },
    isVibro(){
      return this.$user.data.vibrate
    },
    isHardGraphic(){
      return this.$user.data.hard_graphic
    },
  },
  methods: {
    toggle(){
      this.$user.playTap();
      if (this.type == 1) {
        this.switchvolume()
      } else if(this.type == 2) {
        this.switchvibro()
      } else{
        this.switchGraphic()
      }
    },

    switchGraphic(){
      this.$user.data.hard_graphic = !this.$user.data.hard_graphic
    },

    async switchvolume(){
      this.$user.data.sound = !this.$user.data.sound
      try {
        await this.$axios.post('/turnsound/', {user_id: this.$user.data.user_id,}, {withCredentials: true});
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async switchvibro(){
      this.$user.data.vibrate = !this.$user.data.vibrate
      try {
        await this.$axios.post('/turnvibrate/', {user_id: this.$user.data.user_id,}, {withCredentials: true});
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  }
};
</script>