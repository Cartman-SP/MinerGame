<template>
    <div class="wallet-page">
      <img src="../assets/logo-small-blue.png" alt="" style="width: 50px; margin-bottom: 40px;">
      <p class="unavailable" v-if="language == 'ru'">ВРЕМЕННО НЕДОСТУПНО</p>
      <p class="unavailable" v-else>TEMPORARILY UNAVAILABLE</p>
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
          <p class="name" style="font-size: 12px;" v-if="language == 'ru'">ПОДКЛЮЧИТЬ СВОЙ<br>КОШЕЛЕК</p>
          <p class="name" style="font-size: 12px;" v-else>CONNECT YOUR OWN<br>WALLET</p>
        </div>
      </div>
      <AlertMessage :message="alertMessage" style="z-index: 200;"/>
    </div>
  </template>
  
  <script >
  
  import AlertMessage from "../components/AlertMessage.vue";

  export default {
    components: { AlertMessage },
    data() {
      return {
        alertMessage: '',
      };
    },
    methods: {
        async open_pay(){
            try{
                const data = {'user_id':this.$user.data.user_id}
                const response = await this.$axios.get('/get_innovice_link/',data, {withCredentials: true})
                const link = response.data.result
                window.Telegram.WebApp.openInvoice(link, (status) => {
                    if (status === "paid") {
                        console.log('123')
                    }
                });
            }catch(error){
                console.log(error)
            }

            

        }
    }
  };
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