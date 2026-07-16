const express = require('express');
const router = express.Router();
const loginRoutes = require('./login.routes');
const gateRoutes = require('./gate.routes');

router.use('/login', loginRoutes);

router.use('/gate', gateRoutes)

module.exports = router;