<template>
    <div class="statusBar">
        <div class="profile"  @click="this.$router.push('/profile')">
            <img class="avatar" src="https://pixelbox.ru/wp-content/uploads/2022/08/avatar-boy-telegram-pixelbox.ru-76.jpg" alt="Avatar">
            <p class="name">{{username}}</p>
        </div>
        <div style="width: 120px;">
            <img class="logo" src="../assets/logo.png" alt="logo">
        </div>
        
        <div class="level">
            <p class="levelName">WHALE</p>
            <p>20%</p>
            <p class="goals">{{ lvl }}/10</p>
        </div>
    </div>
  </template>
  
  <script>
  export default {
    computed:{
      username(){
        return this.$user.data.username
      },
      lvl(){
        return this.$user.data.lvl
      },
    }
  }
  </script>
  
  <style scoped>
  
  .logo{
    width: 100%;
    scale: .8;
  }
  .statusBar{
    display: flex;
    justify-content: space-between;
    background: #383637;
    padding: 2px 10px;
    height: 60px;
  }
  .avatar{
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid #00E6FF;
  }

  .profile{
    width: 120px;
    height: 50px;
    border-radius: 15px;
    padding: 5px;
    color: white;
    font-family: "Druk Wide";
    font-size: 10px;
    display: flex;
    gap: 5px;
    align-items: center;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  }

  .level{
    height: 50px;
    width: 120px;
    border-radius: 15px;
    padding: 5px;
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    align-items: center;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  }
  </style>