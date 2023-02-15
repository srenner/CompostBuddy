const express = require('express');
const app = express();
const port = 3000;

app.get('/api/heartbeat', (req, res) => {
  res.send(new Date().toISOString());
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});