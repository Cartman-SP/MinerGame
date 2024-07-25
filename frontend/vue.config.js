const fs = require('fs');
const path = require('path');

module.exports = {
  devServer: {
    allowedHosts: 'all',
    host: '0.0.0.0',
    port: 8080,
    https: {
      key: fs.readFileSync(path.resolve(__dirname, 'localhost-key.pem')),
      cert: fs.readFileSync(path.resolve(__dirname, 'localhost.pem')),
    },
    client: {
      webSocketURL: {
        hostname: '0.0.0.0',
        pathname: '/ws',
        port: 8080,
        protocol: 'wss',
      },
    },
  },
};

