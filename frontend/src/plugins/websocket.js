// plugins/websocket.js
export default {
    install(app) {
      const websocketPlugin = {
        socket: null,
        miningSocket: null,
        energySocket: null,
        miningTimer: null,
        remainingTime: 0,
  
        initialize(userId) {
          this.initializeWebSocketConnections(userId);
          setInterval(() => {
            this.updateRemainingTime();
          }, 1000);
        },
  
        initializeWebSocketConnections(userId) {
          this.socket = new WebSocket(`ws://localhost:8001/ws/some_path/${userId}/`);
          this.socket.onmessage = this.onMessage;
          this.socket.onopen = () => {
            console.log('WebSocket connection established');
          };
          this.socket.onclose = () => {
            console.log('WebSocket connection closed');
          };
          this.socket.onerror = (error) => {
            console.error('WebSocket error:', error);
          };
  
          this.miningSocket = new WebSocket(`ws://localhost:8001/ws/mining/${userId}/`);
          this.miningSocket.onmessage = this.onMiningMessage;
          this.miningSocket.onopen = () => {
            console.log('Mining WebSocket connection established');
            this.startMiningTimer();
          };
          this.miningSocket.onclose = () => {
            console.log('Mining WebSocket connection closed');
          };
          this.miningSocket.onerror = (error) => {
            console.error('Mining WebSocket error:', error);
          };
  
          this.energySocket = new WebSocket(`ws://localhost:8001/ws/energy/${userId}/`);
          this.energySocket.onmessage = this.onEnergyMessage;
          this.energySocket.onopen = () => {
            console.log('Energy WebSocket connection established');
            this.startEnergyUpdate();
          };
          this.energySocket.onclose = () => {
            console.log('Energy WebSocket connection closed');
          };
          this.energySocket.onerror = (error) => {
            console.error('Energy WebSocket error:', error);
          };
        },
  
        onMessage(event) {
          const data = JSON.parse(event.data);
          app.config.globalProperties.$user.data.balance = data.balance;
          app.config.globalProperties.$user.data.energy = data.energy;
        },
  
        onMiningMessage(event) {
          const data = JSON.parse(event.data);
          app.config.globalProperties.$user.data.balance = data.balance;
          app.config.globalProperties.$user.data.energy = data.energy;
        },
  
        onEnergyMessage(event) {
          const data = JSON.parse(event.data);
          app.config.globalProperties.$user.data.energy = data.energy;
        },
  
        formatTime(duration) {
          const hours = Math.floor(duration / 3600);
          const minutes = Math.floor((duration % 3600) / 60);
          const seconds = Math.floor(duration % 60);
  
          return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        },
  
        updateRemainingTime() {
          if (this.remainingTime > 0) {
            this.remainingTime -= 1;
          }
        },
  
        startMiningTimer() {
          if (this.miningTimer) {
            clearInterval(this.miningTimer);
          }
          this.miningTimer = setInterval(() => {
            if (this.remainingTime > 0) {
              const now = new Date().getTime();
              const miningEndTime = new Date(app.config.globalProperties.$user.data.mining_end).getTime();
              if (now < miningEndTime && this.miningSocket) {
                const message = {
                  user_id: app.config.globalProperties.$user.data.user_id,
                  gph: app.config.globalProperties.$user.data.gph,
                };
                this.miningSocket.send(JSON.stringify(message));
              } else {
                clearInterval(this.miningTimer);
              }
            } else {
              clearInterval(this.miningTimer);
            }
          }, 5000);
        },
  
        startEnergyUpdate() {
          setInterval(() => {
            if (this.energySocket) {
              const message = {
                user_id: app.config.globalProperties.$user.data.user_id,
              };
              this.energySocket.send(JSON.stringify(message));
            }
          }, 5000);
        },
      };
  
      app.config.globalProperties.$websocket = websocketPlugin;
    }
  };
  