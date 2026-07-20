const gpioConnection = require('./gpio');

const test1 = async () => {
    console.log('LED on')

    try {
        const result = await gpioConnection({ type: 'led', order: 'on' });

        console.log(result)

        return { status: 'success', data: 'test1' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}
const test2 = () => {
    return { status: 'success', data: 'test2' }
}
const test3 = () => {
    return { status: 'success', data: 'test3' }
}

module.exports = {
    test1,
    test2,
    test3
};  