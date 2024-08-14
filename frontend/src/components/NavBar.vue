<template>
  <div class="nav">
    <div class="button" @click="moveto('/wallet')" ref="block_first">
        <div class="icon-nav">
            <img src="../assets/icon-wallet.png" alt="">
        </div>
        <p class="title" v-if="language == 'ru'">КОШЕЛЕК</p>
        <p class="title" v-else>WALLET</p>
    </div>
    <div class="button" @click="moveto('/top')" ref="block_second">
        <div class="icon-nav">
            <img src="../assets/icon-top.png" alt="">
        </div>
        <p class="title" v-if="language == 'ru'">ТОП</p>
        <p class="title" v-else>TOP</p>
    </div>
    <div class="mainButton" @click="spinImage">
        <div class="fan-btn" ref="block_mainBtn">
            <img ref="spinner" style="width: 100%;" src="../assets/icon-spinner.png" alt="">
        </div>
       
    </div>
    <div class="button" @click="moveto('/friends')" ref="block_third">
        <div class="icon-nav">
            <img  style=" width: 8vw; height: 7vw;" src="../assets/icon-friend.png" alt="">
        </div>
        <p class="title" v-if="language == 'ru'">ДРУЗЬЯ</p>
        <p class="title" v-else>FRIENDS</p>
    </div>
    <div class="button"  @click="moveto('/task')" ref="block_fourth">
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
    },
    mounted(){
        let index = 0;
        const blocks = [
        this.$refs.block_first,
        this.$refs.block_second,
        this.$refs.block_third,
        this.$refs.block_fourth,
        ];

        const interval = setInterval(() => {
            if (index < blocks.length) {
                const block = blocks[index];
                if (block) {
                    block.classList.add('nav-button-show');
                }
                index++;
            } else {
                clearInterval(interval);
            }
        }, 50);
        setTimeout(() => {
            this.$refs.block_mainBtn.classList.add('main-button-show')
        }, 200);
        
    }
    
}
</script>

<style>
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
    height: 10vh;
}

.button {
    background: var(--color-gradient);
    width: 100%;
    height: 10vh;
    transform: translateY(100px);
}
.nav-button-show{
    transform: translateY(0px);
    transition: transform .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
}
.fan-btn{
    background: var(--color-gradient);
    padding: 10px;
    width: 15vw;
    height: 15vw;
    /* filter: drop-shadow(0 5px 10px #00E6FF); */
    border-radius: 50%;
    border: solid 2vw rgb(90, 90, 90);
    bottom: 20px;
    position: absolute;
    top: -4vh;

    scale: 0;
    opacity: 0;
    rotate: 180deg;
    z-index: 10;
}
.main-button-show{
    scale: 1 !important;
    opacity: 1 !important;
    rotate: 0deg;
    transition: all .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
}



.mainButton {
    width: 100%;
    height: 10vh;
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
    width: 7vw;
    aspect-ratio: 1;
}

.title {
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    margin: 0;
    margin-top: 5px;
}
</style>