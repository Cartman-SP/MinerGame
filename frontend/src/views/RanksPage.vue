<template>
    <div class="rankPage">
      <div class="ranks">
        <div v-for="(i, index) in ranks.slice(1)" :key="i">
          <div v-if="lvl == index" class="rank-block" :style="'border: solid 1px #00c3ff'" ref="rank_now">
            <p class="position">{{ index + 1 }}</p>
            <div class="line-rank" v-if="lvl == index"></div>
            <p class="rank-name">{{ i }}</p>
            <div class="line-rank" v-if="lvl == index"></div>
            <div class="mark" v-if="lvl >= index" style="background-color: #00c3ff;"></div>
            <div class="mark" v-else></div>
          </div>
          <div v-else class="rank-block">
            <p class="position">{{ index + 1 }}</p>
            <div class="line-rank" v-if="lvl == index"></div>
            <p class="rank-name">{{ i }}</p>
            <div class="line-rank" v-if="lvl == index"></div>
            <div class="mark" v-if="lvl >= index" style="background-color: #00c3ff;"></div>
            <div class="mark" v-else></div>
          </div>
        </div>
      </div>
      <div style="height: 60px;"></div>
    </div>
</template>

<script>
export default {
data() {
    return {
    ranks: ['','IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','IMMORTAL','TRADER','SHARK','WHALE'],
    };
},
computed: {
    lvl() {
    return this.$user.data.lvl - 1;
    },
},
mounted() {
    this.$nextTick(() => {
    const block = this.$refs.rank_now;

    if (block) {
        let index = 0;
        const interval = setInterval(() => {
        if (index < block.length) {
            block[index].classList.add('rank_now');
            index++;
        } else {
            clearInterval(interval);
        }
        }, 50);
    }
    });

    setTimeout(() => {
        let block = this.$refs.rank_now;
        block[0].classList.remove('rank_now')
    }, 1500);
},
};
</script>

<style scoped>
.rankPage{
    height: 70vh;
    overflow-y: scroll;
}
.line-rank{
    background-color: #00c3ff;
    height: 4px;
    border-radius: 2px;
    width: 20%;
}
.ranks{
    padding: 15px 0 100px 0;
    display: flex;
    flex-direction: column-reverse;
    gap: 0;
    
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
    scale: 1;

    transition: scale .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
}
.rank_now{
    scale: 1.2;
    animation: shake 1.5s ease-in-out;
    transition: scale .5s cubic-bezier(0.560, 1.555, 0.305, 0.940);
}

@keyframes shake {
  0%, 100% {
    transform: translateX(0);
  }
  10%, 30%, 50%, 70%, 90% {
    transform: translateX(-10px);
  }
  20%, 40%, 60%, 80% {
    transform: translateX(10px);
  }
}
</style>