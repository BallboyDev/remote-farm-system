const express = require('express')
const router = express.Router()

const testService = require('./test.service')

router.get('/test1', async (req, res) => {
    console.log('test route1')

    const result = await testService.test1()
    res.json(result)
})

router.get('/test2', async (req, res) => {
    console.log('test route2')

    const result = await testService.test2()
    res.json(result)
})

router.get('/test3', async (req, res) => {
    console.log('test route3')

    const result = await testService.test3()
    res.json(result)
})

router.get('/test4', async (req, res) => {
    console.log('test route4')

    const result = await testService.test4()
    res.json(result)
})

router.get('/test5', async (req, res) => {
    console.log('test route5')

    const result = await testService.test5()
    res.json(result)
})

router.get('/test6', async (req, res) => {
    console.log('test route6')

    const result = await testService.test6()
    res.json(result)
})

router.get('/test7', async (req, res) => {
    console.log('test route7')

    const result = await testService.test7()
    res.json(result)
})

router.get('/test8', async (req, res) => {
    console.log('test route8')

    const result = await testService.test8()
    res.json(result)
})

router.get('/test9', async (req, res) => {
    console.log('test route9')

    const result = await testService.test9()
    res.json(result)
})

module.exports = router