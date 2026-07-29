const gpioConnection = require('./gpio');

const test1 = async () => {

    try {
        const order = { device: 'led', command: 'on' }
        const result = await gpioConnection(order);

        console.log(result)

        return { status: 'success', data: 'test1' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}
const test2 = async () => {

    try {
        const order = { device: 'led', command: 'off' }
        const result = await gpioConnection(order);

        console.log(result)

        return { status: 'success', data: 'test2' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }
}
const test3 = async () => {

    try {
        const order = { device: 'test', command: 'off' }
        const result = await gpioConnection(order);

        console.log(result)

        return { status: 'success', data: 'test3' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }
}

module.exports = {
    test1,
    test2,
    test3
};  