const express = require('express')
const router = express.Router()

const testService = require('./test.service')

router.get('/test1', async (req, res) => {
    console.log('test route1')

    const result = await testService.test1()
    res.json(result)
})
router.get('/test2', (req, res) => {
    console.log('test route2')

    const result = testService.test2()
    res.json(result)
})
router.get('/test3', (req, res) => {
    console.log('test route3')

    const result = testService.test3()
    res.json(result)
})

module.exports = router