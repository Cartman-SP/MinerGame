<template>
    <div class="upgrade">
        <!-- <div class="header">
            <h1 class="title">UPGRADE</h1>
        </div> -->

        <div class="blocks">
            <div class="block" @click="upgrade">
                <div class="photo">
                    <img class="spinner" :src="staticPath" alt="">
                </div>
                <div class="cost">
                    <p class="price">{{costs[level]}}</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                </div>
                <div class="cost">
                    <p class="price-locked">ДОСТУПНО НА <br> <span>УРОВНЕ</span></p>
                    <div class="logo-background">
                        3
                    </div>
                </div>
            </div>

            <div class="block">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                </div>
                <div class="cost">
                    <p class="price-locked">ДОСТУПНО НА <br> <span>УРОВНЕ</span></p>
                    <div class="logo-background">
                        6
                    </div>
                </div>
            </div>

            <div class="block">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                </div>
                <div class="cost">
                    <p class="price-locked">ДОСТУПНО НА <br> <span>УРОВНЕ</span></p>
                    <div class="logo-background">
                        9
                    </div>
                </div>
            </div>

            
            
        </div>

        <div class="miningUpgrade" @click="toggleModal(1)">
            <img class="icon" src="../assets/icon-miningTime-boost.png" alt="">
            <div class="statement">
                <p class="price-locked-mining">MINING TIME<br> </p>
                <div class="logo-background">
                    <span style="font-size: 18px;">{{ refresh_energy }}/5</span>
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
                <div class="cost-modal">
                    {{ cost }}

                </div>
            </div>
        </div>
        <AlertMessage :message="alertMessage" :color="alertColor"/>
    </div>
  
</template>

<script>
import AlertMessage from "../components/AlertMessage.vue";
export default {
    components: { AlertMessage } ,
    data(){
        return{
            costs:[0,30000,115000,350000,1000000,2950000,8200000,23400000,58500000,175500000,350000000,'MAX LVL'],
            showModal: false,
            name: '',
            lvl: 0,
            up: '',
            cost: 0,
            num:1,
        }
    },
    methods:{
        async upgrade(){
            let data = {'user_id':this.$user.data.user_id}
            try {
                const response = await this.$axios.post('/upgrade_mining/', data, {withCredentials: true});
                console.log(response.data);
                this.$user.data.balance = response.data.balance
                this.$user.data.gph = response.data.gph
                this.$user.data.video_lvl = response.data.video_lvl
            }
            catch (error) {
                this.error = error;
                console.error('Error fetching data:', error);
            }
        },
        toggleModal(num){
            if(num===1){
                this.upimg = 0
                this.num = num
                this.name = 'MINING TIME'
                this.lvl = this.enery_lvl + 1
                this.up = '+250 ENERGY'
                this.cost = '100'
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
    },
    computed: {
        level(){
            return this.$user.data.video_lvl
        },
        staticPath() {
        return 1;
        }

    }
}
</script>

<style scoped>
.cost-modal{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    width: 100px;
    padding: 10px 0;
    margin-left: 20px;
    border-radius: 10px;
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
.upgrade{
    height: 60vh;
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
    width: 35px;
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
    justify-content: space-between;
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