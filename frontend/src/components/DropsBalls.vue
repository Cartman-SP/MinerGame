<template>
  <div class="clicker-view">
    <button @click="startGame">Start Game</button>
    <div class="game-area" @click="handleClick">
      <div
        v-for="(ball, index) in balls"
        :key="index"
        :style="ball.style"
        class="falling-ball"
        @click.stop="popBall(index)"
      >
        +{{ ball.boost }}
      </div>
    </div>
    <div class="boosts">
      <p>Total Boost: {{ totalBoost }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      balls: [],
      totalBoost: 0,
      gameInterval: null,
      ballFallInterval: null
    };
  },
  methods: {
    startGame() {
      this.totalBoost = 0;
      this.balls = [];
      if (this.gameInterval) {
        clearInterval(this.gameInterval);
      }
      if (this.ballFallInterval) {
        clearInterval(this.ballFallInterval);
      }
      this.gameInterval = setInterval(this.addBall, 500);
      this.ballFallInterval = setInterval(this.updateBalls, 30);
    },
    addBall() {
      const ballSize = 35;
      const gameArea = this.$el.querySelector('.game-area');
      const gameAreaWidth = gameArea.clientWidth;
      const x = Math.random() * (gameAreaWidth - ballSize);
      const boost = Math.floor(Math.random() * 10) + 1;

      const ball = {
        boost,
        y: 0,
        style: {
          position: 'absolute',
          top: '0px',
          left: `${x}px`,
          width: `${ballSize}px`,
          height: `${ballSize}px`,
          backgroundColor: '#EB95F9',
          borderRadius: '50%',
          textAlign: 'center',
          lineHeight: `${ballSize}px`,
          color: 'white'
        }
      };
      this.balls.push(ball);
    },
    updateBalls() {
      const gameArea = this.$el.querySelector('.game-area');
      const gameAreaHeight = gameArea.clientHeight;
      this.balls = this.balls.filter(ball => {
        ball.y += 5; // Adjust the speed of falling here
        ball.style.top = `${ball.y}px`;
        return ball.y < gameAreaHeight;
      });
    },
    popBall(index) {
      this.totalBoost += this.balls[index].boost;
      this.balls.splice(index, 1);
    }
  },
  beforeUnmount() {
    if (this.gameInterval) {
      clearInterval(this.gameInterval);
    }
    if (this.ballFallInterval) {
      clearInterval(this.ballFallInterval);
    }
  }
};
</script>

<style scoped>
.clicker-view {
  position: relative;
}

.game-area {
  position: absolute;
  width: 100%;
  height: 500px;
  border: none;
  background-color: transparent;
  overflow: hidden;
}

.boosts {
  margin-top: 20px;
}
</style>
