const gpioConnection = require('./gpio');

const order = [
    { index: 1, device: 'led', command: 'on' },
    { index: 2, device: 'led', command: 'off' },
    { index: 3, device: '', command: '' },
    { index: 4, device: 'ir', command: 'transmit' },
    { index: 5, device: 'ir', command: 'test' },
    { index: 6, device: '', command: '' },
    { index: 7, device: '', command: '' },
    { index: 8, device: '', command: '' },
    { index: 9, device: '', command: '' },
]

const test1 = async () => {

    try {
        const result = await gpioConnection(order[0]);

        console.log(result)

        return { status: 'success', data: 'test1' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test2 = async () => {

    try {
        const result = await gpioConnection(order[1]);

        console.log(result)

        return { status: 'success', data: 'test2' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test3 = async () => {

    try {
        const result = await gpioConnection(order[2]);

        console.log(result)

        return { status: 'success', data: 'test3' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test4 = async () => {

    try {
        const result = await gpioConnection(order[3]);

        console.log(result)

        return { status: 'success', data: 'test4' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test5 = async () => {

    try {
        const result = await gpioConnection(order[4]);

        console.log(result)

        return { status: 'success', data: 'test5' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test6 = async () => {

    try {
        const result = await gpioConnection(order[5]);

        console.log(result)

        return { status: 'success', data: 'test6' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test7 = async () => {

    try {
        const result = await gpioConnection(order[6]);

        console.log(result)

        return { status: 'success', data: 'test7' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test8 = async () => {

    try {
        const result = await gpioConnection(order[7]);

        console.log(result)

        return { status: 'success', data: 'test8' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

const test9 = async () => {

    try {
        const result = await gpioConnection(order[8]);

        console.log(result)

        return { status: 'success', data: 'test9' }
    } catch (err) {
        console.log(err)
        return { status: 'failure', data: err }
    }

}

module.exports = {
    test1,
    test2,
    test3,
    test4,
    test5,
    test6,
    test7,
    test8,
    test9,
};  