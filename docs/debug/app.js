const express = require('express');


const PORT = process.argv[2];
const HOST =  process.argv[3];

const app = express();

app.get("/", function (req, res) {
    res.sendFile(__dirname + '/static/index.html')
});

app.listen(PORT, HOST);

console.log(`Running app on http://${HOST}:${PORT}`);