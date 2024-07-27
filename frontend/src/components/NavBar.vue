<template>
  <div class="nav">
    <div class="button">
        <div class="icon">
            <img src="../assets/icon-wallet.png" alt="">
        </div>
        <p class="title">WALLET</p>
    </div>
    <div class="button">
        <div class="icon">
            <img src="../assets/icon-top.png" alt="">
        </div>
        <p class="title">TOP</p>
    </div>
    <div class="mainButton">
        <div class="left"></div>
        <!-- <img src="../assets/icon-spinner.png" alt=""> -->
        <div class="right"></div>
    </div>
    <div class="button">
        <div class="icon">
            <img src="../assets/icon-friend.png" alt="">
        </div>
        <p class="title">FRIENDS</p>
    </div>
    <div class="button">
        <div class="icon">
            <img src="../assets/icon-task.png" alt="">
        </div>
        <p class="title">TASKS</p>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
:root {
    --color-gradient: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
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

.mainButton {
    width: 100%;
    height: 60px;
    display: flex;
}

.left {
    height: 60px;
    width: 50%;
    background: radial-gradient(circle at 100% 0, transparent 50%, black 10px);
    background-position: top right;
    background-size: 100% 100%;
    background-repeat: no-repeat;    
}

.right {
    height: 60px;
    width: 50%;
    
    background: radial-gradient(circle at 0 0, transparent 50%, black 10px);
    background-position: top left;
    background-size: 100% 100%;
    background-repeat: no-repeat;
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