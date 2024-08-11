<template>
    <div class="upgrade">
        <!-- <div class="header">
            <h1 class="title">UPGRADE</h1>
        </div> -->

        <div class="blocks">
            <div class="block"  @click="toggleModal(2), modalType = 2">
                <div class="photo">
                    <img class="spinner" :src="staticPath(this.video_lvl)" alt="">
                    <p class="gpu_name">{{ names[video_lvl] }}</p>
                </div>
                <div class="cost">
                    <p class="price">{{costs[video_lvl]}}</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block" @click="open_pay(2)" v-if="!video2_lvl">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                    <p class="gpu_name">ЗАБЛОКИРОВАНО</p>
                </div>
                <div class="cost">
                    <p class="price">{{don_costs.video2 || 'null'}}</p>
                    <div class="logo-background" >
                        <img class="logoSmall" src="../assets/star_logo.png" alt="" style="height:20px;">
                    </div>
                </div>
            </div>
            <div class="block"  @click="toggleModal(3), modalType = 2" v-else>
                <div class="photo">
                    <img class="spinner" :src="staticPath(this.video2_lvl)" alt="">
                    <p class="gpu_name">{{ names[video2_lvl] }}</p>
                </div>
                <div class="cost">
                    <p class="price">{{costs[video2_lvl]}}</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block" @click="open_pay(3)" v-if="!video3_lvl">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                    <p class="gpu_name">ЗАБЛОКИРОВАНО</p>
                </div>
                <div class="cost">
                    <p class="price">{{don_costs.video3 || 'null'}}</p>
                    <div class="logo-background" >
                        <img class="logoSmall" src="../assets/star_logo.png" alt="" style="height:20px;">
                    </div>
                </div>
            </div>
            <div class="block"  @click="toggleModal(4), modalType = 2" v-else>
                <div class="photo">
                    <img class="spinner" :src="staticPath(this.video3_lvl)" alt="">
                    <p class="gpu_name">{{ names[video3_lvl] }}</p>
                </div>
                <div class="cost">
                    <p class="price">{{costs[video3_lvl]}}</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block" @click="open_pay(4)" v-if="!video4_lvl">
                <div class="photo">
                    <img class="spinner" src="../assets/spinner-icon-locked.png" alt="">
                    <p class="gpu_name">ЗАБЛОКИРОВАНО</p>
                </div>
                <div class="cost">
                    <p class="price">{{don_costs.video4 || 'null'}}</p>
                    <div class="logo-background" >
                        <img class="logoSmall" src="../assets/star_logo.png" alt="" style="height:20px;">
                    </div>
                </div>
            </div>
            <div class="block"  @click="toggleModal(5), modalType = 2" v-else>
                <div class="photo">
                    <img class="spinner" :src="staticPath(this.video4_lvl)" alt="">
                    <p class="gpu_name">{{ names[video4_lvl] }}</p>
                </div>
                <div class="cost">
                    <p class="price">{{costs[video4_lvl]}}</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
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
                <img style="width: 300px; margin-top: -150px; margin-bottom: -40px;" :src="staticPath(this.video_lvl+1)" alt="">
                <h3>{{ names[video_lvl] }}</h3>
                <div class="info">
                    <p class="level">{{ lvl }} LVL</p>
                    <hr>
                    <p class="boost">{{up}}</p>
                </div>

                <div class="buy" @click="upgrade">
                    УЛУЧШИТЬ ЗА
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
            costs:[0,30000,115000,350000,1000000,2950000,8200000,23400000,58500000,175500000,350000000,'MAX LVL'],
            names: ['SM 1020','SM 1050','SM 1090','SPG 1220','iX 1300','RTG 1500','SR 1750','BP 2000','SSG 2500','DFX 3300','GM 4090'], 
            showModal: false,
            name: '',
            lvl: 0,
            up: '',
            cost: 0,
            num:1,
            upcost: [0,'6 500','45 000','150 000','500 000','1$','1,25$','1,5$','1,75$','2$'],
            upgph: ['731','1 638','3 627','8 307','18 720','42 120','94 770','213 408','4 80 285','1 080 612','2 250 550'],
            alertMessage: '',
            modalType: 0,
        }
    },
    methods:{
        async open_pay(video) {
            window.Telegram.WebApp.HapticFeedback.notificationOccurred('error');
            try {
                const response = await this.$axios.get('/get_invoice_link/', { params: {num: video, withCredentials: true} });
                const link = response.data.result;
                
                window.Telegram.WebApp.openInvoice(link, async(status) => {
                    if (status === "paid") {
                        if (video === 2) {
                            this.$user.data.video2_lvl = 1;
                            this.toggleModal(3);
                        } else if (video === 3) {
                            this.$user.data.video3_lvl = 1;
                            this.toggleModal(4);
                        } else if (video === 4) {
                            this.$user.data.video4_lvl = 1;
                            this.toggleModal(5);
                        }
                    }
                });
            } catch (error) {
                console.error('Error during payment:', error);
            }
        },
        formatNumber(num) {
            return num >= 1_000_000 ? `${(num / 1_000_000).toFixed(1)}M` : 
                num >= 1_000 ? `${(num / 1_000).toFixed(1)}K` : 
                num.toString();
        },
        async upgrade(num){
            this.alertMessage = '';
            this.$user.playTap()
            let data = {'user_id':this.$user.data.user_id,'num':num}
            try {
                const response = await this.$axios.post('/upgrade_mining/', data, {withCredentials: true});
                console.log(response.data);
                this.$user.data.balance = response.data.balance
                this.$user.data.gph = response.data.gph

                this.toggleModal();
                this.modalType = 2
                this.$user.playBuy()
                if(this.num==2){
                    this.$user.data.video_lvl = response.data.video_lvl
                }else if(this.num==3){
                    this.$user.data.video2_lvl = response.data.video2_lvl
                }else if(this.num==4){
                    this.$user.data.video3_lvl = response.data.video3_lvl
                }else if(this.num==5){
                    this.$user.data.video4_lvl = response.data.video4_lvl
                }
            }
            catch (error) {
                this.$user.playError()
                this.alertMessage = 'Недостаточно баланса'
                this.error = error;
                console.error('Error fetching data:', error);
            }
        },

        async uptime() {
            this.alertMessage = '';
            this.$user.playTap()
            let data = {'user_id': this.$user.data.user_id};
            try {
                const response = await this.$axios.post('/uptime/', data, {withCredentials: true});
                console.log(response.data);
                this.$user.data.balance = response.data.balance;
                this.$user.data.mining_time_lvl = response.data.mining_time_lvl;
                this.lvl = this.mining_time_lvl
                this.cost = this.upcost[this.mining_time_lvl]
                this.$user.playBuy()
            } catch (error) {
                this.$user.playError()
                this.alertMessage = 'Недостаточно баланса';
                this.error = error;
            }
        },
        toggleModal(num){
            this.$user.playTap()
            if(num==1){
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
                this.$user.playTap()
                
                this.showModal = true
                setTimeout(() => {
                    const modalwindow = this.$refs.modal;
                    modalwindow.classList.add('show');
                    const modaloverlay = this.$refs.overlay;
                    modaloverlay.classList.add('showOverlay');
                }, 10);
            }
            }else if(num==2){
            this.name = 'MINING TIME'
            this.lvl = this.video_lvl
            this.up = 'ПРИБЫЛЬ: ' + this.upgph[this.video_lvl] + '/час'
            this.num=num
            if (this.video_lvl<11){
                this.cost = this.formatNumber(this.costs[this.video_lvl])
            }else{
                this.cost = this.costs[this.video_lvl]
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
                this.$user.playTap()
                
                this.showModal = true
                setTimeout(() => {
                    const modalwindow = this.$refs.modal;
                    modalwindow.classList.add('show');
                    const modaloverlay = this.$refs.overlay;
                    modaloverlay.classList.add('showOverlay');
                }, 10);
            }
            }




            else if(num==3){
            this.name = 'MINING TIME'
            this.lvl = this.video2_lvl
            this.num=num
            this.up = 'ПРИБЫЛЬ: ' + this.upgph[this.video2_lvl] + '/час'
            if (this.video2_lvl<11){
                this.cost = this.formatNumber(this.costs[this.video2_lvl])
            }else{
                this.cost = this.costs[this.video2_lvl]
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
                this.$user.playTap()
                
                this.showModal = true
                setTimeout(() => {
                    const modalwindow = this.$refs.modal;
                    modalwindow.classList.add('show');
                    const modaloverlay = this.$refs.overlay;
                    modaloverlay.classList.add('showOverlay');
                }, 10);
            }
            }




            else if(num==4){
            this.num=num
            this.name = 'MINING TIME'
            this.lvl = this.video3_lvl
            this.up = 'ПРИБЫЛЬ: ' + this.upgph[this.video3_lvl] + '/час'
            if (this.video3_lvl<11){
                this.cost = this.formatNumber(this.costs[this.video3_lvl])
            }else{
                this.cost = this.costs[this.video3_lvl]
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
                this.$user.playTap()
                
                this.showModal = true
                setTimeout(() => {
                    const modalwindow = this.$refs.modal;
                    modalwindow.classList.add('show');
                    const modaloverlay = this.$refs.overlay;
                    modaloverlay.classList.add('showOverlay');
                }, 10);
            }
            }



            else if(num==5){
            this.num=num
            this.name = 'MINING TIME'
            this.lvl = this.video4_lvl
            this.up = 'ПРИБЫЛЬ: ' + this.upgph[this.video4_lvl] + '/час'
            if (this.video4_lvl<11){
                this.cost = this.formatNumber(this.costs[this.video4_lvl])
            }else{
                this.cost = this.costs[this.video4_lvl]
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
                this.$user.playTap()
                
                this.showModal = true
                setTimeout(() => {
                    const modalwindow = this.$refs.modal;
                    modalwindow.classList.add('show');
                    const modaloverlay = this.$refs.overlay;
                    modaloverlay.classList.add('showOverlay');
                }, 10);
            }
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
        don_costs(){
            return this.$user.data.costs
        },

        gph(){
            return this.$user.data.gph;
        },
        
        level(){
            return this.$user.data.video_lvl
        },
        mining_time_lvl(){
            return this.$user.data.mining_time_lvl
        },
        video_lvl(){
            return this.$user.data.video_lvl
        },
        video2_lvl(){
            return this.$user.data.video2_lvl
        },
        video3_lvl(){
            return this.$user.data.video3_lvl
        },
        video4_lvl(){
            return this.$user.data.video4_lvl
        }
    }
}
</script>

<style scoped>
.gpu_name{
    margin: 0;
    margin-bottom: 10px;
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    background: rgba(57,54,53,1);
    padding: 5px 15px;
    border: 1px solid rgb(0, 166, 255);
    width: fit-content;
    border-radius: 10px;
}
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
    width: 340px;
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
    width: 340px;
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
    padding-bottom: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
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
    width: 120px;
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