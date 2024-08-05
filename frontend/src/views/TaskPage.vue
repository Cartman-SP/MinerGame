<template>
  <div class="taskpage">
    <!-- <div class="header">
        <h1 class="title">TASK</h1>
    </div> -->

    <div class="daily">
        <p class="naming">ЕЖЕДНЕВНЫЕ ЗАДАНИЯ</p>
        <div class="daily-tasks">
            <div class="task">
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-calendar-task.png" alt="">
                </div>
                <p class="name" style="font-size: 10px;">ЕЖЕДНЕВНАЯ НАГРАДА</p>
                <div class="logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="task" @click="shareLink">  
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-addfriend-task.png" alt="">
                </div>
                <p class="name">ПРИГЛАСИТЬ ДРУГА <br>+ 4 000</p>
                <div class="logo-background" style="background: #a0a0a0;">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="task" @click="redirectToTelegram">
                <div style="background: linear-gradient(180deg, rgba(25,25,25,1) 0%, rgba(57,54,52,1) 100%);" class="logo-background">
                    <img class="task-icon" src="../assets/icon-telegram-task.png" alt="">
                </div>
                <p class="name">ПОДПИСАТЬСЯ НА КАНАЛ<br>+ 4 000</p>
                <div class="logo-background" v-if="this.$user.data.subscribed">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
                <div class="logo-background" style="background: #a0a0a0;" v-else>
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
        </div>
        
    </div>
    <div class="other">
        <p class="naming" style="margin-top: 30px;">ЗАДАНИЯ</p>
        <div class="other-tasks">
            <div class="other-task">
                <p class="other-name">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 4 000</p>
                <div class="other-logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="other-task">
                <p class="other-name">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 4 000</p>
                <div class="other-logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="other-task">
                <p class="other-name">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 4 000</p>
                <div class="other-logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="other-task">
                <p class="other-name">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 4 000</p>
                <div class="other-logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="other-task">
                <p class="other-name">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 4 000</p>
                <div class="other-logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
            <div class="other-task">
                <p class="other-name">ПРИГЛАСИТЬ 3 ДРУЗЕЙ <br>+ 4 000</p>
                <div class="other-logo-background">
                    <img class="task-icon" src="../assets/icon-complete-task.png" alt="">
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    computed:{
        invite(){
            return 'https://t.me/M1nerGamebot/Miner?startapp='+this.$user.data.user_id
        } 
    },
 methods:{
    async check_subscribe(){
        try{
            console.log(this.$user.data.user_id)
            const response = this.$axios.get('/check_subscribe/', {params:{user_id: this.$user.data.user_id}})
            this.$user.data.balance = response.data.balance
            this.$user.data.subscribed = response.data.subscribed
            this.$user.data.subscribed_money_gived = response.data.subscribed_money_gived
        }catch(error){
            console.log(error)
        }
    },
    redirectToTelegram() {
        window.location.href = 'https://t.me/MinerGam3';
    },
    shareLink(){
        const url = this.invite;
        const text = '\nПривет! Хочу пригласить тебя поиграть в классную игру, где ты сможешь создать свою собственную майнинг ферму прямо на телефоне! Развивай свою империю, добывай криптовалюту и зарабатывай вместе со мной! \nА в качестве бонуса при запуске игры тебя ждет приятное вознаграждение 💸';
        window.location.href = `https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`;
    }
},

mounted(){
    this.check_subscribe()
}
}
</script>

<style scoped>
.other-tasks{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(3, 1fr);
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    padding: 0 10px;
    margin-bottom: 150px;
}
.taskpage{
    overflow-y: scroll;
    height: 70vh;
}
.naming{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
}
.daily-tasks{
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.task-icon{
    width: 25px;
}
.name{
    color: white;
    font-family: "Druk Wide";
    font-size: 8px;
    margin: 0;
}
.other-name{
    color: white;
    font-family: "Druk Wide";
    font-size: 6px;
    margin: 0;
}
.daily-tasks{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    
}
.task{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    display: flex;
    width: 90%;
    align-items: center;
    justify-content: space-between;
    padding: 5px;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.other-task{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    display: flex;
    width: 95%;
    align-items: center;
    justify-content: space-between;
    padding: 5px;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.logo-background{
  width: 40px;
  height: 35px;
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
.other-logo-background{
  width: 35px;
  height: 30px;
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