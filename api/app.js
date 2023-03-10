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
    //let localDate = 
    //    new Date(date.getTime() - date.getTimezoneOffset()*60000);
    console.log("GET " + date.toISOString())
    res.send(date.toISOString());
});

app.get('/api/version', (req, res) => {
    res.send(meta.version);
});

app.get('/api/event/latest', (req, res) => {
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

app.get('/api/events', (req, res) =>{
    async function run() {

        let inputStartDate = req.query.start;
        let inputEndDate = req.query.end;

        let startDate = new Date(inputStartDate).toUTCString();
        let endDate = new Date(inputEndDate).toISOString();

        const filter = {
            'timestamp': {
              '$gte': new Date(startDate), 
              '$lte': new Date(endDate)
            }
          };
        const client = await MongoClient.connect(mongoURI,
            { useNewUrlParser: true, useUnifiedTopology: true }
        );
        const coll = client.db('compost').collection('esp32');
        const cursor = coll.find(filter);
        const result = await cursor.toArray();

        await client.close();
        res.send(result);
    };
    run().catch(console.dir);
});


// POST ///////////////////////////////////////////////////////////////////////

app.post('/api/compost', function(req, res) {
    
    let datapoints = req.body;
    let len = datapoints.length;

    if(len > 0) {
        let now = new Date();
        let maxtime = Math.max.apply(Math,datapoints.map(function(o){return o.timeref;}))

        datapoints.forEach(function (d) {
            let timediff = maxtime - d.timeref;
            let date = new Date(now.valueOf());
            d.timestamp = new Date(date.setSeconds(date.getSeconds() - timediff));
            console.log(d);
          });

          async function run() {
            const client = new MongoClient(mongoURI);
            await client.connect();
            let db = client.db("compost");
            await db.collection("esp32").insertMany(datapoints);
            await client.close();
            //console.log("POSTed " + JSON.stringify(req.body));
        };
        run().catch(console.dir);
        res.send({});

    }    
    console.log("POST: " + len.toString() + " datapoint(s)");
});
