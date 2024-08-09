<template>
    <div class="upgrade">
        <!-- <div class="header">
            <h1 class="title">UPGRADE</h1>
        </div> -->

        <div class="blocks">
            <div class="block"  @click="toggleModal(2), modalType = 2">
                <div class="photo">
                    <img class="spinner" :src="staticPath(1)" alt="">
                </div>
                <div class="cost">
                    <p class="price">{{costs[level]}}</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block" @click="window.Telegram.WebApp.HapticFeedback.notificationOccurred('error');">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                </div>
                <div class="cost">
                    <p class="price">2.5</p>
                    <div class="logo-background">
                        $
                    </div>
                </div>
            </div>

            <div class="block" @click="window.Telegram.WebApp.HapticFeedback.notificationOccurred('error');">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                </div>
                <div class="cost">
                    <p class="price">2.5</p>
                    <div class="logo-background">
                        $
                    </div>
                </div>
            </div>

            <div class="block" @click="window.Telegram.WebApp.HapticFeedback.notificationOccurred('error');">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                </div>
                <div class="cost">
                    <p class="price">2.5</p>
                    <div class="logo-background">
                        $
                    </div>
                </div>
            </div>

            
            
        </div>

        <div class="miningUpgrade" @click="toggleModal(1), modalType = 1">
            <img class="icon" src="../assets/icon-miningTime-boost.png" alt="">
            <div class="statement">
                <p class="price-locked-mining">MINING TIME<br> </p>
                <div class="logo-background" style="width: 60px; height: 60px;">
                    <span style="font-size: 18px;">{{ mining_time_lvl }} <br> <span style="font-size: 18px;">lvl</span></span>
                </div>
            </div>
        </div>
        

        <div class="overlay" ref="overlay" @click="toggleModal()" v-if="showModal"></div>
        <div class="modal" v-if="showModal" ref="modal">
            <div v-if="modalType == 1">
                <img style="width: 120px;" class="icon" src="../assets/icon-miningTime-boost.png" alt="">

                <h3>{{ name }}</h3>
                <div class="info">
                    <p class="level">{{ lvl }} LVL</p>
                    <hr>
                    <p class="boost">{{up}}</p>
                </div>

                <div class="buy" @click="uptime">
                    ПОЛУЧИТЬ ЗА
                    <div class="cost-modal">
                        {{ cost }}

                    </div>
                </div>
            </div>
            <div v-if="modalType == 2" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <img style="width: 300px; margin-top: -150px; margin-bottom: -40px;" :src="staticPath(1)" alt="">
                <h3>НАЗВАНИЕ ВИДЕОКАРТЫ</h3>
                <div class="info">
                    <p class="level">{{ lvl }} LVL</p>
                    <hr>
                    <p class="boost">{{up}}</p>
                </div>

                <div class="buy" @click="upgrade">
                    ПОЛУЧИТЬ ЗА
                    <div class="cost-modal">
                        {{ cost }}

                    </div>
                </div>
            </div>
        </div>
        <AlertMessage :message="alertMessage" style="z-index: 200;"/>
    </div>
  
</template>

<script>
import AlertMessage from "../components/AlertMessage.vue";
export default {
    components: { AlertMessage } ,
    data(){
        return{
            costs:[0,'30 000','115 000','350 000','1 000 000','2 950 000,','8 200 000','23 400 000','58 500 000','175 500 000','350 000 000','MAX LVL'],
            showModal: false,
            name: '',
            lvl: 0,
            up: '',
            cost: 0,
            num:1,
            upcost: [0,'6 500','45 000','150 000','500 000','1$','1,25$','1,5$','1,75$','2$'],
            alertMessage: '',
            modalType: 0,
        }
    },
    methods:{
        async upgrade(){
            this.alertMessage = '';
            window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
            let data = {'user_id':this.$user.data.user_id}
            try {
                const response = await this.$axios.post('/upgrade_mining/', data, {withCredentials: true});
                console.log(response.data);
                this.$user.data.balance = response.data.balance
                this.$user.data.gph = response.data.gph
                this.$user.data.video_lvl = response.data.video_lvl
                this.toggleModal();
                this.modalType = 2
                var audio = new Audio(require('../assets/buy.mp3'));
                audio.volume = 1
                audio.play()
            }
            catch (error) {
                window.Telegram.WebApp.HapticFeedback.notificationOccurred('error');
                this.alertMessage = 'Недостаточно баланса'
                this.error = error;
                console.error('Error fetching data:', error);
            }
        },

        async uptime() {
            this.alertMessage = '';
            window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
            let data = {'user_id': this.$user.data.user_id};
            try {
                const response = await this.$axios.post('/uptime/', data, {withCredentials: true});
                console.log(response.data);
                this.$user.data.balance = response.data.balance;
                this.$user.data.mining_time_lvl = response.data.mining_time_lvl;
                this.lvl = this.mining_time_lvl
                this.cost = this.upcost[this.mining_time_lvl]
                var audio = new Audio(require('../assets/buy.mp3'));
                audio.volume = 1
                audio.play()
            } catch (error) {
                this.alertMessage = 'Недостаточно баланса';
                this.error = error;
            }
        },
        toggleModal(){
            
            window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
            this.name = 'MINING TIME'
            this.lvl = this.mining_time_lvl + 1
            this.up = '+30 MINUTES'
            this.cost = this.upcost[this.mining_time_lvl]
            if (this.showModal) {
                const modalwindow = this.$refs.modal;
                modalwindow.classList.remove('show');
                const modaloverlay = this.$refs.overlay;
                modaloverlay.classList.remove('showOverlay');

                setTimeout(() => {
                    this.showModal = false
                }, 400);
                

            } else {
                var audio = new Audio(require('../assets/tap.mp3'));
                audio.volume = 1
                audio.play()
                
                this.showModal = true
                setTimeout(() => {
                    const modalwindow = this.$refs.modal;
                    modalwindow.classList.add('show');
                    const modaloverlay = this.$refs.overlay;
                    modaloverlay.classList.add('showOverlay');
                }, 10);
            }
        },
        staticPath(lvl) {
            switch (lvl) {
                case 1:
                return require(`../assets/gpu1-static.png`);
                case 2:
                return require(`../assets/gpu1-static.png`);
                case 3:
                return require(`../assets/gpu1-static.png`);
                case 4:
                return require(`../assets/gpu4-static.png`);
                case 5:
                return require(`../assets/gpu5-static.png`);
                case 6:
                return require(`../assets/gpu6-static.png`);
                case 7:
                return require(`../assets/gpu7-static.png`);
                case 8:
                return require(`../assets/gpu8-static.png`);
                case 9:
                return require(`../assets/gpu9-static.png`);
                case 10:
                return require(`../assets/gpu10-static.png`);
                case 11:
                return require(`../assets/gpu11-static.png`);
            }
            return 1
        }
    },
    computed: {
        gph(){
            return this.$user.data.gph;
        },
        
        level(){
            return this.$user.data.video_lvl
        },
        mining_time_lvl(){
            return this.$user.data.mining_time_lvl
        },

    }
}
</script>

<style scoped>
.earningPerHour{
    background: rgba(57,54,53,1);
    padding: 5px 15px;
    border: 1px solid rgb(0, 166, 255);
    width: fit-content;
    border-radius: 10px;
    color: white;
    font-family: "Druk Wide";
    font-size: 20px;
    margin-top: -15px;
}
.cost-modal{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    width: 100px;
    padding: 10px 0;
    margin-left: 20px;
    border-radius: 10px;
}
.info{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    width: 300px;
    border-radius: 10px;
    filter: drop-shadow(0 0px 5px rgb(23, 23, 23));
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
    height: fit-content;
    padding-bottom: 130px;
    bottom: -500px;
    z-index: 10;
    transition: all .4s ease;
}
.show{
    bottom: 0;
    transition: all .4s ease;
}
.showOverlay{
    opacity: 1 !important;
    transition: all .4s ease;
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
    margin: 25px 0;
}
.level{
    color: white;
    font-family: "Druk Wide";
    font-size: 14px;
    margin: 5px 0;
}
.boost{
    color: white;
    font-family: "Druk Wide";
    font-size: 16px;
    margin: 5px 0;
}
hr{
    margin: 0 20px;
    color: #00C5FF;
}
.buy{
    font-family: "Druk Wide";
    color: white;
    font-size: 14px;
    margin-top: 10px;
    background: linear-gradient(180deg, rgb(0, 166, 255) 0%, rgba(0,230,255,1) 100%);
    width: 300px;
    border-radius: 10px;
    filter: drop-shadow(0 0px 5px rgb(23, 23, 23));
    display: flex;
    align-items: center;
    justify-content: center;
    padding:  5px 0;
}
.upgrade{
    height: 70vh;
    overflow: scroll;
}
.price-locked-mining{
    color: #FFFFFF;
    font-family: "Druk Wide";
    font-size: 16px;
    margin-bottom: 10px;
    text-align: left;
}
.price-locked span{
    font-size: 22px;
    
}
.miningUpgrade{
    background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);
    height: 70px;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    display: flex;
    align-items: center;
    box-sizing: border-box;
    margin: 0 30px;
    margin-top: 20px;
    margin-bottom: 100px;
}
.logo-background{
  width: 60px;
  height: 60px;
  background: linear-gradient(180deg, rgb(0, 166, 255) 0%, #00e6ff 100%);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  font-family: "Druk Wide";
  font-size: 14px;
}
.icon{
    width: 55px;
    margin: 0 15px;
}
.statement{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    width: 100%;
    height: 70px;
    border-radius: 10px;
    filter: drop-shadow(0 0px 5px rgb(23, 23, 23));
    display: flex;
    align-items: center;
    padding: 0 10px 0 40px;
    justify-content: space-between;
}
.price-locked{
    color: #C9C9C9;
    font-family: "Druk Wide";
    font-size: 8px;
    margin-bottom: 2px;
}
.price-locked span{
    font-size: 14px;
    
}
.price{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
    margin: 0;
    width: 70%;
}
.blocks{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 30px;
    grid-row-gap: 30px;
    padding: 0 30px;
}
.photo {
    background-color: #535453;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}

.cost {
    background-color: #535453;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    padding: 5px;
    display: flex;
    justify-content: center;
    margin-top: 5px;
    align-items: center;
    height: 30px;
}
.photo img{
    width: 90px;
    margin: 5px;
}
.logo-background{
  width: 30px;
  height: 30px;
  background: linear-gradient(180deg, rgb(0, 166, 255) 0%, rgba(0,230,255,1) 100%);
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-family: "Druk Wide";
  font-size: 14px;
}
.logoSmall{
  width: 20px;
  height: 13px;
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