<template>
  <div class="nav">
    <div class="button" @click="this.$router.push('/wallet')">
        <div class="icon">
            <img src="../assets/icon-wallet.png" alt="">
        </div>
        <p class="title">WALLET</p>
    </div>
    <div class="button" @click="this.$router.push('/top')">
        <div class="icon">
            <img src="../assets/icon-top.png" alt="">
        </div>
        <p class="title">TOP</p>
    </div>
    <div class="mainButton" @click="spinImage">
        <img ref="spinner" class="fan-btn" src="../assets/icon-spinner.png" alt="">
    </div>
    <div class="button" @click="this.$router.push('/friends')">
        <div class="icon">
            <img src="../assets/icon-friend.png" alt="">
        </div>
        <p class="title">FRIENDS</p>
    </div>
    <div class="button"   @click="this.$router.push('/task')">
        <div class="icon">
            <img src="../assets/icon-task.png" alt="">
        </div>
        <p class="title">TASKS</p>
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
            setTimeout(() => {
                spinner.classList.remove('spin');
            
            }, 500);
        }
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
    height: 60px;
}

.button {
    background: var(--color-gradient);
    width: 100%;
    height: 60px;
}
.fan-btn{
    background: var(--color-gradient);
    padding: 10px;
    height: 50px;
    width: 50px;
    filter: drop-shadow(0 0px 5px rgb(23, 23, 23));
    border-radius: 50%;
    bottom: 20px;
    position: absolute;
    
}

.fan-btn img{}

.mainButton {
    width: 100%;
    height: 60px;
    display: flex;
    justify-content: center;
    background: var(--color-gradient);
    position: relative;
}


.button{
    display: flex;
    flex-direction: column;
    justify-content: center;
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