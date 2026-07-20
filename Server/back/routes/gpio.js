const net = require('node:net')

const gpioConnection = (command) => {

    const order = JSON.stringify(command)

    return new Promise((resolve, reject) => {
        const client = net.createConnection(
            {
                host: "127.0.0.1",
                port: 8888,
            },
            () => {
                client.write(order);
            }
        );

        client.on("data", (data) => {
            resolve(data.toString());
            client.end();
        });

        client.on("error", (error) => {
            reject(error);
        });

        client.setTimeout(3000, () => {
            client.destroy();
            reject(new Error("Python 서버 응답 시간 초과"));
        });
    });
}

module.exports = gpioConnection