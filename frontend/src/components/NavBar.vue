<template>
  <div class="nav">
    <div class="button" @click="moveto('/wallet')">
        <div class="icon-nav">
            <img src="../assets/icon-wallet.png" alt="">
        </div>
        <p class="title" v-if="language == 'ru'">КОШЕЛЕК</p>
        <p class="title" v-else>WALLET</p>
    </div>
    <div class="button" @click="moveto('/top')">
        <div class="icon-nav">
            <img src="../assets/icon-top.png" alt="">
        </div>
        <p class="title" v-if="language == 'ru'">ТОП</p>
        <p class="title" v-else>TOP</p>
    </div>
    <div class="mainButton" @click="spinImage">
        <div class="fan-btn">
            <img ref="spinner" style="width: 100%;" src="../assets/icon-spinner.png" alt="">
        </div>
       
    </div>
    <div class="button" @click="moveto('/friends')">
        <div class="icon-nav">
            <img  style="width: 25px;" src="../assets/icon-friend.png" alt="">
        </div>
        <p class="title" v-if="language == 'ru'">ДРУЗЬЯ</p>
        <p class="title" v-else>FRIENDS</p>
    </div>
    <div class="button"  @click="moveto('/task')">
        <div class="icon-nav">
            <img src="../assets/icon-task.png" alt="">
        </div>
        <p class="title" v-if="language == 'ru'">ЗАДАНИЯ</p>
        <p class="title" v-else>TASKS</p>
    </div>
  </div>
</template>

<script>
export default {
    methods: {
        spinImage() {
            const spinner = this.$refs.spinner;
            spinner.classList.add('spin');
            this.$router.push('/');

            this.$user.playTap()

            setTimeout(() => {
                spinner.classList.remove('spin');
            
            }, 500);
        },
        moveto(url){
            
            this.$user.playTap()

            if(url=='/top' || url=='/friends'){
                this.$user.data.toppage = true
            }
            this.$router.push(url);
        }
    },
     computed:{
        language(){
          return this.$user.data.lang;
        },
     }
}
</script>

<style>
.icon-nav{
    scale: 1.5;
}
:root {
    --color-gradient: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.spin {
    animation: spin .5s ease;
}

.nav {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 30px;
}

.button {
    background: var(--color-gradient);
    width: 100%;
    height: 15vh;
}
.fan-btn{
    background: var(--color-gradient);
    padding: 10px;
    height: 60px;
    width: 60px;
    /* filter: drop-shadow(0 5px 10px #00E6FF); */
    border-radius: 50%;
    border: solid 10px rgb(90, 90, 90);
    bottom: 20px;
    position: absolute;
    top: -4vh;
}


.mainButton {
    width: 100%;
    height: 19vh;
    display: flex;
    justify-content: center;
    background: var(--color-gradient);
    position: relative;
}


.button{
    display: flex;
    flex-direction: column;
    justify-content: start;
    padding-top: 2vh;
    gap: 5px;
    align-items: center;
}
.button img {
    width: 20px;
    height: 20px;
}

.title {
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    margin: 0;
    margin-top: 5px;
}
</style>