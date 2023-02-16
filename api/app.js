const express = require('express');
const app = express();
const port = 3000;
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
const { MongoClient } = require("mongodb");

app.listen(port, () => {
    console.log(`CompostBuddy API listening on port ${port}`);
  });

// GET ////////////////////////////////////////////////////////////////////////

app.get('/api/datetime', (req, res) => {
    let date = new Date();
    let localDate = 
        new Date(date.getTime() - date.getTimezoneOffset()*60000);
    res.send(localDate.toISOString());
});

app.get('/api/version', (req, res) => {
    res.send('1.0.0');
});




// POST ///////////////////////////////////////////////////////////////////////

app.post('/api/compost', function(req, res) {

    req.body.timestamp = new Date();

    const uptime = req.body.uptime;
    const lastTurn = req.body.lastTurn;
    const batt = req.body.batt;

    async function run() {
        const uri = "mongodb://localhost:27017/";
        const client = new MongoClient(uri);
        await client.connect();
        let db = client.db("compost");
        await db.collection("esp32").insertOne(req.body);
        await client.close();

    };
    run().catch(console.dir);

    res.send({
        'uptime': uptime,
        'lastTurn': lastTurn,
        'batt': batt+1
    });
});
