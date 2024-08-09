<template>
    <div class="upgrade">
        <!-- <div class="header">
            <h1 class="title">BOOST</h1>
        </div> -->
        <div class="content">
            <div class="block" @click="toggleModal(1)" v-if="enery_lvl<15">
                <img class="icon" src="../assets/icon-battery-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">ENERGY LIMIT<br> <span>{{upcost[enery_lvl]}}</span></p>
                    <div class="logo-background">
                        <span style="font-size: 26px;">{{enery_lvl}}</span>LVL
                    </div>
                </div>
            </div>
            <div class="block" v-else>
                <img class="icon" src="../assets/icon-battery-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">ENERGY LIMIT<br> <span>{{upcost[enery_lvl]}}</span></p>
                    <div class="logo-background">
                        <span style="font-size: 26px;">MAX_lvl</span>LVL
                    </div>
                </div>
            </div>
            <div class="block" @click="toggleModal(2)" v-if="tap_lvl<15">
                <img class="icon" src="../assets/icon-multitap-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">MULTITAP<br> <span>{{upcost[tap_lvl]}}</span></p>
                    <div class="logo-background">
                        <span style="font-size: 26px;">{{tap_lvl}}</span>LVL
                    </div>
                </div>
            </div>
            <div class="block" v-else>
                <img class="icon" src="../assets/icon-multitap-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">MULTITAP<br> <span>{{upcost[tap_lvl]}}</span></p>
                    <div class="logo-background">
                        <span style="font-size: 26px;">MAX LVL</span>LVL
                    </div>
                </div>
            </div>
            <div class="block" @click="give_energy">
                <img class="icon" src="../assets/icon-energy-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">FULL ENERGY<br> </p>
                    <div class="logo-background">
                        <span style="font-size: 18px;">{{ refresh_energy }}/5</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="overlay" ref="overlay" @click="toggleModal(1)" v-if="showModal"></div>
        <div class="modal" v-if="showModal" ref="modal">
            <img class="icon" src="../assets/icon-multitap-boost.png" alt="" v-if="upimg">
            <img class="icon" src="../assets/icon-battery-boost.png" alt="" v-else>

            <h3>{{ name }}</h3>
            <div class="info">
                <p class="level">{{ lvl }} LVL</p>
                <hr>
                <p class="boost">{{up}}</p>
            </div>

            <div class="buy" @click="upgrade">
                ПОЛУЧИТЬ ЗА
                <div class="cost">
                    {{ cost }}

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
            showModal: false,
            name: '',
            lvl: 0,
            up: '',
            cost: 0,
            num:1,
            upcost:[0,'1 400','3 500','7 500','10 600','30 600','100 000','220 000','550 000','900 000','1 300 000','1 600 000','2 000 000','2 500 000','3 500 000'],
            uptap: [0,2,2,4,4,6,6,7,7,8,8,10,10,15,15],        
            upimg: 0,
            alertMessage: '',
        }
    },

    computed: {
        enery_lvl(){
            return this.$user.data.enery_lvl
        },
        tap_lvl(){
            return this.$user.data.tap_lvl
        },
        refresh_energy(){
            return this.$user.data.refresh_energy
        }
    },
    methods:{
        async give_energy(){
            window.Telegram.WebApp.HapticFeedback.impactOccurred('light');

            if(this.$user.data.refresh_energy>0 && this.$user.data.energy<this.$user.data.max_energy){
                let data = {'user_id':this.$user.data.user_id}
            try {
                const response = await this.$axios.post('/set_max_energy/', data, {withCredentials: true});
                console.log(response)
                this.$user.data.energy = this.$user.data.max_energy;
                this.$user.data.refresh_energy -=1
            }catch (error) {
                this.error = error;
                console.error('Error fetching data:', error);
            }
            }
        },
        async upgrade(){
            window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
            let data = {'user_id':this.$user.data.user_id,'num':this.num}
            try {
                const response = await this.$axios.post('/upgrade/', data, {withCredentials: true});
                console.log(response.data);
                this.$user.data.balance = response.data.balance
                this.$user.data.enery_lvl = response.data.energy_lvl
                this.$user.data.gpc = response.data.gpc
                this.$user.data.max_energy = response.data.max_energy
                this.$user.data.tap_lvl = response.data.tap_lvl

                if(this.num==1){

                    this.lvl = response.data.energy_lvl+1
                    this.cost = this.upcost[response.data.energy_lvl]
                    if(this.lvl==16){
                            this.toggleModal(1)
                    }
                }else{
                    this.lvl = response.data.tap_lvl+1
                    this.cost = this.upcost[response.data.tap_lvl]
                    if(this.lvl==16){
                            this.toggleModal(2)
                    }        
                    this.up = '+'+ this.uptap[this.lvl-1] +' TAP'
                }
            }
            catch (error) {
                this.alertMessage = 'Недостаточно баланса'
                this.error = error;
                console.error('Error fetching data:', error);
            }
        },

        toggleModal(num){
            window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
            if(num==1){
                this.upimg = 0
                this.num = num
                this.name = 'ENERGY LIMIT'
                this.lvl = this.enery_lvl + 1
                this.up = '+250 ENERGY'
                this.cost = this.upcost[this.enery_lvl] > 1000 ? (this.upcost[this.enery_lvl] / 1000) + 'K' : this.upcost[this.enery_lvl]
            }else{
                this.upimg = 1
                this.num = num
                this.name = 'MULTITAP'
                this.lvl = this.tap_lvl + 1
                this.up = '+'+ this.uptap[this.lvl-1] +' TAP'
                this.cost = this.upcost[this.tap_lvl] > 1000 ? (this.upcost[this.tap_lvl] / 1000) + 'K' : this.upcost[this.tap_lvl]
 
            }
            if (this.showModal) {
                const modalwindow = this.$refs.modal;
                modalwindow.classList.remove('show');
                const modaloverlay = this.$refs.overlay;
                modaloverlay.classList.remove('showOverlay');

                setTimeout(() => {
                    this.showModal = false
                }, 400);
                

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
    }
    
}
</script>

<style scoped>
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
    height: 350px;
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
.cost{
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
.icon{
    width: 25px;
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
.content{
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.block{
    background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);
    height: 70px;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    display: flex;
    align-items: center;
    box-sizing: border-box;
}
.logo-background{
  width: 60px;
  height: 60px;
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
.price-locked{
    color: #FFFFFF;
    font-family: "Druk Wide";
    font-size: 16px;
    margin-bottom: 10px;
    text-align: left;
}
.price-locked span{
    font-size: 22px;
    
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