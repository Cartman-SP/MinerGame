<template>
  <div class="ranks">
    <div class="rank-block" v-for="(i, index) in ranks.slice(1)" :key="i" :style="lvl == index ? 'border: solid 1px #00c3ff' : ''">
        <p class="position">{{index+1}}</p>
        <div class="line-rank" v-if="lvl == index"></div>
        <p class="rank-name">{{ i }}</p>
        <div class="line-rank" v-if="lvl == index"></div>
        <div class="mark" v-if="lvl != index"></div>
        <div class="mark" v-else style="background-color: #00c3ff;"></div>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return{
            ranks: ['','IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','IMMORTAL','TRADER','SHARK','WHALE'],
        }
    },
    computed:{
        lvl(){
            return this.$user.data.lvl-1
        },
    }
}
</script>

<style scoped>
.line-rank{
    background-color: #00c3ff;
    height: 4px;
    border-radius: 2px;
    width: 20%;
}
.ranks{
    padding: 15px 0 100px 0;
    height: 60vh;
    display: flex;
    flex-direction: column-reverse;
    gap: 0;
    overflow-y: scroll;
}
.mark{
    height: 30px;
    width: 30px;
    background-color: rgb(120, 120, 120);
    border-radius: 10px;
}
.position{
    color: white;
    font-family: "Druk Wide";
    font-size: 20px;
    margin: 0;
}
.rank-name{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
    margin: 0;
}
.rank-block{
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    margin: 5px 50px;
    padding-left: 15px;
}
</style>