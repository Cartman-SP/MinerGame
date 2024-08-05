<template>
    <div class="wallet-page">
        <!-- <div class="header">
            <h1 class="title">WALLET</h1>
        </div> -->
        <img src="../assets/logo-small-blue.png" alt="" style="width: 50px; margin-bottom: 40px;">
        <p class="unavailable">ВРЕМЕННО НЕДОСТУПНО</p>
        <div style="position: relative;">
            <img src="../assets/icon-lock.png" alt="" class="lock-icon">
            <div class="exchange">
                <img src="../assets/icon-exchange.png" alt="" class="exchange-icon">
                <p class="name">EXCHANGE</p>
            </div>
        </div>
        <div style="position: relative;">
            <img src="../assets/icon-lock.png" alt="" class="lock-icon">
            <div class="wallet">
                <img src="../assets/icon-wallet-white.png" alt="" class="wallet-icon">
                <p class="name" style="font-size: 12px;">ПОДКЛЮЧИТЬ СВОЙ<br>КОШЕЛЕК</p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
.lock-icon{
    position: absolute;
    top: 25%;
    left: 46.5%;
    width: 30px;
    height: 30px;
    z-index: 2;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.name{
    color: white;
    font-family: "Druk Wide";
    font-size: 16px;
    margin: 0;
    width: 100%;
}
.wallet-icon{
    width: 56px;
    height: 56px;
}
.exchange-icon{
    width: 56px;
    height: 56px;
    background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
    border-radius: 10px;
}
.exchange{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
}
.wallet{
    background: linear-gradient(0deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
}
.exchange, .wallet{
    display: flex;
    align-items: center;
    justify-content: start;
    padding: 0 5px;
    margin: 20px 40px;
    height: 70px;
    border-radius: 15px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    filter: brightness(50%);
}
.unavailable{
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    margin: 0;
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