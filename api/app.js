const express = require('express');
const app = express();
const port = 3000;

app.get('/api/heartbeat', (req, res) => {
  let date = new Date();
  let localDate = new Date(date.getTime() - date.getTimezoneOffset()*60000);
  res.send(localDate.toISOString());
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});