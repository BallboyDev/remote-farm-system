const express = require('express');
const router = express.Router();

const gateService = require('./gate.service')

router.get('/test', (req, res) => {
    res.send('Gate test route');
});

router.get('/open', (req, res) => {
    console.log("Gate open route called");

    const result = gateService.openGate();

    res.json(result);
});

router.get('/close', (req, res) => {
    const result = gateService.closeGate();

    res.json(result);
});

module.exports = router;