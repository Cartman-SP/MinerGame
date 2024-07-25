<template>
  <div class="rooms">
    <div class="room" v-for="r in rooms" :key="r.id">
      <img src="https://art.kartinkof.club/uploads/posts/2023-07/1688879562_art-kartinkof-club-p-komnata-geimera-art-22.jpg" alt="">
      <div class="room-info">
        <h1 style="color: #7D7D7D;">Lvl: {{r.lvl}}</h1>
        <h1>+{{ calculate(r) }} / час</h1>
        <button class="btn-upgrade" @click="toggleUpgrade(r)">Upgrade</button>
      </div>
    </div>
    <div class="room" v-for="er in emptyRooms" :key="er.id">
      <div class="room-image-wrapper">
        <img src="https://art.kartinkof.club/uploads/posts/2023-07/1688879562_art-kartinkof-club-p-komnata-geimera-art-22.jpg" alt="">
        <svg class="lock-icon" width="70" height="92" viewBox="0 0 70 92" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M35 70.0952C37.3206 70.0952 39.5462 69.1721 41.1872 67.5289C42.8281 65.8858 43.75 63.6571 43.75 61.3333C43.75 56.4705 39.8125 52.5714 35 52.5714C32.6794 52.5714 30.4538 53.4946 28.8128 55.1377C27.1719 56.7809 26.25 59.0095 26.25 61.3333C26.25 63.6571 27.1719 65.8858 28.8128 67.5289C30.4538 69.1721 32.6794 70.0952 35 70.0952ZM61.25 30.6667C63.5706 30.6667 65.7962 31.5898 67.4372 33.233C69.0781 34.8761 70 37.1048 70 39.4286V83.2381C70 85.5619 69.0781 87.7905 67.4372 89.4337C65.7962 91.0769 63.5706 92 61.25 92H8.75C6.42936 92 4.20376 91.0769 2.56282 89.4337C0.921872 87.7905 0 85.5619 0 83.2381V39.4286C0 34.5657 3.9375 30.6667 8.75 30.6667H13.125V21.9048C13.125 16.0953 15.4297 10.5237 19.532 6.41576C23.6344 2.30782 29.1984 0 35 0C37.8727 0 40.7172 0.566584 43.3712 1.6674C46.0252 2.76822 48.4367 4.38171 50.468 6.41576C52.4992 8.4498 54.1105 10.8646 55.2099 13.5222C56.3092 16.1798 56.875 19.0282 56.875 21.9048V30.6667H61.25ZM35 8.7619C31.519 8.7619 28.1806 10.1466 25.7192 12.6114C23.2578 15.0761 21.875 18.4191 21.875 21.9048V30.6667H48.125V21.9048C48.125 18.4191 46.7422 15.0761 44.2808 12.6114C41.8194 10.1466 38.481 8.7619 35 8.7619Z" fill="white"/>
        </svg>

      </div>
      <div class="room-info">
        <h1 style="color: #7D7D7D;">Lvl: {{er + rooms.length}}</h1>
      </div>
    </div>

    <div v-if="dialog" :class="{'dialog' : dialogClass, 'dialog-hide' : !dialogClass}">
      <div class="upgrade-content">
        <div class="cancel" @click="toggleUpgrade" style="margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
          <h3>Upgrades</h3>
          <svg width="13" height="13" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12.0857 10L20 17.9143V20H17.9143L10 12.0857L2.08571 20H0V17.9143L7.91429 10L0 2.08571V0H2.08571L10 7.91429L17.9143 0H20V2.08571L12.0857 10Z" fill="white"/>
          </svg>
        </div>
        <div class="blocks">
          <div class="up-block">
            <img src="https://avatars.dzeninfra.ru/get-zen_doc/1538903/pub_5c8b3fb6e05e9f00b3c70b14_5c8ea970cc852f00b446c57d/scale_1200" alt="">
            <div>
              <h3>Computer</h3>
              <div class="row">
                <p>Income {{ comp_current }}</p>
                <svg width="25" height="15" viewBox="0 0 36 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M22.9091 0C26.381 0 29.7107 1.36964 32.1658 3.80761C34.6208 6.24558 36 9.55219 36 13C36 16.4478 34.6208 19.7544 32.1658 22.1924C29.7107 24.6304 26.381 26 22.9091 26C19.4372 26 16.1074 24.6304 13.6524 22.1924C11.1974 19.7544 9.81818 16.4478 9.81818 13C9.81818 9.55219 11.1974 6.24558 13.6524 3.80761C16.1074 1.36964 19.4372 0 22.9091 0ZM22.9091 22.75C25.513 22.75 28.0103 21.7228 29.8516 19.8943C31.6929 18.0658 32.7273 15.5859 32.7273 13C32.7273 10.4141 31.6929 7.93419 29.8516 6.10571C28.0103 4.27723 25.513 3.25 22.9091 3.25C20.3051 3.25 17.8079 4.27723 15.9666 6.10571C14.1253 7.93419 13.0909 10.4141 13.0909 13C13.0909 15.5859 14.1253 18.0658 15.9666 19.8943C17.8079 21.7228 20.3051 22.75 22.9091 22.75ZM3.27273 13C3.27273 17.2412 6.00545 20.8487 9.81818 22.1812V25.5775C4.17273 24.1313 0 19.0613 0 13C0 6.93875 4.17273 1.86875 9.81818 0.4225V3.81875C6.00545 5.15125 3.27273 8.75875 3.27273 13Z" fill="#EB95F9"/>
                </svg>
              </div>
              <p style="color: rgb(255, 255, 255);">Lvl {{ comp_lvl }}</p>
            </div>
            <button @click="upgrade('comp', room_id, comp_to_upgrade)" v-if="comp_lvl<4" class="btn-upgrade" style="width: 100%; margin-top: 10px;">{{comp_to_upgrade}}</button>
            <button v-else class="btn-upgrade-disabled" style="width: 100%; margin-top: 10px;">Max lvl</button>
          </div>

          <div class="up-block">
            <img src="../../static/imgs/mic.png" alt="">
            <div>
              <h3>Microphone</h3>
              <div class="row">
                <p>Income {{ mic_current}}</p>
                <svg width="25" height="15" viewBox="0 0 36 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M22.9091 0C26.381 0 29.7107 1.36964 32.1658 3.80761C34.6208 6.24558 36 9.55219 36 13C36 16.4478 34.6208 19.7544 32.1658 22.1924C29.7107 24.6304 26.381 26 22.9091 26C19.4372 26 16.1074 24.6304 13.6524 22.1924C11.1974 19.7544 9.81818 16.4478 9.81818 13C9.81818 9.55219 11.1974 6.24558 13.6524 3.80761C16.1074 1.36964 19.4372 0 22.9091 0ZM22.9091 22.75C25.513 22.75 28.0103 21.7228 29.8516 19.8943C31.6929 18.0658 32.7273 15.5859 32.7273 13C32.7273 10.4141 31.6929 7.93419 29.8516 6.10571C28.0103 4.27723 25.513 3.25 22.9091 3.25C20.3051 3.25 17.8079 4.27723 15.9666 6.10571C14.1253 7.93419 13.0909 10.4141 13.0909 13C13.0909 15.5859 14.1253 18.0658 15.9666 19.8943C17.8079 21.7228 20.3051 22.75 22.9091 22.75ZM3.27273 13C3.27273 17.2412 6.00545 20.8487 9.81818 22.1812V25.5775C4.17273 24.1313 0 19.0613 0 13C0 6.93875 4.17273 1.86875 9.81818 0.4225V3.81875C6.00545 5.15125 3.27273 8.75875 3.27273 13Z" fill="#EB95F9"/>
                </svg>
              </div>
              <p style="color: rgb(255, 255, 255);">Lvl {{ mic_lvl }}</p>
            </div>
            <button @click="upgrade('mic', room_id, mic_to_upgrade)" v-if="mic_lvl<4" class="btn-upgrade" style="width: 100%; margin-top: 10px;">{{mic_to_upgrade}}</button>
            <button v-else class="btn-upgrade-disabled" style="width: 100%; margin-top: 10px;">Max lvl</button>
          </div>

          <div class="up-block">
            <img src="https://i.pinimg.com/originals/cc/74/9e/cc749ededc077309f29421d3cb727927.png" alt="">
            <div>
              <h3>Camera</h3>
              <div class="row">
                <p>Income {{ cam_current}}</p>
                <svg width="25" height="15" viewBox="0 0 36 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M22.9091 0C26.381 0 29.7107 1.36964 32.1658 3.80761C34.6208 6.24558 36 9.55219 36 13C36 16.4478 34.6208 19.7544 32.1658 22.1924C29.7107 24.6304 26.381 26 22.9091 26C19.4372 26 16.1074 24.6304 13.6524 22.1924C11.1974 19.7544 9.81818 16.4478 9.81818 13C9.81818 9.55219 11.1974 6.24558 13.6524 3.80761C16.1074 1.36964 19.4372 0 22.9091 0ZM22.9091 22.75C25.513 22.75 28.0103 21.7228 29.8516 19.8943C31.6929 18.0658 32.7273 15.5859 32.7273 13C32.7273 10.4141 31.6929 7.93419 29.8516 6.10571C28.0103 4.27723 25.513 3.25 22.9091 3.25C20.3051 3.25 17.8079 4.27723 15.9666 6.10571C14.1253 7.93419 13.0909 10.4141 13.0909 13C13.0909 15.5859 14.1253 18.0658 15.9666 19.8943C17.8079 21.7228 20.3051 22.75 22.9091 22.75ZM3.27273 13C3.27273 17.2412 6.00545 20.8487 9.81818 22.1812V25.5775C4.17273 24.1313 0 19.0613 0 13C0 6.93875 4.17273 1.86875 9.81818 0.4225V3.81875C6.00545 5.15125 3.27273 8.75875 3.27273 13Z" fill="#EB95F9"/>
                </svg>
              </div>
              <p style="color: rgb(255, 255, 255);">Lvl {{ cam_lvl }}</p>
            </div>
            <button @click="upgrade('webcam', room_id, cam_to_upgrade)" v-if="cam_lvl<4" class="btn-upgrade" style="width: 100%; margin-top: 10px;">{{cam_to_upgrade}}</button>
            <button v-else class="btn-upgrade-disabled" style="width: 100%; margin-top: 10px;">Max lvl</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getUpgradePrices } from '../../upgrade.js'
import { calculateTotalIncome } from '../../calculate'
export default {
  data(){
    return{
      dialog: false,
      dialogClass: false,

      comp_to_upgrade: null,
      mic_to_upgrade: null,
      cam_to_upgrade: null,

      comp_current: null,
      mic_current: null,
      cam_current: null,

      comp_lvl: null,
      mic_lvl: null,
      cam_lvl: null,

      room_id: null,
      room_data: null,
    }
  },
  methods:{
    calculate(r){
      let arr = [r]
      return calculateTotalIncome(arr)
    },

    toggleUpgrade(data){
      if (this.dialog) {
        this.dialogClass = false;

        setTimeout(() => {
          this.dialog = false;
        }, 200);
        
      }else{
        this.room_data = data
        this.dialog = true;
        let context = getUpgradePrices(data);

        this.comp_to_upgrade = context.comp_up;
        this.mic_to_upgrade = context.micro_up;
        this.cam_to_upgrade = context.webcam_up;

        this.comp_current = context.comp_cur;
        this.mic_current = context.micro_cur;
        this.cam_current = context.webcam_cur;

        this.comp_lvl = data.comp_lvl
        this.mic_lvl = data.micro_lvl
        this.cam_lvl = data.webcam_lvl

        this.room_id = data.id

        setTimeout(() => {
          this.dialogClass = true;
        }, 10);
      }
      console.log(this.dialog, this.dialogClass)
      
    },
    update_lvls(){
      let new_room = {}
      console.log(5555555555555555555555555,this.$store.state.rooms)
      for(let room in this.$store.state.rooms){
        console.log(room,'---',this.$store.state.rooms[room],'|||||',this.room_data.id)
        if(this.$store.state.rooms[room].id==this.room_data.id){
          new_room = this.$store.state.rooms[room]
        }
      }
      console.log(new_room)
      let context = getUpgradePrices(new_room);
      this.comp_to_upgrade = context.comp_up;
      this.mic_to_upgrade = context.micro_up;
      this.cam_to_upgrade = context.webcam_up;

      this.comp_current = context.comp_cur;
      this.mic_current = context.micro_cur;
      this.cam_current = context.webcam_cur;

      this.comp_lvl = new_room.comp_lvl
      this.mic_lvl = new_room.micro_lvl
      this.cam_lvl = new_room.webcam_lvl

      this.room_id = new_room.id
    },
    async update_us(){
      const response = await this.$axios.get('/get_user/', {
          params: {
            user_id: this.datar.user.user_id,
            username: this.datar.user.username,
            usertag: this.datar.user.usertag,
          },
          withCredentials: true,
        });
        console.log(response.data)
        this.data = response.data;
        this.$store.commit('ADD_TO_ROOMS', this.data.rooms)
        this.update_lvls()
    },
    async upgrade(type,room_id,upgrade_cost) {
    try {
      const response = await this.$axios.post('/upgrade/', {'type':type,'room_id':room_id,'upgrade_cost':upgrade_cost});  /// comp,mic,webcam
      this.response = response.data;
      await this.update_us()
      this.$emit('update-bal', {type:type,room_id:room_id,upgrade_cost:upgrade_cost});
    } catch (error) {
      this.error = error;
      console.error('Error submitting data:', error);
    }
  }
  },
  mounted(){
  },
  computed:{
    rooms(){
      return this.$store.state.rooms;
    },
    datar(){
      return this.$store.state.data;
    },
    emptyRooms() {
      return 6 - this.rooms.length;
    }
  }
}
</script>

<style scoped>
.room-image-wrapper {
  position: relative;
  display: inline-block;
  width: 100%;
}

.room-image-wrapper img {
  display: block;
  width: 100%;
  filter: saturate(0);
}

.lock-icon {
  position: absolute;
  top: 40%;
  right: 43%;
  width: 40px;
  height: 40px;
}

.blocks{
  display: grid;
  grid-template-columns: repeat(2, 48%);
  grid-column-gap: 4%;
  grid-row-gap: 2%; 
  margin-bottom: 10px;
}
.up-block{
  backdrop-filter: blur(20px);
  border: 1px solid rgb(59, 59, 59);
  border-radius: 7.5px;
  text-align: start;
  padding: 10px;
}
.up-block img{
  width: 100%;
  height: 120px;
  object-fit: cover;
}
.upgrade-content{
  width: 100%;
  border-radius: 15px;
  backdrop-filter: blur(20px);
  border: 1px solid rgb(59, 59, 59);
  padding: 15px;
  margin: 15px;
}
.row{
  display: flex;
  align-items: center;
  gap: 10px;
}
.dialog{
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.637);
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 99;
  opacity: 1;
  transition: all .2s ease;
}

.dialog-hide{
  opacity: 0;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.737);
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 99;
  transition: all .2s ease;
}
.btn-upgrade{
  background-color: #EB95F9;
  color: white;
  border: none;
  border-radius: 7.5px;
  padding: 10px 20px;
  font-family: 'Montserrat';
  filter: drop-shadow(0 0 10px #df67f19a);
}

.btn-upgrade-disabled{
  background-color: #92609a;
  color: white;
  border: none;
  border-radius: 7.5px;
  padding: 10px 20px;
  font-family: 'Montserrat';
}

.rooms{
  height: 100%;
  overflow-y: scroll;
  padding: 15px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-bottom: 300px;
}
.room{
  padding: 10px;
  backdrop-filter: blur(20px);
  border: 1px solid rgb(59, 59, 59);
  /* filter: drop-shadow(0 0 10px #df67f142); */
  border-radius: 15px;
}

.room img{
  height: 200px;
  object-fit: cover;
  width: 100%;
  border-radius: 7.5px;
}

h1{
  color: white;
  font-size: 1rem;
}

.room-info{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>