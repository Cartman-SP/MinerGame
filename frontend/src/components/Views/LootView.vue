<template>
  <div>
    <div class="fortune-wheel">
    <canvas ref="wheelCanvas" width="250" height="250"></canvas>

    <div class="bets-container">
      <div class="bet">
        <h3>1</h3>
        <input type="number" v-model="bet_one" :disabled="spinning" :class="{'input_disabled' : spinning, 'input' : !spinning}">
      </div>
      <div class="bet">
        <h3>3</h3>
        <input type="number" v-model="bet_three" :disabled="spinning" :class="{'input_disabled' : spinning, 'input' : !spinning}">
      </div>
      <div class="bet">
        <h3>5</h3>
        <input type="number" v-model="bet_five" :disabled="spinning" :class="{'input_disabled' : spinning, 'input' : !spinning}">
      </div>
      <div class="bet">
        <h3>10</h3>
        <input type="number" v-model="bet_ten" :disabled="spinning" :class="{'input_disabled' : spinning, 'input' : !spinning}">
      </div>
      <div class="bet">
        <h3>20</h3>
        <input type="number" v-model="bet_twenty" :disabled="spinning" :class="{'input_disabled' : spinning, 'input' : !spinning}">
      </div>
      
    </div>
    <div class="summary-row">
      <h3>Summary: {{ bet_one + bet_three + bet_five + bet_ten + bet_twenty }}</h3>
      <button @click="spinWheel(),deegrade()" :disabled="spinning || !error" class="spin-btn" :class="{'spin-btn-disabled' : (spinning || !error)}">Spin</button>
    </div>
    <p style="margin-top: -20px; text-align: left; margin-left: 15px;">(min: {{ minMaxBets[userLvl].min }}, max: {{ minMaxBets[userLvl].max }})</p>
  </div>
  <div v-show="winner" :class="{'dialog' : winner, 'dialog-hide' : !winner}">
      <div class="container-dialog">
        <h3>You won:</h3>
        <h4>{{countWin(winner)}}</h4>
        <button class="collect" @click="toggleDialog">Okay</button>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, onMounted} from 'vue';

export default {
  data(){
    return{
      bet_one: 0,
      bet_three :0,
      bet_five: 0,
      bet_ten: 0,
      bet_twenty: 0,

      dialogClass: false,

      minMaxBets:{
        1: {min: 100, max: 1500},
        2: {min: 350, max: 5000},
        3: {min: 1500, max: 25000},
        4: {min: 3500, max: 50000},
        5: {min: 5000, max: 100000},
      },
      error: false,
    }
  },
  watch: {
    sum(newSum) {
      this.betsRequirements(newSum);
    }
  },
  methods:{
    deegrade(){
      let bet = (parseInt(this.bet_one) + parseInt(this.bet_three) + parseInt(this.bet_five) + parseInt(this.bet_ten) + parseInt(this.bet_twenty)) * -1
      console.log('1233333333333',bet)
      this.$emit('update-value', bet);
      this.$websocket.send(JSON.stringify({user_id: this.$store.state.data.user.user_id, increment: bet,type:'offline'}));
    },
    betsRequirements(newSum){
      if (newSum == 0) {
        this.error = false;
      }
      if((this.minMaxBets[this.userLvl].min <= newSum) && (this.minMaxBets[this.userLvl].max >= newSum)){
        this.error = true;
      }
    },

    toggleDialog(){
      if (this.winner) {
        let bets = {
        1: this.bet_one,
        3: this.bet_three,
        5: this.bet_five,
        10: this.bet_ten,
        20: this.bet_twenty,
      };
        let win = bets[this.winner]*(parseInt(this.winner)+1)
        console.log(win)

        this.$emit('update-value', win);
        this.$websocket.send(JSON.stringify({user_id: this.$store.state.data.user.user_id, increment: win}));

        this.winner = 0;
        
      }else{
        this.winner = 1;
      }
    },

    countWin(winner_bet){
      let bets = {
        1: this.bet_one,
        3: this.bet_three,
        5: this.bet_five,
        10: this.bet_ten,
        20: this.bet_twenty,
      };
      return bets[winner_bet]*(parseInt(winner_bet)+1)
    }
  },
  name: 'FortuneWheel',
  setup() {
    const wheelCanvas = ref(null);
    const segments = ['1', '3', '1', '10', '1', '3', '1', '5', '1', '5', '3', '1', '10', '1', '3', '1', '5', '1', '3', '1', '20', '1', '3', '1', '5', '1'];
    const spinning = ref(false);
    const winner = ref(null);
    let angle = 0;
    let spinAngle = 0;

    const colors = {
      '1': '#1F262D',
      '3': '#36414D',
      '5': '#81869C',
      '10': '#6D2B88',
      '20': '#EB95F9',
    };

    onMounted(() => {
      drawWheel();
      drawArrow();
    });

    const drawWheel = () => {
      const canvas = wheelCanvas.value;
      const ctx = canvas.getContext('2d');
      const radius = canvas.width / 2;
      const arcSize = (2 * Math.PI) / segments.length;

      ctx.clearRect(0, 0, canvas.width, canvas.height);

      segments.forEach((segment, index) => {
        const startAngle = index * arcSize;
        const endAngle = startAngle + arcSize;

        ctx.beginPath();
        ctx.arc(radius, radius, radius, startAngle, endAngle);
        ctx.lineTo(radius, radius);
        ctx.fillStyle = colors[segment]; // Use color mapping
        ctx.fill();

        ctx.save();
        ctx.translate(radius, radius);
        ctx.rotate((startAngle + endAngle) / 2);
        ctx.textAlign = 'right';
        ctx.fillStyle = 'white';
        ctx.font = '16px Montserrat';
        ctx.fillText(segment, radius - 10, 10);
        ctx.restore();
      });
    };

      const drawArrow = () => {
      const canvas = wheelCanvas.value;
      const ctx = canvas.getContext('2d');
      const radius = canvas.width / 2;

      ctx.fillStyle = '#F82E2E'; // Color for the arrow
      ctx.beginPath();
      ctx.moveTo(canvas.width, radius - 10); // Move to the right center of the wheel
      ctx.lineTo(canvas.width, radius + 10); // Line to the bottom
      ctx.lineTo(canvas.width - 25, radius); // Line to the left
      ctx.closePath(); // Close the path
      ctx.fill(); // Fill the arrow
    };




    const spinWheel = () => {
      if (spinning.value) return;
      spinning.value = true;
      winner.value = null;
      spinAngle = Math.random() * 2000 + 3000;
      const duration = 2000; // 5 seconds
      const startTime = performance.now();

      const animate = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easing = easeOutCubic(progress);
        angle = (easing * spinAngle) % 360;

        const canvas = wheelCanvas.value;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);
        ctx.rotate((angle * Math.PI) / 180);
        ctx.translate(-canvas.width / 2, -canvas.height / 2);
        drawWheel();
        ctx.restore();
        drawArrow(); // Redraw the arrow on top

        if (progress < 1) {
          requestAnimationFrame(animate);
        } else {
          spinning.value = false;
          winner.value = getWinningSegment();
        }
      };

      requestAnimationFrame(animate);
    };

    const easeOutCubic = (t) => (--t) * t * t + 1;

    const getWinningSegment = () => {
      const arcSize = 360 / segments.length;
      const winningIndex = Math.floor((360 - (angle % 360)) / arcSize) % segments.length;
      return segments[winningIndex];
    };

    return {
      wheelCanvas,
      spinWheel,
      spinning,
      winner
    };
  },
  computed:{
    userLvl(){
      return this.$store.state.data.user.lvl
    },
    sum() {
      return (
        this.bet_one +
        this.bet_three +
        this.bet_five +
        this.bet_ten +
        this.bet_twenty
      );
    },
  }
};

</script>

<style scoped>
.container-dialog{
  backdrop-filter: blur(20px);
  border: 1px solid rgb(59, 59, 59);
  border-radius: 15px;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 250px;
  margin: 15px;
  padding: 15px;
}
.dialog{
  background-color: rgba(0, 0, 0, 0.737);
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 99;
  opacity: 1;
  transition: all .3s ease;
}

.dialog-hide{
  background-color: rgba(0, 0, 0, 0.737);
  opacity: 0;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: end;
  z-index: 99;
  transition: all .3s ease;
}
.input_disabled{
  width: 50px;
  backdrop-filter: blur(10px);
  background-color: transparent;
  border: 1px solid rgb(59, 59, 59);
  border-radius: 20px;
  color: rgb(133, 130, 130);
  font-family: 'Montserrat';
  text-align: center;
  height: 50px;
}
.summary-row{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  padding-top: 0;
}
.bets-container{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
}

.input{
  width: 50px;
  backdrop-filter: blur(10px);
  background-color: transparent;
  border: 1px solid rgb(59, 59, 59);
  border-radius: 20px;
  color: white;
  font-family: 'Montserrat';
  text-align: center;
  height: 50px;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
}

input,
input:hover,
input:focus {
    appearance: none;
    -moz-appearance: textfield;
}
.fortune-wheel {
  text-align: center;
  margin-top: 20px;
  position: relative;
}

canvas {
  border: 5px solid #404557;
  filter: drop-shadow(0 0 10px #df67f142);
  border-radius: 50%;
}

button {
  margin-top: 20px;
}

.winner {
  margin-top: 20px;
  font-size: 1.5em;
  color: rgb(255, 255, 255);
}

.spin-btn{
  margin: 0;
  background-color: #EB95F9;
  color: white;
  border: none;
  border-radius: 7.5px;
  padding: 10px 20px;
  font-family: 'Montserrat';
  filter: drop-shadow(0 0 10px #df67f19a);
  font-size: .8rem;
}

.spin-btn-disabled{
  margin: 0;
  background-color: #92609a;
  color: rgb(205, 205, 205);
  border: none;
  border-radius: 7.5px;
  padding: 10px 20px;
  filter: none;
  font-family: 'Montserrat';
  font-size: .8rem;
}


</style>
