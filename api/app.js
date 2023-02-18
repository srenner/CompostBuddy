const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
const { MongoClient } = require("mongodb");
const meta = require('./package.json');
const mongoURI = 'mongodb://localhost:27017/';

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
    res.send(meta.version);
});

app.get('/api/compost/latest', (req, res) => {
    async function run() {
        const filter = {};
        const client = await MongoClient.connect(
            mongoURI,
            { useNewUrlParser: true, useUnifiedTopology: true }
        );
        const coll = client.db('compost').collection('esp32');
        const cursor = coll.find(filter);
        const result = await coll.findOne({}, {sort: {timestamp: -1}});
        await client.close();
        console.log("GET " + JSON.stringify(result));
        res.send(result);
    };
    run().catch(console.dir);
});


// POST ///////////////////////////////////////////////////////////////////////

app.post('/api/compost', function(req, res) {
    req.body.timestamp = new Date();
    const uptime = req.body.uptime;
    const lastTurn = req.body.lastTurn;
    const batt = req.body.batt;

    async function run() {
        const client = new MongoClient(mongoURI);
        await client.connect();
        let db = client.db("compost");
        await db.collection("esp32").insertOne(req.body);
        await client.close();
        console.log("POSTed " + JSON.stringify(req.body));
    };
    run().catch(console.dir);
    res.send({});
});
