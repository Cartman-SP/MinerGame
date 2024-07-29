<template>
    <div class="upgrade">
        <div class="header">
            <h1 class="title">BOOST</h1>
        </div>
        <div class="content">
            <div class="block" @click="toggleModal">
                <img class="icon" src="../assets/icon-battery-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">ENERGY LIMIT<br> <span>30 000</span></p>
                    <div class="logo-background">
                        <span style="font-size: 26px;">7</span>LVL
                    </div>
                </div>
            </div>
            <div class="block" @click="toggleModal">
                <img class="icon" src="../assets/icon-multitap-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">MULTITAP<br> <span>30 000</span></p>
                    <div class="logo-background">
                        <span style="font-size: 26px;">7</span>LVL
                    </div>
                </div>
            </div>
            <div class="block" @click="toggleModal">
                <img class="icon" src="../assets/icon-energy-boost.png" alt="">
                <div class="statement">
                    <p class="price-locked">FULL ENERGY<br> <span>30 000</span></p>
                    <div class="logo-background">
                        <span style="font-size: 18px;">7/7</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="overlay" ref="overlay" @click="toggleModal" v-if="showModal"></div>
        <div class="modal" v-if="showModal" ref="modal">
            <img class="icon" src="../assets/icon-multitap-boost.png" alt="">
            <h3>MULTITAP</h3>
            <div class="info">
                <p class="level">4 LVL</p>
                <hr>
                <p class="boost">+1 TAP</p>
            </div>

            <div class="buy">
                ПОЛУЧИТЬ ЗА
                <div class="cost">
                    75K
                </div>
            </div>
        </div>
    </div>
  
</template>

<script>
export default {
    data(){
        return{
            showModal: false,
        }
    },
    methods:{
        toggleModal(){
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