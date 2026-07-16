const express = require('express');

const router = express.Router();

const loginService = require('./login.service')

router.get('/', (req, res) => {
    res.send('Login route');
});

router.post('/', (req, res) => {

    const { id } = req.body;

    const result = loginService.login(id);

    res.json(result);
});

module.exports = router;