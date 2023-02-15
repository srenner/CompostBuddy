const express = require('express');
const app = express();
const port = 3000;
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/api/datetime', (req, res) => {
    let date = new Date();
    let localDate = new Date(date.getTime() - date.getTimezoneOffset()*60000);
    res.send(localDate.toISOString());
});

app.get('/api/version', (req, res) => {
    res.send('1.0.0');
});

app.post('/api/compost', function(req, res) {
    const uptime = req.body.uptime;
    const lastTurn = req.body.lastTurn;
    const batt = req.body.batt;

    //do the needful

    res.send({
        'uptime': uptime,
        'lastTurn': lastTurn,
        'batt': batt+1
    });
});

app.listen(port, () => {
  console.log(`CompostBuddy API listening on port ${port}`);
});