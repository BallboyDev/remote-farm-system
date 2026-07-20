const express = require('express');
const router = express.Router();
const testRoutes = require('./test.routes');
const loginRoutes = require('./login.routes');
const gateRoutes = require('./gate.routes');

router.use('/test', testRoutes);

router.use('/user', loginRoutes);

router.use('/gate', gateRoutes)

module.exports = router;